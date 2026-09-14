"""
Regression tests for the GEO-Hubble projection factor.

These tests verify the final application layer only.

The geometric result is derived first:

    eta = 3/5
    f_c = sqrt(eta)

    A + B = 1
    theta = pi/4

    A' = 1/sqrt(2)

therefore

    P_geo = f_c / A'
          = sqrt(6/5)

The Hubble application is then introduced separately as:

    H_geo = H_base * P_geo

Important
---------
The tests distinguish between:

1. mathematical result:
       P_geo = sqrt(6/5)

2. physical application hypothesis:
       H_geo / H_base = P_geo

No local-H0 target is used to determine P_geo.
"""

import math

import pytest

from geo_external_operator import compute


# =============================================================================
# CANONICAL GEO ARCHITECTURE
# =============================================================================

ETA = 3.0 / 5.0
L = 0.0

A = ETA
B = 1.0 - ETA

THETA = math.pi / 4.0

# Required by the engine API.
# The final projection factor must not depend on this choice.
MU_REFERENCE = 0.8104

TOL = 1.0e-13
TOL_H = 1.0e-11


# =============================================================================
# HELPERS
# =============================================================================

def analytic_projected_observable() -> float:
    """
    Compute the observable projection analytically.
    """

    c = math.cos(THETA)
    s = math.sin(THETA)

    return (
        A * c
        + B * s
    )


def analytic_projection_factor() -> float:
    """
    Construct P_geo entirely from the canonical analytic geometry.
    """

    fc = math.sqrt(ETA)

    a_prime = analytic_projected_observable()

    return fc / a_prime


def engine_projection_factor(mu_eff: float = MU_REFERENCE) -> float:
    """
    Construct P_geo from quantities returned by the
    GEO External Operator.
    """

    g = compute(
        eta=ETA,
        L=L,
        mu_eff=mu_eff,
    )

    fc = math.sqrt(g.eta)

    return (
        fc
        / g.projected_observable
    )


def project_hubble(
    h_base: float,
    p_geo: float,
) -> float:
    """
    Apply the declared GEO-Hubble mapping.
    """

    return h_base * p_geo


# =============================================================================
# TEST 1 — CLOSED-FORM GEOMETRIC FACTOR
# =============================================================================

def test_hubble_projection_factor_closed_form():

    p_geo = analytic_projection_factor()

    expected = math.sqrt(6.0 / 5.0)

    assert abs(
        p_geo - expected
    ) < TOL


# =============================================================================
# TEST 2 — EXPLICIT DERIVATION OF A'
# =============================================================================

def test_projected_observable_is_inverse_sqrt_two():

    a_prime = analytic_projected_observable()

    expected = 1.0 / math.sqrt(2.0)

    assert abs(
        a_prime - expected
    ) < TOL


# =============================================================================
# TEST 3 — OLD SIMPLE GEO FORM AND NEW CLOSED FORM AGREE
# =============================================================================

def test_fc_over_cos45_equals_sqrt_six_fifths():

    fc = math.sqrt(ETA)

    simple_form = (
        fc
        / math.cos(THETA)
    )

    closed_form = math.sqrt(6.0 / 5.0)

    assert abs(
        simple_form - closed_form
    ) < TOL


# =============================================================================
# TEST 4 — FULL Q PROJECTION REDUCES TO COS(45)
# =============================================================================

def test_full_projection_reduces_to_cos45():

    a_prime = analytic_projected_observable()

    cos45 = math.cos(THETA)

    assert abs(
        a_prime - cos45
    ) < TOL


# =============================================================================
# TEST 5 — ANALYTIC AND ENGINE FACTORS AGREE
# =============================================================================

def test_analytic_and_engine_hubble_factors_agree():

    p_analytic = analytic_projection_factor()

    p_engine = engine_projection_factor()

    assert abs(
        p_analytic - p_engine
    ) < TOL


# =============================================================================
# TEST 6 — ENGINE FACTOR MATCHES CLOSED FORM
# =============================================================================

def test_engine_hubble_factor_matches_closed_form():

    p_engine = engine_projection_factor()

    expected = math.sqrt(6.0 / 5.0)

    assert abs(
        p_engine - expected
    ) < TOL


