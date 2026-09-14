"""
Regression tests for the canonical GEO projection.

This module verifies the projection sector independently
of any Hubble-scale application.

Canonical architecture
----------------------

    eta = 3/5
    A   = eta
    B   = 1 - eta
    theta = pi/4

Projection operator

        [ cos(theta)   sin(theta) ]
    Q = [                         ]
        [-sin(theta)   cos(theta) ]

Applied to

    v = (A, B)

gives

    A' = A cos(theta) + B sin(theta)
    B' = -A sin(theta) + B cos(theta)

At theta = pi/4 and A+B=1:

    A' = 1/sqrt(2)

For A=3/5 and B=2/5:

    B' = -1/(5 sqrt(2))

The canonical coupling amplitude is

    f_c = sqrt(eta)

and the dimensionless projection factor is

    P_geo = f_c / A'
          = sqrt(6/5)

No Hubble measurement is used in these tests.
"""

import math

from geo_external_operator import compute


# =============================================================================
# CANONICAL PARAMETERS
# =============================================================================

ETA = 3.0 / 5.0
A = ETA
B = 1.0 - ETA

L = 0.0

THETA = math.pi / 4.0

# mu_eff is required by the engine, but it does not enter the
# analytic derivation of the canonical projection factor.
MU_REFERENCE = 0.8104

TOL = 1.0e-13


# =============================================================================
# HELPERS
# =============================================================================

def projection_matrix(theta: float):
    """
    Return the canonical two-dimensional GEO rotation/projection matrix.

        Q(theta) =
            [ cos(theta)   sin(theta) ]
            [-sin(theta)   cos(theta) ]
    """

    c = math.cos(theta)
    s = math.sin(theta)

    return (
        (c, s),
        (-s, c),
    )


def apply_projection(a: float, b: float, theta: float):
    """
    Apply Q(theta) to the state vector (a,b).
    """

    q = projection_matrix(theta)

    a_prime = (
        q[0][0] * a
        + q[0][1] * b
    )

    b_prime = (
        q[1][0] * a
        + q[1][1] * b
    )

    return a_prime, b_prime


def inverse_projection(
    a_prime: float,
    b_prime: float,
    theta: float,
):
    """
    Since Q is orthogonal,

        Q^{-1} = Q^T.

    Reconstruct the original state.
    """

    c = math.cos(theta)
    s = math.sin(theta)

    a = (
        c * a_prime
        - s * b_prime
    )

    b = (
        s * a_prime
        + c * b_prime
    )

    return a, b


# =============================================================================
# TEST 1 — CONSERVATIVE STATE
# =============================================================================

def test_canonical_partition():

    assert abs((A + B) - 1.0) < TOL

    assert abs(A - 0.6) < TOL
    assert abs(B - 0.4) < TOL


# =============================================================================
# TEST 2 — ORTHOGONAL PROJECTION MATRIX
# =============================================================================

def test_projection_matrix_is_orthogonal():

    q = projection_matrix(THETA)

    q00, q01 = q[0]
    q10, q11 = q[1]

    # Q^T Q

    m00 = q00 * q00 + q10 * q10
    m01 = q00 * q01 + q10 * q11
    m10 = q01 * q00 + q11 * q10
    m11 = q01 * q01 + q11 * q11

    assert abs(m00 - 1.0) < TOL
    assert abs(m01) < TOL
    assert abs(m10) < TOL
    assert abs(m11 - 1.0) < TOL

    determinant = (
        q00 * q11
        - q01 * q10
    )

    assert abs(determinant - 1.0) < TOL


# =============================================================================
# TEST 3 — CANONICAL 45-DEGREE PROJECTION
# =============================================================================

def test_canonical_projection_closed_form():

    a_prime, b_prime = apply_projection(
        A,
        B,
        THETA,
    )

    expected_a_prime = 1.0 / math.sqrt(2.0)

    expected_b_prime = (
        -1.0
        / (5.0 * math.sqrt(2.0))
    )

    assert abs(
        a_prime - expected_a_prime
    ) < TOL

    assert abs(
        b_prime - expected_b_prime
    ) < TOL


# =============================================================================
# TEST 4 — NORM PRESERVATION
# =============================================================================

