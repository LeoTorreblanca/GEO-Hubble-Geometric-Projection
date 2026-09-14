"""
Regression tests for GEO mu_eff / eta independence.

Purpose
-------
Protect the corrected GEO architecture against the historical
shortcut

    mu_eff = eta

being reintroduced as a universal identity.

The canonical architecture fixes

    eta = 3/5

while the radial state obeys

    R = mu_eff^(1/3).

Therefore eta and mu_eff have distinct mathematical roles.

Under the tested canonical projection architecture:

    eta -> A, B, f_c
    mu_eff -> R -> Phi, alpha

Changing mu_eff must change the radial sector while leaving
the canonical projection sector unchanged.

No Hubble measurement is used in this test module.
"""

import math

import pytest

from geo_external_operator import compute


# =============================================================================
# CANONICAL ARCHITECTURE
# =============================================================================

ETA = 3.0 / 5.0
L = 0.0

A = ETA
B = 1.0 - ETA

THETA = math.pi / 4.0

FC_EXPECTED = math.sqrt(ETA)

A_PRIME_EXPECTED = 1.0 / math.sqrt(2.0)

P_EXPECTED = math.sqrt(6.0 / 5.0)

TOL = 1.0e-13
CHANGE_TOL = 1.0e-8


MU_VALUES = (
    0.10,
    0.20,
    0.30,
    0.40,
    0.50,
    0.60,
    0.70,
    0.80,
    0.8104,
    0.90,
    1.00,
)


# =============================================================================
# HELPERS
# =============================================================================

def real_cuberoot(x: float) -> float:
    """
    Real-valued cube root.
    """

    if x >= 0.0:
        return x ** (1.0 / 3.0)

    return -((-x) ** (1.0 / 3.0))


def geo_state(mu_eff: float):
    """
    Evaluate the public GEO External Operator at fixed architecture
    and variable effective radial state.
    """

    return compute(
        eta=ETA,
        L=L,
        mu_eff=mu_eff,
    )


def projection_factor(g) -> float:
    """
    Construct the canonical external projection factor from
    engine-returned quantities.
    """

    fc = math.sqrt(g.eta)

    return (
        fc
        / g.projected_observable
    )


# =============================================================================
# TEST 1 — ETA IS FIXED WHILE MU_EFF VARIES
# =============================================================================

@pytest.mark.parametrize(
    "mu_eff",
    MU_VALUES,
)
def test_eta_is_independent_input_from_mu_eff(mu_eff):

    g = geo_state(mu_eff)

    assert abs(
        g.eta - ETA
    ) < TOL


# =============================================================================
# TEST 2 — ENGINE PRESERVES MU_EFF
# =============================================================================

@pytest.mark.parametrize(
    "mu_eff",
    MU_VALUES,
)
def test_engine_preserves_requested_mu_eff(mu_eff):

    g = geo_state(mu_eff)

    assert abs(
        g.mu_eff - mu_eff
    ) < TOL


# =============================================================================
# TEST 3 — CORRECT RADIAL LAW
# =============================================================================

@pytest.mark.parametrize(
    "mu_eff",
    MU_VALUES,
)
def test_radial_law_depends_on_mu_eff(mu_eff):

    g = geo_state(mu_eff)

    expected_R = real_cuberoot(mu_eff)

    assert abs(
        g.R - expected_R
    ) < TOL

    assert abs(
        g.R ** 3 - mu_eff
    ) < TOL


# =============================================================================
# TEST 4 — ETA^(1/3) IS NOT THE GENERAL RADIAL LAW
# =============================================================================

@pytest.mark.parametrize(
    "mu_eff",
    [
        value
        for value in MU_VALUES
        if not math.isclose(
            value,
            ETA,
            rel_tol=0.0,
            abs_tol=1.0e-15,
        )
    ],
)
def test_eta_cuberoot_shortcut_fails_when_mu_differs_from_eta(
    mu_eff,
):

    g = geo_state(mu_eff)

    wrong_general_shortcut = real_cuberoot(ETA)

    assert abs(
        g.R - wrong_general_shortcut
    ) > CHANGE_TOL


# =============================================================================
# TEST 5 — SPECIAL NUMERICAL EQUALITY IS NOT UNIVERSAL IDENTITY
# =============================================================================

def test_mu_equal_eta_is_only_a_special_state():

    g_equal = geo_state(ETA)

    g_other = geo_state(0.8104)

    # At the special point mu_eff = eta, both cube roots
    # are numerically equal.

    assert abs(
        g_equal.R - real_cuberoot(ETA)
    ) < TOL

    # But moving mu_eff while eta remains fixed changes R.

    assert abs(
        g_other.eta - g_equal.eta
    ) < TOL

    assert abs(
        g_other.mu_eff - g_equal.mu_eff
    ) > CHANGE_TOL

    assert abs(
        g_other.R - g_equal.R
    ) > CHANGE_TOL


