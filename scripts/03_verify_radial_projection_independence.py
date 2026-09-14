#!/usr/bin/env python3

"""
03_verify_radial_projection_independence.py

GEO-Hubble Geometric Projection
Radial / projection independence test.

Purpose
-------
Test whether the corrected radial sector

    R = mu_eff^(1/3)

is mathematically independent from the canonical external
projection factor

    P_geo = f_c / A'

under the frozen GEO architecture

    eta = 3/5
    A = eta
    B = 1 - eta
    theta = pi/4
    f_c = sqrt(eta).

The test deliberately sweeps mu_eff over a broad interval.

If the architecture is correctly separated, then:

    mu_eff changes
        -> R changes
        -> Phi may change
        -> alpha may change

while

    eta remains fixed
    f_c remains fixed
    A' remains fixed
    P_geo remains fixed.

No Hubble measurement is used.
"""

from __future__ import annotations

import math
import sys
from pathlib import Path

try:
    from geo_external_operator import compute, api_version
except ImportError as exc:
    print("ERROR: geo_external_operator could not be imported.")
    print()
    print(
        "Activate "
        "~/GEO-EXTERNAL-TEST/GEO-External-Operator/.venv/bin/activate"
    )
    print()
    print(exc)
    sys.exit(2)


# =============================================================================
# PATHS
# =============================================================================

SCRIPT_PATH = Path(__file__).resolve()
PROJECT_ROOT = SCRIPT_PATH.parent.parent

RESULTS_DIR = PROJECT_ROOT / "results"
RESULTS_DIR.mkdir(parents=True, exist_ok=True)

OUTPUT_FILE = RESULTS_DIR / "03_radial_projection_independence.txt"


# =============================================================================
# CANONICAL ARCHITECTURE
# =============================================================================

ETA = 3.0 / 5.0
L = 0.0

A = ETA
B = 1.0 - ETA

THETA = math.pi / 4.0

FC_ANALYTIC = math.sqrt(ETA)

A_PRIME_ANALYTIC = (
    A * math.cos(THETA)
    + B * math.sin(THETA)
)

P_ANALYTIC = FC_ANALYTIC / A_PRIME_ANALYTIC

P_CLOSED = math.sqrt(6.0 / 5.0)


# =============================================================================
# RADIAL STATES
# =============================================================================

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
# TOLERANCES
# =============================================================================

TOL = 1.0e-13
CHANGE_THRESHOLD = 1.0e-6


# =============================================================================
# REPORT
# =============================================================================

REPORT_LINES: list[str] = []


def emit(text: str = "") -> None:
    print(text)
    REPORT_LINES.append(text)


def section(title: str, width: int = 118) -> None:
    emit()
    emit("=" * width)
    emit(title)
    emit("=" * width)


def status(name: str, passed: bool) -> None:
    emit(f"{name:<84} {'PASS' if passed else 'FAIL'}")


# =============================================================================
# MAIN
# =============================================================================