def test_projection_preserves_norm():

    a_prime, b_prime = apply_projection(
        A,
        B,
        THETA,
    )

    norm_before = (
        A * A
        + B * B
    )

    norm_after = (
        a_prime * a_prime
        + b_prime * b_prime
    )

    assert abs(
        norm_before - norm_after
    ) < TOL


# =============================================================================
# TEST 5 — INVERSE RECONSTRUCTION
# =============================================================================

def test_inverse_projection_reconstructs_state():

    a_prime, b_prime = apply_projection(
        A,
        B,
        THETA,
    )

    a_reconstructed, b_reconstructed = inverse_projection(
        a_prime,
        b_prime,
        THETA,
    )

    assert abs(
        a_reconstructed - A
    ) < TOL

    assert abs(
        b_reconstructed - B
    ) < TOL


# =============================================================================
# TEST 6 — EXTERNAL OPERATOR AGREEMENT
# =============================================================================

def test_external_operator_matches_analytic_projection():

    g = compute(
        eta=ETA,
        L=L,
        mu_eff=MU_REFERENCE,
    )

    a_prime, b_prime = apply_projection(
        A,
        B,
        THETA,
    )

    assert abs(
        g.projected_observable
        - a_prime
    ) < TOL

    assert abs(
        g.projected_complementary
        - b_prime
    ) < TOL


# =============================================================================
# TEST 7 — EXTERNAL OPERATOR INVERSE RECONSTRUCTION
# =============================================================================

def test_external_operator_reconstructs_original_state():

    g = compute(
        eta=ETA,
        L=L,
        mu_eff=MU_REFERENCE,
    )

    assert abs(
        g.reconstructed_observable
        - A
    ) < TOL

    assert abs(
        g.reconstructed_complementary
        - B
    ) < TOL

    assert abs(
        g.reconstructed_latent
        - L
    ) < TOL


# =============================================================================
# TEST 8 — ENGINE NUMERICAL CLOSURE
# =============================================================================

def test_external_operator_projection_norm_closure():

    g = compute(
        eta=ETA,
        L=L,
        mu_eff=MU_REFERENCE,
    )

    assert abs(
        g.projection_norm_error
    ) < TOL

    assert abs(
        g.reconstruction_observable_error
    ) < TOL

    assert abs(
        g.reconstruction_complementary_error
    ) < TOL

    assert abs(
        g.reconstruction_latent_error
    ) < TOL


# =============================================================================
# TEST 9 — CANONICAL COUPLING
# =============================================================================

def test_canonical_coupling_amplitude():

    fc = math.sqrt(ETA)

    assert abs(
        fc * fc - ETA
    ) < TOL

    assert abs(
        fc - math.sqrt(3.0 / 5.0)
    ) < TOL


# =============================================================================
# TEST 10 — GEO PROJECTION FACTOR
# =============================================================================

def test_projection_factor_closed_form():

    a_prime, _ = apply_projection(
        A,
        B,
        THETA,
    )

    fc = math.sqrt(ETA)

    p_geo = fc / a_prime

    expected = math.sqrt(6.0 / 5.0)

    assert abs(
        p_geo - expected
    ) < TOL


# =============================================================================
# TEST 11 — ENGINE PROJECTION FACTOR
# =============================================================================

def test_engine_projection_factor_closed_form():

    g = compute(
        eta=ETA,
        L=L,
        mu_eff=MU_REFERENCE,
    )

    fc_engine = math.sqrt(g.eta)

    p_geo_engine = (
        fc_engine
        / g.projected_observable
    )

    expected = math.sqrt(6.0 / 5.0)

    assert abs(
        p_geo_engine - expected
    ) < TOL


# =============================================================================
# TEST 12 — ANALYTIC / ENGINE FACTOR AGREEMENT
# =============================================================================

def test_analytic_and_engine_projection_factors_match():

    a_prime, _ = apply_projection(
        A,
        B,
        THETA,
    )

    p_analytic = (
        math.sqrt(ETA)
        / a_prime
    )

    g = compute(
        eta=ETA,
        L=L,
        mu_eff=MU_REFERENCE,
    )

    p_engine = (
        math.sqrt(g.eta)
        / g.projected_observable
    )

    assert abs(
        p_analytic - p_engine
    ) < TOL