# =============================================================================
# TEST 6 — RADIAL RESPONSE IS NONTRIVIAL
# =============================================================================

def test_radial_sector_changes_across_mu_sweep():

    states = [
        geo_state(mu)
        for mu in MU_VALUES
    ]

    radial_values = [
        g.R
        for g in states
    ]

    radial_span = (
        max(radial_values)
        - min(radial_values)
    )

    assert radial_span > CHANGE_TOL


# =============================================================================
# TEST 7 — PHI RESPONDS TO RADIAL STATE
# =============================================================================

def test_phi_changes_across_mu_sweep():

    states = [
        geo_state(mu)
        for mu in MU_VALUES
    ]

    phi_values = [
        g.Phi
        for g in states
    ]

    phi_span = (
        max(phi_values)
        - min(phi_values)
    )

    assert phi_span > CHANGE_TOL


# =============================================================================
# TEST 8 — ALPHA RESPONDS TO RADIAL STATE
# =============================================================================

def test_alpha_changes_across_mu_sweep():

    states = [
        geo_state(mu)
        for mu in MU_VALUES
    ]

    alpha_values = [
        g.alpha
        for g in states
    ]

    alpha_span = (
        max(alpha_values)
        - min(alpha_values)
    )

    assert alpha_span > CHANGE_TOL


# =============================================================================
# TEST 9 — PROJECTED OBSERVABLE DOES NOT FOLLOW MU_EFF
# =============================================================================

@pytest.mark.parametrize(
    "mu_eff",
    MU_VALUES,
)
def test_projected_observable_is_mu_independent(mu_eff):

    g = geo_state(mu_eff)

    assert abs(
        g.projected_observable
        - A_PRIME_EXPECTED
    ) < TOL


# =============================================================================
# TEST 10 — CANONICAL COUPLING DOES NOT FOLLOW MU_EFF
# =============================================================================

@pytest.mark.parametrize(
    "mu_eff",
    MU_VALUES,
)
def test_fc_is_mu_independent(mu_eff):

    g = geo_state(mu_eff)

    fc = math.sqrt(g.eta)

    assert abs(
        fc - FC_EXPECTED
    ) < TOL


# =============================================================================
# TEST 11 — PROJECTION FACTOR DOES NOT FOLLOW MU_EFF
# =============================================================================

@pytest.mark.parametrize(
    "mu_eff",
    MU_VALUES,
)
def test_projection_factor_is_mu_independent(mu_eff):

    g = geo_state(mu_eff)

    p_geo = projection_factor(g)

    assert abs(
        p_geo - P_EXPECTED
    ) < TOL


# =============================================================================
# TEST 12 — GLOBAL RADIAL / PROJECTION SEPARATION
# =============================================================================

def test_radial_changes_while_projection_factor_does_not():

    states = [
        geo_state(mu)
        for mu in MU_VALUES
    ]

    radial_values = [
        g.R
        for g in states
    ]

    projection_values = [
        projection_factor(g)
        for g in states
    ]

    radial_span = (
        max(radial_values)
        - min(radial_values)
    )

    projection_span = (
        max(projection_values)
        - min(projection_values)
    )

    assert radial_span > CHANGE_TOL

    assert projection_span < TOL


# =============================================================================
# TEST 13 — ANALYTIC PROJECTION REMAINS INDEPENDENT OF MU
# =============================================================================

def test_projection_closed_form_contains_no_mu_eff():

    c = math.cos(THETA)
    s = math.sin(THETA)

    a_prime = (
        A * c
        + B * s
    )

    assert abs(
        a_prime
        - 1.0 / math.sqrt(2.0)
    ) < TOL

    fc = math.sqrt(ETA)

    p_geo = fc / a_prime

    assert abs(
        p_geo
        - math.sqrt(6.0 / 5.0)
    ) < TOL


# =============================================================================
# TEST 14 — TWO-STATE EXPLICIT CONTRAST
# =============================================================================

def test_explicit_mu_eta_independence_contrast():

    mu1 = ETA
    mu2 = 0.8104

    g1 = geo_state(mu1)
    g2 = geo_state(mu2)

    # Architecture stays fixed.

    assert abs(
        g1.eta - g2.eta
    ) < TOL

    # Effective state changes.

    assert abs(
        g1.mu_eff - g2.mu_eff
    ) > CHANGE_TOL

    # Radial response changes.

    assert abs(
        g1.R - g2.R
    ) > CHANGE_TOL

    # Derived radial-sector quantities respond.

    assert abs(
        g1.Phi - g2.Phi
    ) > CHANGE_TOL

    assert abs(
        g1.alpha - g2.alpha
    ) > CHANGE_TOL

    # Projection sector remains fixed.

    assert abs(
        g1.projected_observable
        - g2.projected_observable
    ) < TOL

    assert abs(
        projection_factor(g1)
        - projection_factor(g2)
    ) < TOL
