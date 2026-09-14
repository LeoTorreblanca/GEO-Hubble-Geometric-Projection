#!/usr/bin/env python3

"""
01_verify_geo_core.py

GEO-Hubble Geometric Projection
Core mathematical verification

Purpose
-------
Validate the corrected canonical GEO relations before any Hubble-specific
calculation is performed.

This script verifies:

1. Conservative partition:
       A + B = 1

2. Canonical efficiency law:
       eta = f_c^2

3. Correct radial law:
       R = mu_eff^(1/3)

4. Independence of eta and mu_eff:
       eta remains fixed while R changes with mu_eff

5. Numerical closure:
       R^3 = mu_eff

Important
---------
This script does NOT calculate a Hubble prediction.

It contains no local-H0 target and does not use the historical shorthand

    R = eta^(1/3)

as a general law.

The only valid radial relation used here is

    R = mu_eff^(1/3)
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
    print("Activate the External Operator environment first, for example:")
    print()
    print("  source ~/GEO-EXTERNAL-TEST/GEO-External-Operator/.venv/bin/activate")
    print()
    print(f"Original import error: {exc}")
    sys.exit(2)


# =============================================================================
# PATHS
# =============================================================================

SCRIPT_PATH = Path(__file__).resolve()
PROJECT_ROOT = SCRIPT_PATH.parent.parent
RESULTS_DIR = PROJECT_ROOT / "results"
RESULTS_DIR.mkdir(parents=True, exist_ok=True)

OUTPUT_FILE = RESULTS_DIR / "01_geo_core_check.txt"


# =============================================================================
# FROZEN CANONICAL ARCHITECTURE
# =============================================================================

ETA = 3.0 / 5.0
L = 0.0

MU_VALUES = (
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
# NUMERICAL TOLERANCES
# =============================================================================

TOL_CONSERVATION = 1.0e-14
TOL_EFFICIENCY = 1.0e-14
TOL_RADIAL = 1.0e-13


# =============================================================================
# OUTPUT HELPERS
# =============================================================================

REPORT_LINES: list[str] = []


def emit(text: str = "") -> None:
    """Print a line and store it in the reproducibility report."""

    print(text)
    REPORT_LINES.append(text)


def section(title: str, width: int = 110) -> None:
    """Print a formatted section header."""

    emit()
    emit("=" * width)
    emit(title)
    emit("=" * width)


def subsection(title: str, width: int = 110) -> None:
    """Print a formatted subsection header."""

    emit()
    emit(title)
    emit("-" * width)


def status_line(name: str, passed: bool) -> None:
    """Print a PASS/FAIL status line."""

    emit(f"{name:<72} {'PASS' if passed else 'FAIL'}")


# =============================================================================
# MATHEMATICAL HELPERS
# =============================================================================

def real_cuberoot(x: float) -> float:
    """
    Return the real cube root of x.

    Python's x ** (1/3) is adequate for the positive domain used here,
    but this implementation also behaves correctly for negative inputs.
    """

    if x >= 0.0:
        return x ** (1.0 / 3.0)

    return -((-x) ** (1.0 / 3.0))


# =============================================================================
# MAIN VALIDATION
# =============================================================================

def main() -> int:

    failures: list[str] = []

    section("GEO-HUBBLE GEOMETRIC PROJECTION — CORE GEO VERIFICATION")

    emit()
    emit("Purpose:")
    emit("  Verify the corrected canonical GEO architecture before any")
    emit("  Hubble-specific physical interpretation is introduced.")
    emit()
    emit("No local H0 target is used.")
    emit("No universal identity mu_eff = eta is assumed.")
    emit("The radial law tested is R = mu_eff^(1/3).")

    # -------------------------------------------------------------------------
    # SOFTWARE ENVIRONMENT
    # -------------------------------------------------------------------------

    section("SOFTWARE / API")

    try:
        api = api_version()
    except Exception as exc:
        emit(f"API version query failed: {exc}")
        failures.append("API version")
        api = None

    emit(f"geo_external_operator API version : {api}")
    emit(f"project root                      : {PROJECT_ROOT}")
    emit(f"output file                       : {OUTPUT_FILE}")

    # -------------------------------------------------------------------------
    # TEST 1 — CONSERVATIVE PARTITION
    # -------------------------------------------------------------------------

    section("TEST 1 — CONSERVATIVE PARTITION")

    A = ETA
    B = 1.0 - ETA

    conservation_sum = A + B
    conservation_error = abs(conservation_sum - 1.0)

    emit(f"eta = A                           : {A:.15f}")
    emit(f"B = 1 - eta                       : {B:.15f}")
    emit(f"A + B                             : {conservation_sum:.15f}")
    emit(f"|A + B - 1|                       : {conservation_error:.15e}")
    emit(f"tolerance                         : {TOL_CONSERVATION:.1e}")

    pass_conservation = conservation_error < TOL_CONSERVATION

    status_line("Conservative partition", pass_conservation)

    if not pass_conservation:
        failures.append("Conservative partition")

    # -------------------------------------------------------------------------
    # TEST 2 — QUADRATIC EFFICIENCY LAW
    # -------------------------------------------------------------------------

    section("TEST 2 — QUADRATIC EFFICIENCY LAW")

    fc = math.sqrt(ETA)
    reconstructed_eta = fc * fc
    efficiency_error = abs(reconstructed_eta - ETA)

    emit(f"eta                               : {ETA:.15f}")
    emit(f"f_c = sqrt(eta)                   : {fc:.15f}")
    emit(f"f_c^2                             : {reconstructed_eta:.15f}")
    emit(f"|f_c^2 - eta|                     : {efficiency_error:.15e}")
    emit(f"tolerance                         : {TOL_EFFICIENCY:.1e}")

    pass_efficiency = efficiency_error < TOL_EFFICIENCY

    status_line("Quadratic efficiency law", pass_efficiency)

    if not pass_efficiency:
        failures.append("Quadratic efficiency law")

    # -------------------------------------------------------------------------
    # TEST 3 — RADIAL LAW SWEEP
    # -------------------------------------------------------------------------

    section("TEST 3 — CORRECT RADIAL LAW")

    emit(
        f"{'mu_eff':>12} "
        f"{'R engine':>18} "
        f"{'R analytic':>18} "
        f"{'|difference|':>18} "
        f"{'|R^3-mu|':>18}"
    )

    emit("-" * 92)

    radial_rows = []

    for mu_eff in MU_VALUES:

        g = compute(
            eta=ETA,
            L=L,
            mu_eff=mu_eff,
        )

        R_engine = float(g.R)
        R_analytic = real_cuberoot(mu_eff)

        direct_error = abs(R_engine - R_analytic)
        closure_error = abs((R_engine ** 3) - mu_eff)

        radial_rows.append(
            {
                "mu_eff": mu_eff,
                "R_engine": R_engine,
                "R_analytic": R_analytic,
                "direct_error": direct_error,
                "closure_error": closure_error,
                "eta_returned": float(g.eta),
            }
        )

        emit(
            f"{mu_eff:12.6f} "
            f"{R_engine:18.15f} "
            f"{R_analytic:18.15f} "
            f"{direct_error:18.6e} "
            f"{closure_error:18.6e}"
        )

    max_direct_error = max(row["direct_error"] for row in radial_rows)
    max_closure_error = max(row["closure_error"] for row in radial_rows)

    emit()
    emit(f"max |R_engine - R_analytic|       : {max_direct_error:.15e}")
    emit(f"max |R^3 - mu_eff|                : {max_closure_error:.15e}")
    emit(f"tolerance                         : {TOL_RADIAL:.1e}")

    pass_radial = (
        max_direct_error < TOL_RADIAL
        and max_closure_error < TOL_RADIAL
    )

    status_line("Canonical radial law", pass_radial)

    if not pass_radial:
        failures.append("Canonical radial law")

    # -------------------------------------------------------------------------
    # TEST 4 — ETA MUST REMAIN FIXED DURING MU SWEEP
    # -------------------------------------------------------------------------

    section("TEST 4 — ETA / MU_EFF INDEPENDENCE")

    eta_values = [row["eta_returned"] for row in radial_rows]

    eta_span = max(eta_values) - min(eta_values)

    emit(f"eta requested                      : {ETA:.15f}")
    emit(f"eta returned min                  : {min(eta_values):.15f}")
    emit(f"eta returned max                  : {max(eta_values):.15f}")
    emit(f"eta span                          : {eta_span:.15e}")

    # Compare specifically the two states already used during the manual audit.

    state_mu_060 = next(
        row for row in radial_rows
        if math.isclose(row["mu_eff"], 0.60, rel_tol=0.0, abs_tol=1e-15)
    )

    state_mu_08104 = next(
        row for row in radial_rows
        if math.isclose(row["mu_eff"], 0.8104, rel_tol=0.0, abs_tol=1e-15)
    )

    delta_R = (
        state_mu_08104["R_engine"]
        - state_mu_060["R_engine"]
    )

    emit()
    emit("Explicit comparison")
    emit("-" * 110)

    emit(
        f"mu_eff 1                          : "
        f"{state_mu_060['mu_eff']:.15f}"
    )

    emit(
        f"R 1                               : "
        f"{state_mu_060['R_engine']:.15f}"
    )

    emit(
        f"mu_eff 2                          : "
        f"{state_mu_08104['mu_eff']:.15f}"
    )

    emit(
        f"R 2                               : "
        f"{state_mu_08104['R_engine']:.15f}"
    )

    emit(f"delta R                           : {delta_R:+.15e}")

    pass_eta_fixed = eta_span < TOL_CONSERVATION
    pass_R_changes = abs(delta_R) > 1.0e-6

    status_line("eta remains fixed while mu_eff changes", pass_eta_fixed)
    status_line("R changes when mu_eff changes", pass_R_changes)

    if not pass_eta_fixed:
        failures.append("eta stability")

    if not pass_R_changes:
        failures.append("mu_eff / eta independence")

    # -------------------------------------------------------------------------
    # TEST 5 — HISTORICAL SHORTCUT MUST NOT BE UNIVERSAL
    # -------------------------------------------------------------------------

    section("TEST 5 — HISTORICAL RADIAL SHORTCUT AUDIT")

    historical_R = real_cuberoot(ETA)

    emit(f"eta                               : {ETA:.15f}")
    emit(f"eta^(1/3)                         : {historical_R:.15f}")
    emit()
    emit("Compare eta^(1/3) against engine R for multiple mu_eff:")
    emit()

    mismatch_count = 0

    for row in radial_rows:

        mu_eff = row["mu_eff"]
        R_engine = row["R_engine"]
        difference = abs(R_engine - historical_R)

        if not math.isclose(
            mu_eff,
            ETA,
            rel_tol=0.0,
            abs_tol=1.0e-15,
        ):
            if difference > 1.0e-8:
                mismatch_count += 1

        emit(
            f"mu_eff={mu_eff:0.6f}  "
            f"R_engine={R_engine:.15f}  "
            f"|R_engine-eta^(1/3)|={difference:.6e}"
        )

    expected_mismatches = sum(
        1
        for mu in MU_VALUES
        if not math.isclose(
            mu,
            ETA,
            rel_tol=0.0,
            abs_tol=1.0e-15,
        )
    )

    emit()
    emit(f"non-eta states tested             : {expected_mismatches}")
    emit(f"states inconsistent with R=eta^1/3: {mismatch_count}")

    pass_historical_shortcut = (
        mismatch_count == expected_mismatches
    )

    status_line(
        "Historical R=eta^(1/3) is not a universal radial law",
        pass_historical_shortcut,
    )

    if not pass_historical_shortcut:
        failures.append("historical radial shortcut audit")

    # -------------------------------------------------------------------------
    # TEST 6 — REFERENCE VALUES
    # -------------------------------------------------------------------------

    section("TEST 6 — REFERENCE CANONICAL VALUES")

    expected_fc = math.sqrt(3.0 / 5.0)

    emit(f"eta                               : {ETA:.15f}")
    emit(f"B                                 : {B:.15f}")
    emit(f"f_c                               : {fc:.15f}")
    emit(f"expected f_c                      : {expected_fc:.15f}")
    emit(f"|difference|                      : {abs(fc-expected_fc):.15e}")

    pass_reference = abs(fc - expected_fc) < TOL_EFFICIENCY

    status_line("Canonical numerical reference", pass_reference)

    if not pass_reference:
        failures.append("canonical numerical reference")

    # -------------------------------------------------------------------------
    # FINAL STATUS
    # -------------------------------------------------------------------------

    section("FINAL CORE VERDICT")

    required_tests = {
        "Conservative partition": pass_conservation,
        "Quadratic efficiency": pass_efficiency,
        "Radial law": pass_radial,
        "eta fixed": pass_eta_fixed,
        "R responds to mu_eff": pass_R_changes,
        "Historical shortcut rejected": pass_historical_shortcut,
        "Reference values": pass_reference,
    }

    for name, passed in required_tests.items():
        status_line(name, passed)

    emit()

    if failures:
        emit("RESULT: FAIL")
        emit()
        emit("Failed checks:")
        for failure in failures:
            emit(f"  - {failure}")

        exit_code = 1

    else:
        emit("RESULT: PASS")
        emit()
        emit("The corrected GEO core relations are internally consistent:")
        emit()
        emit("  A + B = 1")
        emit("  eta = f_c^2")
        emit("  f_c = sqrt(eta)")
        emit("  R = mu_eff^(1/3)")
        emit()
        emit("eta and mu_eff remain distinct quantities.")
        emit()
        emit("No Hubble-scale prediction has been used or tested by this script.")

        exit_code = 0

    # -------------------------------------------------------------------------
    # WRITE REPORT
    # -------------------------------------------------------------------------

    OUTPUT_FILE.write_text(
        "\n".join(REPORT_LINES) + "\n",
        encoding="utf-8",
    )

    emit()
    emit(f"Saved report:")
    emit(str(OUTPUT_FILE))

    return exit_code


if __name__ == "__main__":
    sys.exit(main())