# =============================================================================
# TEST 7 — REFERENCE NUMERICAL APPLICATION
# =============================================================================

def test_reference_hubble_projection():

    h_base = 67.4

    p_geo = math.sqrt(6.0 / 5.0)

    h_geo = project_hubble(
        h_base,
        p_geo,
    )

    expected = 73.833000751696

    assert abs(
        h_geo - expected
    ) < TOL_H


# =============================================================================
# TEST 8 — REFERENCE SHIFT
# =============================================================================

def test_reference_fractional_shift():

    p_geo = math.sqrt(6.0 / 5.0)

    fractional_shift = p_geo - 1.0

    expected = 0.095445115010332

    assert abs(
        fractional_shift - expected
    ) < TOL


# =============================================================================
# TEST 9 — HUBBLE INPUT DOES NOT DETERMINE P_GEO
# =============================================================================

@pytest.mark.parametrize(
    "h_base",
    (
        50.0,
        60.0,
        67.4,
        70.0,
        73.0,
        80.0,
        100.0,
    ),
)
def test_projection_factor_is_independent_of_hubble_input(
    h_base,
):

    # Deliberately compute P_geo without using h_base.

    p_geo = analytic_projection_factor()

    expected = math.sqrt(6.0 / 5.0)

    assert abs(
        p_geo - expected
    ) < TOL

    # h_base enters only after P_geo exists.

    h_geo = project_hubble(
        h_base,
        p_geo,
    )

    assert abs(
        h_geo / h_base - expected
    ) < TOL


# =============================================================================
# TEST 10 — LINEAR HUBBLE MAPPING
# =============================================================================

@pytest.mark.parametrize(
    "h_base",
    (
        50.0,
        60.0,
        67.4,
        70.0,
        80.0,
        100.0,
    ),
)
def test_hubble_mapping_is_linear(h_base):

    p_geo = analytic_projection_factor()

    h_geo = project_hubble(
        h_base,
        p_geo,
    )

    assert abs(
        h_geo - h_base * p_geo
    ) < TOL_H


# =============================================================================
# TEST 11 — MU_EFF DOES NOT DETERMINE HUBBLE FACTOR
# =============================================================================

@pytest.mark.parametrize(
    "mu_eff",
    (
        0.20,
        0.40,
        0.60,
        0.80,
        0.8104,
        1.00,
    ),
)
def test_hubble_factor_is_independent_of_mu_eff(mu_eff):

    p_engine = engine_projection_factor(
        mu_eff=mu_eff,
    )

    expected = math.sqrt(6.0 / 5.0)

    assert abs(
        p_engine - expected
    ) < TOL


# =============================================================================
# TEST 12 — RADIAL STATE MAY CHANGE WITHOUT CHANGING HUBBLE FACTOR
# =============================================================================

def test_radial_change_does_not_change_projection_factor():

    g1 = compute(
        eta=ETA,
        L=L,
        mu_eff=0.60,
    )

    g2 = compute(
        eta=ETA,
        L=L,
        mu_eff=0.8104,
    )

    # Radial sector must actually differ.

    assert abs(
        g1.R - g2.R
    ) > 1.0e-8

    # Projection factor remains the same.

    p1 = (
        math.sqrt(g1.eta)
        / g1.projected_observable
    )

    p2 = (
        math.sqrt(g2.eta)
        / g2.projected_observable
    )

    assert abs(
        p1 - p2
    ) < TOL


# =============================================================================
# TEST 13 — DIMENSIONLESS FACTOR
# =============================================================================

def test_projection_factor_is_pure_ratio():

    fc = math.sqrt(ETA)

    a_prime = analytic_projected_observable()

    p_geo = fc / a_prime

    assert math.isfinite(p_geo)

    assert p_geo > 0.0

    assert abs(
        p_geo - math.sqrt(6.0 / 5.0)
    ) < TOL


# =============================================================================
# TEST 14 — REFERENCE ENGINE APPLICATION
# =============================================================================

def test_reference_hubble_projection_using_engine():

    h_base = 67.4

    p_engine = engine_projection_factor()

    h_geo = project_hubble(
        h_base,
        p_engine,
    )

    h_closed = (
        h_base
        * math.sqrt(6.0 / 5.0)
    )

    assert abs(
        h_geo - h_closed
    ) < TOL_H
