"""
Regression tests for the corrected GEO radial law.

Canonical rule:

    R = mu_eff^(1/3)

The architectural quantity eta must not be substituted for
mu_eff unless a particular application explicitly derives
that identification.
"""

import math

from geo_external_operator import compute


ETA = 3.0 / 5.0
L = 0.0

TOL = 1.0e-13

MU_VALUES = (
    0.10,
    0.20,
    0.40,
    0.60,
    0.8104,
    1.00,
)


def real_cuberoot(x: float) -> float:
    if x >= 0.0:
        return x ** (1.0 / 3.0)

    return -((-x) ** (1.0 / 3.0))


def test_radial_law_matches_mu_eff():

    for mu_eff in MU_VALUES:

        g = compute(
            eta=ETA,
            L=L,
            mu_eff=mu_eff,
        )

        expected = real_cuberoot(mu_eff)

        assert abs(g.R - expected) < TOL


def test_radial_cubic_closure():

    for mu_eff in MU_VALUES:

        g = compute(
            eta=ETA,
            L=L,
            mu_eff=mu_eff,
        )

        assert abs((g.R ** 3) - mu_eff) < TOL


def test_radial_response_changes_when_mu_eff_changes():

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

    assert not math.isclose(
        g1.R,
        g2.R,
        rel_tol=0.0,
        abs_tol=1.0e-6,
    )


def test_eta_remains_fixed_during_mu_variation():

    values = []

    for mu_eff in MU_VALUES:

        g = compute(
            eta=ETA,
            L=L,
            mu_eff=mu_eff,
        )

        values.append(g.eta)

    assert max(values) - min(values) < TOL

    for value in values:
        assert abs(value - ETA) < TOL


def test_eta_cuberoot_is_not_universal_radial_response():

    eta_radial_shortcut = real_cuberoot(ETA)

    mismatches = 0

    for mu_eff in MU_VALUES:

        if math.isclose(
            mu_eff,
            ETA,
            rel_tol=0.0,
            abs_tol=1.0e-15,
        ):
            continue

        g = compute(
            eta=ETA,
            L=L,
            mu_eff=mu_eff,
        )

        if abs(g.R - eta_radial_shortcut) > 1.0e-8:
            mismatches += 1

    expected = sum(
        1
        for mu_eff in MU_VALUES
        if not math.isclose(
            mu_eff,
            ETA,
            rel_tol=0.0,
            abs_tol=1.0e-15,
        )
    )

    assert mismatches == expected