def main() -> int:

    failures: list[str] = []

    section(
        "GEO-HUBBLE GEOMETRIC PROJECTION — "
        "RADIAL / PROJECTION INDEPENDENCE"
    )

    emit()
    emit("Question:")
    emit()
    emit("Does changing the radial effective state mu_eff alter")
    emit("the canonical external projection factor?")
    emit()
    emit("No Hubble measurement is used in this test.")

    # -------------------------------------------------------------------------
    # ANALYTIC REFERENCE
    # -------------------------------------------------------------------------

    section("ANALYTIC REFERENCE")

    emit(f"eta                               : {ETA:.15f}")
    emit(f"A                                 : {A:.15f}")
    emit(f"B                                 : {B:.15f}")
    emit(f"theta                             : {THETA:.15f}")
    emit(f"theta degrees                     : {math.degrees(THETA):.15f}")
    emit(f"f_c                               : {FC_ANALYTIC:.15f}")
    emit(f"A' analytic                       : {A_PRIME_ANALYTIC:.15f}")
    emit(f"P_geo analytic                    : {P_ANALYTIC:.15f}")
    emit(f"sqrt(6/5)                         : {P_CLOSED:.15f}")
    emit(
        f"|P_geo-sqrt(6/5)|               : "
        f"{abs(P_ANALYTIC-P_CLOSED):.15e}"
    )

    pass_closed = abs(P_ANALYTIC - P_CLOSED) < TOL

    status("Analytic closed form", pass_closed)

    if not pass_closed:
        failures.append("analytic closed form")

    # -------------------------------------------------------------------------
    # ENGINE SWEEP
    # -------------------------------------------------------------------------

    section("MU_EFF SWEEP")

    emit(
        f"{'mu_eff':>9} "
        f"{'R':>16} "
        f"{'Phi':>16} "
        f"{'alpha':>16} "
        f"{'A_prime':>16} "
        f"{'f_c':>16} "
        f"{'P_geo':>16}"
    )

    emit("-" * 112)

    rows = []

    for mu in MU_VALUES:

        g = compute(
            eta=ETA,
            L=L,
            mu_eff=mu,
        )

        eta_engine = float(g.eta)
        R = float(g.R)
        Phi = float(g.Phi)
        alpha = float(g.alpha)
        A_prime = float(g.projected_observable)

        fc = math.sqrt(eta_engine)
        P_geo = fc / A_prime

        radial_closure = abs(R ** 3 - mu)

        rows.append(
            {
                "mu": mu,
                "eta": eta_engine,
                "R": R,
                "Phi": Phi,
                "alpha": alpha,
                "A_prime": A_prime,
                "fc": fc,
                "P": P_geo,
                "radial_error": radial_closure,
            }
        )

        emit(
            f"{mu:9.4f} "
            f"{R:16.12f} "
            f"{Phi:16.12f} "
            f"{alpha:16.12f} "
            f"{A_prime:16.12f} "
            f"{fc:16.12f} "
            f"{P_geo:16.12f}"
        )

    # -------------------------------------------------------------------------
    # SPANS
    # -------------------------------------------------------------------------

    section("INVARIANCE SPANS")

    def span(key: str) -> float:
        values = [row[key] for row in rows]
        return max(values) - min(values)

    eta_span = span("eta")
    R_span = span("R")
    Phi_span = span("Phi")
    alpha_span = span("alpha")
    Aprime_span = span("A_prime")
    fc_span = span("fc")
    P_span = span("P")

    max_radial_error = max(
        row["radial_error"]
        for row in rows
    )

    emit(f"eta span                          : {eta_span:.15e}")
    emit(f"R span                            : {R_span:.15e}")
    emit(f"Phi span                          : {Phi_span:.15e}")
    emit(f"alpha span                        : {alpha_span:.15e}")
    emit(f"A' span                           : {Aprime_span:.15e}")
    emit(f"f_c span                          : {fc_span:.15e}")
    emit(f"P_geo span                        : {P_span:.15e}")
    emit(f"max |R^3-mu_eff|                  : {max_radial_error:.15e}")

    # -------------------------------------------------------------------------
    # EXPECTED VARIATION
    # -------------------------------------------------------------------------

    section("RADIAL-SECTOR RESPONSE")

    pass_R_changes = R_span > CHANGE_THRESHOLD
    pass_Phi_changes = Phi_span > CHANGE_THRESHOLD
    pass_alpha_changes = alpha_span > CHANGE_THRESHOLD

    status("R responds to mu_eff", pass_R_changes)
    status("Phi responds to mu_eff", pass_Phi_changes)
    status("alpha responds to mu_eff", pass_alpha_changes)

    if not pass_R_changes:
        failures.append("R did not respond to mu_eff")

    if not pass_Phi_changes:
        failures.append("Phi did not respond to mu_eff")

    if not pass_alpha_changes:
        failures.append("alpha did not respond to mu_eff")

    # -------------------------------------------------------------------------
    # EXPECTED INVARIANCE
    # -------------------------------------------------------------------------

    section("PROJECTION-SECTOR INVARIANCE")

    pass_eta = eta_span < TOL
    pass_Aprime = Aprime_span < TOL
    pass_fc = fc_span < TOL
    pass_P = P_span < TOL
    pass_radial = max_radial_error < TOL

    status("eta invariant", pass_eta)
    status("A' invariant", pass_Aprime)
    status("f_c invariant", pass_fc)
    status("P_geo invariant", pass_P)
    status("R^3 = mu_eff closure", pass_radial)

    if not pass_eta:
        failures.append("eta invariance")

    if not pass_Aprime:
        failures.append("A-prime invariance")

    if not pass_fc:
        failures.append("fc invariance")

    if not pass_P:
        failures.append("P_geo invariance")

    if not pass_radial:
        failures.append("radial closure")

    # -------------------------------------------------------------------------
    # ROW-BY-ROW CLOSED FORM
    # -------------------------------------------------------------------------

    section("ROW-BY-ROW CLOSED-FORM CHECK")

    max_Aprime_error = 0.0
    max_P_error = 0.0

    for row in rows:

        A_error = abs(
            row["A_prime"]
            - 1.0 / math.sqrt(2.0)
        )

        P_error = abs(
            row["P"]
            - math.sqrt(6.0 / 5.0)
        )

        max_Aprime_error = max(
            max_Aprime_error,
            A_error,
        )

        max_P_error = max(
            max_P_error,
            P_error,
        )

        emit(
            f"mu={row['mu']:0.4f}  "
            f"|A'-1/sqrt(2)|={A_error:.6e}  "
            f"|P-sqrt(6/5)|={P_error:.6e}"
        )

    emit()
    emit(
        f"max |A'-1/sqrt(2)|               : "
        f"{max_Aprime_error:.15e}"
    )

    emit(
        f"max |P-sqrt(6/5)|                : "
        f"{max_P_error:.15e}"
    )

    pass_row_closed = (
        max_Aprime_error < TOL
        and max_P_error < TOL
    )

    status(
        "Closed form survives entire radial sweep",
        pass_row_closed,
    )

    if not pass_row_closed:
        failures.append("closed form radial sweep")

    # -------------------------------------------------------------------------
    # CONTRAST FIRST/LAST
    # -------------------------------------------------------------------------

    section("EXTREME-STATE CONTRAST")

    first = rows[0]
    last = rows[-1]

    emit(f"mu_eff low                        : {first['mu']:.15f}")
    emit(f"mu_eff high                       : {last['mu']:.15f}")

    emit()

    emit(f"R low                             : {first['R']:.15f}")
    emit(f"R high                            : {last['R']:.15f}")
    emit(
        f"delta R                           : "
        f"{last['R']-first['R']:+.15e}"
    )

    emit()

    emit(f"Phi low                           : {first['Phi']:.15f}")
    emit(f"Phi high                          : {last['Phi']:.15f}")
    emit(
        f"delta Phi                         : "
        f"{last['Phi']-first['Phi']:+.15e}"
    )

    emit()

    emit(f"alpha low                         : {first['alpha']:.15f}")
    emit(f"alpha high                        : {last['alpha']:.15f}")
    emit(
        f"delta alpha                       : "
        f"{last['alpha']-first['alpha']:+.15e}"
    )

    emit()

    emit(f"P_geo low                         : {first['P']:.15f}")
    emit(f"P_geo high                        : {last['P']:.15f}")
    emit(
        f"delta P_geo                       : "
        f"{last['P']-first['P']:+.15e}"
    )

    # -------------------------------------------------------------------------
    # INTERPRETATION
    # -------------------------------------------------------------------------

    section("MATHEMATICAL INTERPRETATION")

    emit("The sweep separates two mathematical sectors:")
    emit()
    emit("RADIAL SECTOR")
    emit()
    emit("  mu_eff -> R = mu_eff^(1/3)")
    emit("         -> Phi")
    emit("         -> alpha")
    emit()
    emit("PROJECTION SECTOR")
    emit()
    emit("  eta -> A=eta")
    emit("      -> B=1-eta")
    emit("      -> f_c=sqrt(eta)")
    emit()
    emit("  (A,B,pi/4) -> A'=1/sqrt(2)")
    emit()
    emit("  P_geo = f_c/A'")
    emit("        = sqrt(6/5)")
    emit()
    emit("Therefore changing the radial effective state does not")
    emit("change the canonical projection factor under this architecture.")

    # -------------------------------------------------------------------------
    # FINAL
    # -------------------------------------------------------------------------

    section("FINAL INDEPENDENCE VERDICT")

    tests = {
        "Analytic closed form": pass_closed,
        "R responds to mu_eff": pass_R_changes,
        "Phi responds to mu_eff": pass_Phi_changes,
        "alpha responds to mu_eff": pass_alpha_changes,
        "eta invariant": pass_eta,
        "A' invariant": pass_Aprime,
        "f_c invariant": pass_fc,
        "P_geo invariant": pass_P,
        "Radial closure": pass_radial,
        "Closed form across sweep": pass_row_closed,
    }

    for name, passed in tests.items():
        status(name, passed)

    emit()

    if failures:

        emit("RESULT: FAIL")
        emit()

        for failure in failures:
            emit(f"  - {failure}")

        exit_code = 1

    else:

        emit("RESULT: PASS")
        emit()

        emit("The radial and projection sectors are numerically")
        emit("separable under the tested canonical GEO architecture.")
        emit()

        emit(
            f"R changes across the sweep by "
            f"{R_span:.15e}"
        )

        emit(
            f"Phi changes across the sweep by "
            f"{Phi_span:.15e}"
        )

        emit(
            f"alpha changes across the sweep by "
            f"{alpha_span:.15e}"
        )

        emit()

        emit(
            f"P_geo span = {P_span:.15e}"
        )

        emit()

        emit(
            "P_geo remains equal to sqrt(6/5) "
            "within numerical precision."
        )

        emit()
        emit("No Hubble measurement was used.")

        exit_code = 0

    OUTPUT_FILE.write_text(
        "\n".join(REPORT_LINES) + "\n",
        encoding="utf-8",
    )

    emit()
    emit("Saved report:")
    emit(str(OUTPUT_FILE))

    return exit_code


if __name__ == "__main__":
    sys.exit(main())
