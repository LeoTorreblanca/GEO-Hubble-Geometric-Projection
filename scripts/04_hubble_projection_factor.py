#!/usr/bin/env python3

"""
04_hubble_projection_factor.py

GEO-Hubble Geometric Projection
Application of the frozen canonical GEO projection factor
to an external baseline Hubble scale.

Purpose
-------
This script performs the first Hubble-specific calculation
in the repository.

It does NOT derive the GEO geometry.

The geometry has already been independently validated by:

    01_verify_geo_core.py
    02_verify_projection_matrix.py
    03_verify_radial_projection_independence.py

This script only:

1. reconstructs the canonical GEO projection factor
   from the same frozen architecture;

2. accepts an external H_base;

3. calculates

       H_geo = P_geo * H_base

4. compares the numerical result with the closed analytic form

       H_geo = H_base * sqrt(6/5).

No local-H0 target is used to determine any GEO quantity.
"""

from __future__ import annotations

import argparse
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

OUTPUT_FILE = RESULTS_DIR / "04_hubble_projection.txt"


# =============================================================================
# CANONICAL GEO ARCHITECTURE
# =============================================================================

ETA = 3.0 / 5.0
L = 0.0

A = ETA
B = 1.0 - ETA

THETA = math.pi / 4.0

# mu_eff is required only by the public External Operator API.
#
# The Hubble projection factor derived below must remain independent
# of this value. This representative value is not fitted to Hubble.
MU_EFF_REFERENCE = 0.8104


# =============================================================================
# TOLERANCES
# =============================================================================

TOL_FACTOR = 1.0e-13
TOL_HUBBLE = 1.0e-11


# =============================================================================
# REPORT
# =============================================================================

REPORT_LINES: list[str] = []


def emit(text: str = "") -> None:
    print(text)
    REPORT_LINES.append(text)


def section(title: str, width: int = 112) -> None:
    emit()
    emit("=" * width)
    emit(title)
    emit("=" * width)


def status(name: str, passed: bool) -> None:
    emit(f"{name:<82} {'PASS' if passed else 'FAIL'}")


# =============================================================================
# ARGUMENTS
# =============================================================================

def parse_args():
    parser = argparse.ArgumentParser(
        description=(
            "Apply the frozen canonical GEO projection factor "
            "to an external baseline Hubble scale."
        )
    )

    parser.add_argument(
        "--h-base",
        type=float,
        default=67.4,
        help=(
            "Baseline Hubble scale in km s^-1 Mpc^-1. "
            "Default: 67.4"
        ),
    )

    return parser.parse_args()


# =============================================================================
# MAIN
# =============================================================================

def main() -> int:

    args = parse_args()

    H_base = float(args.h_base)

    failures: list[str] = []

    section(
        "GEO-HUBBLE GEOMETRIC PROJECTION — "
        "HUBBLE APPLICATION TEST"
    )

    emit()
    emit("This is the first Hubble-specific script in the chain.")
    emit()
    emit("The GEO geometry is frozen before H_base is introduced.")
    emit()
    emit("No local-H0 target is used to derive eta, theta,")
    emit("f_c, A', or P_geo.")

    # -------------------------------------------------------------------------
    # INPUT
    # -------------------------------------------------------------------------

    section("EXTERNAL HUBBLE INPUT")

    emit(
        f"H_base                             : "
        f"{H_base:.12f} km s^-1 Mpc^-1"
    )

    emit()
    emit("H_base is treated as an externally supplied baseline.")
    emit("It is not derived by GEO.")

    # -------------------------------------------------------------------------
    # RECONSTRUCT GEO FACTOR
    # -------------------------------------------------------------------------

    section("RECONSTRUCT FROZEN GEO PROJECTION FACTOR")

    g = compute(
        eta=ETA,
        L=L,
        mu_eff=MU_EFF_REFERENCE,
    )

    eta_engine = float(g.eta)

    fc = math.sqrt(eta_engine)

    A_prime_engine = float(g.projected_observable)

    P_engine = fc / A_prime_engine

    P_closed = math.sqrt(6.0 / 5.0)

    factor_error = abs(P_engine - P_closed)

    emit(f"API version                         : {api_version()}")
    emit(f"eta                                 : {eta_engine:.15f}")
    emit(f"mu_eff reference                    : {MU_EFF_REFERENCE:.15f}")
    emit(f"R reference                         : {float(g.R):.15f}")
    emit(f"f_c = sqrt(eta)                     : {fc:.15f}")
    emit(f"A' engine                           : {A_prime_engine:.15f}")
    emit(f"P_geo engine                        : {P_engine:.15f}")
    emit(f"P_geo closed = sqrt(6/5)            : {P_closed:.15f}")
    emit(f"|difference|                        : {factor_error:.15e}")

    pass_factor = factor_error < TOL_FACTOR

    status(
        "Frozen GEO projection-factor closure",
        pass_factor,
    )

    if not pass_factor:
        failures.append("projection factor closure")

    # -------------------------------------------------------------------------
    # HUBBLE CALCULATION
    # -------------------------------------------------------------------------

    section("HUBBLE PROJECTION")

    H_geo_engine = H_base * P_engine

    H_geo_closed = H_base * P_closed

    H_error = abs(H_geo_engine - H_geo_closed)

    delta_H = H_geo_engine - H_base

    fractional_shift = (
        H_geo_engine - H_base
    ) / H_base

    percent_shift = 100.0 * fractional_shift

    emit(
        f"H_base                              : "
        f"{H_base:.12f}"
    )

    emit(
        f"P_geo                               : "
        f"{P_engine:.15f}"
    )

    emit()

    emit(
        f"H_geo = H_base * P_geo              : "
        f"{H_geo_engine:.12f}"
    )

    emit(
        f"H_geo analytic                      : "
        f"{H_geo_closed:.12f}"
    )

    emit(
        f"|engine - analytic|                 : "
        f"{H_error:.15e}"
    )

    emit()

    emit(
        f"absolute shift                      : "
        f"{delta_H:+.12f}"
    )

    emit(
        f"fractional shift                    : "
        f"{fractional_shift:+.15f}"
    )

    emit(
        f"percentage shift                    : "
        f"{percent_shift:+.9f}%"
    )

    pass_hubble = H_error < TOL_HUBBLE

    status(
        "Hubble multiplication closure",
        pass_hubble,
    )

    if not pass_hubble:
        failures.append("Hubble multiplication closure")

    # -------------------------------------------------------------------------
    # DIMENSIONAL CHECK
    # -------------------------------------------------------------------------

    section("DIMENSIONAL CHECK")

    emit("P_geo is dimensionless.")
    emit()
    emit("Therefore:")
    emit()
    emit("  [H_geo] = [P_geo] [H_base]")
    emit("          = 1 * [H_base]")
    emit("          = km s^-1 Mpc^-1")
    emit()
    emit("The transformation preserves Hubble units.")

    # -------------------------------------------------------------------------
    # CLOSED FORM
    # -------------------------------------------------------------------------

    section("CLOSED-FORM RESULT")

    emit("P_geo = sqrt(6/5)")
    emit()
    emit("Therefore:")
    emit()
    emit("  H_geo = H_base * sqrt(6/5)")
    emit()

    emit(
        f"For H_base = {H_base:.12f}:"
    )

    emit()

    emit(
        f"  H_geo = {H_geo_closed:.12f} "
        "km s^-1 Mpc^-1"
    )

    # -------------------------------------------------------------------------
    # NO-TARGET AUDIT
    # -------------------------------------------------------------------------

    section("NO-TARGET AUDIT")

    emit("Quantities fixed before H_base:")
    emit()
    emit("  eta = 3/5")
    emit("  A = eta")
    emit("  B = 1-eta")
    emit("  theta = pi/4")
    emit("  f_c = sqrt(eta)")
    emit("  A' = 1/sqrt(2)")
    emit("  P_geo = sqrt(6/5)")
    emit()
    emit("No value of H_local was used.")
    emit()
    emit("No Hubble value was used to solve for:")
    emit()
    emit("  eta")
    emit("  theta")
    emit("  f_c")
    emit("  mu_eff")
    emit("  R")
    emit("  Phi")
    emit("  alpha")

    # -------------------------------------------------------------------------
    # PHYSICAL CLAIM BOUNDARY
    # -------------------------------------------------------------------------

    section("PHYSICAL CLAIM BOUNDARY")

    emit("MATHEMATICAL RESULT")
    emit()
    emit("  P_geo = sqrt(6/5)")
    emit()

    emit("APPLICATION HYPOTHESIS")
    emit()
    emit("  H_projected / H_base = P_geo")
    emit()

    emit("NUMERICAL CONSEQUENCE")
    emit()

    emit(
        f"  H_projected = {H_geo_engine:.12f} "
        "km s^-1 Mpc^-1"
    )

    emit()
    emit(
        "The software calculation validates the internal "
        "projection arithmetic."
    )

    emit(
        "It does not by itself prove that the physical Universe "
        "must realize this Hubble mapping."
    )

    # -------------------------------------------------------------------------
    # FINAL VERDICT
    # -------------------------------------------------------------------------

    section("FINAL HUBBLE-APPLICATION VERDICT")

    status(
        "Projection factor derived before Hubble input",
        pass_factor,
    )

    status(
        "Hubble calculation matches closed form",
        pass_hubble,
    )

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

        emit("Frozen geometric factor:")
        emit()

        emit(
            f"  P_geo = {P_engine:.15f}"
        )

        emit()

        emit("Reference projection:")
        emit()

        emit(
            f"  {H_base:.12f} "
            "km s^-1 Mpc^-1"
        )

        emit("        ->")

        emit(
            f"  {H_geo_engine:.12f} "
            "km s^-1 Mpc^-1"
        )

        emit()

        emit(
            "This numerical output follows from the declared "
            "GEO-Hubble application hypothesis."
        )

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
