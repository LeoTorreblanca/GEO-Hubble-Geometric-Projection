#!/usr/bin/env python3

"""
05_full_reproduction.py

GEO-Hubble Geometric Projection
Complete reproducibility runner.

Purpose
-------
Execute the full corrected GEO-Hubble validation chain:

    01_verify_geo_core.py
    02_verify_projection_matrix.py
    03_verify_radial_projection_independence.py
    04_hubble_projection_factor.py

The script does not replace the individual scientific tests.

Instead, it:

1. runs every required stage in order;
2. records stdout and stderr;
3. verifies process exit codes;
4. reconstructs the final canonical quantities independently;
5. confirms the final closed-form factor;
6. produces a single reproducibility verdict.

Scientific separation
---------------------
The sequence is intentionally ordered:

    core geometry
        ->
    canonical projection
        ->
    radial/projection independence
        ->
    Hubble application

The Hubble calculation is therefore downstream of the frozen geometry.

No local-H0 target is used to determine the GEO architecture.
"""

from __future__ import annotations

import argparse
import math
import platform
import subprocess
import sys
from datetime import datetime, timezone
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
SCRIPTS_DIR = PROJECT_ROOT / "scripts"
RESULTS_DIR = PROJECT_ROOT / "results"

RESULTS_DIR.mkdir(parents=True, exist_ok=True)

OUTPUT_FILE = RESULTS_DIR / "05_full_reproduction.txt"


# =============================================================================
# CANONICAL ARCHITECTURE
# =============================================================================

ETA = 3.0 / 5.0
L = 0.0
MU_REFERENCE = 0.8104

THETA = math.pi / 4.0

TOL = 1.0e-13
TOL_H = 1.0e-11


# =============================================================================
# REQUIRED SCRIPT CHAIN
# =============================================================================

REQUIRED_SCRIPTS = (
    "01_verify_geo_core.py",
    "02_verify_projection_matrix.py",
    "03_verify_radial_projection_independence.py",
    "04_hubble_projection_factor.py",
)


# =============================================================================
# REPORTING
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
    emit(f"{name:<86} {'PASS' if passed else 'FAIL'}")


# =============================================================================
# CLI
# =============================================================================

def parse_args():
    parser = argparse.ArgumentParser(
        description=(
            "Run the complete GEO-Hubble Geometric Projection "
            "reproducibility chain."
        )
    )

    parser.add_argument(
        "--h-base",
        type=float,
        default=67.4,
        help=(
            "External baseline Hubble value in km s^-1 Mpc^-1. "
            "Default: 67.4"
        ),
    )

    return parser.parse_args()


# =============================================================================
# SCRIPT EXECUTION
# =============================================================================

def run_script(script_name: str, h_base: float):
    """
    Execute one validation stage.

    The Hubble baseline is passed only to script 04.
    Earlier stages receive no Hubble argument.
    """

    script_path = SCRIPTS_DIR / script_name

    if not script_path.exists():
        return {
            "name": script_name,
            "exists": False,
            "returncode": None,
            "stdout": "",
            "stderr": f"Missing script: {script_path}",
        }

    command = [
        sys.executable,
        str(script_path),
    ]

    if script_name == "04_hubble_projection_factor.py":
        command.extend(
            [
                "--h-base",
                f"{h_base:.17g}",
            ]
        )

    process = subprocess.run(
        command,
        cwd=str(PROJECT_ROOT),
        text=True,
        capture_output=True,
        check=False,
    )

    return {
        "name": script_name,
        "exists": True,
        "returncode": process.returncode,
        "stdout": process.stdout,
        "stderr": process.stderr,
    }


# =============================================================================
# MAIN
# =============================================================================

def main() -> int:

    args = parse_args()

    H_base = float(args.h_base)

    failures: list[str] = []

    section(
        "GEO-HUBBLE GEOMETRIC PROJECTION — "
        "FULL REPRODUCTION"
    )

    emit()
    emit("Complete corrected derivation and executable audit.")
    emit()
    emit("Order:")
    emit()
    emit("  01  GEO core")
    emit("  02  canonical projection")
    emit("  03  radial / projection independence")
    emit("  04  Hubble application")
    emit()
    emit("The Hubble baseline is supplied only to stage 04.")

    # -------------------------------------------------------------------------
    # ENVIRONMENT
    # -------------------------------------------------------------------------

    section("ENVIRONMENT")

    now = datetime.now(timezone.utc)

    emit(f"UTC run time                        : {now.isoformat()}")
    emit(f"Python                              : {sys.version.split()[0]}")
    emit(f"Python executable                   : {sys.executable}")
    emit(f"Platform                            : {platform.platform()}")
    emit(f"Machine                             : {platform.machine()}")
    emit(f"External Operator API               : {api_version()}")
    emit(f"Project root                        : {PROJECT_ROOT}")

    # -------------------------------------------------------------------------
    # INPUT
    # -------------------------------------------------------------------------

    section("EXTERNAL APPLICATION INPUT")

    emit(
        f"H_base                              : "
        f"{H_base:.12f} km s^-1 Mpc^-1"
    )

    emit()
    emit("This input is not visible to stages 01, 02, or 03.")

    # -------------------------------------------------------------------------
    # RUN CHAIN
    # -------------------------------------------------------------------------

    section("EXECUTION CHAIN")

    execution_results = []

    for script_name in REQUIRED_SCRIPTS:

        emit()
        emit("-" * 118)
        emit(f"RUNNING: {script_name}")
        emit("-" * 118)

        result = run_script(
            script_name=script_name,
            h_base=H_base,
        )

        execution_results.append(result)

        if not result["exists"]:
            emit(result["stderr"])
            failures.append(f"{script_name}: missing")
            continue

        emit(
            f"return code                         : "
            f"{result['returncode']}"
        )

        stdout = result["stdout"].strip()

        if stdout:
            emit()
            emit("stdout:")
            emit()
            for line in stdout.splitlines():
                emit(f"  {line}")

        stderr = result["stderr"].strip()

        if stderr:
            emit()
            emit("stderr:")
            emit()
            for line in stderr.splitlines():
                emit(f"  {line}")

        passed = result["returncode"] == 0

        emit()

        status(script_name, passed)

        if not passed:
            failures.append(
                f"{script_name}: return code {result['returncode']}"
            )

    # -------------------------------------------------------------------------
    # SCRIPT SUMMARY
    # -------------------------------------------------------------------------

    section("SCRIPT-LEVEL SUMMARY")

    stage_pass = {}

    for result in execution_results:

        passed = (
            result["exists"]
            and result["returncode"] == 0
        )

        stage_pass[result["name"]] = passed

        status(
            result["name"],
            passed,
        )

    # -------------------------------------------------------------------------
    # INDEPENDENT FINAL RECONSTRUCTION
    # -------------------------------------------------------------------------

    section("INDEPENDENT FINAL RECONSTRUCTION")

    A = ETA
    B = 1.0 - ETA

    fc = math.sqrt(ETA)

    c = math.cos(THETA)
    s = math.sin(THETA)

    A_prime_analytic = (
        A * c
        + B * s
    )

    B_prime_analytic = (
        -A * s
        + B * c
    )

    P_analytic = (
        fc
        / A_prime_analytic
    )

    P_closed = math.sqrt(6.0 / 5.0)

    g = compute(
        eta=ETA,
        L=L,
        mu_eff=MU_REFERENCE,
    )

    A_prime_engine = float(
        g.projected_observable
    )

    B_prime_engine = float(
        g.projected_complementary
    )

    P_engine = (
        math.sqrt(float(g.eta))
        / A_prime_engine
    )

    H_engine = H_base * P_engine
    H_closed = H_base * P_closed

    emit(f"eta                                 : {ETA:.15f}")
    emit(f"A                                   : {A:.15f}")
    emit(f"B                                   : {B:.15f}")
    emit(f"A+B                                 : {A+B:.15f}")
    emit(f"theta                               : {THETA:.15f}")
    emit(f"theta [deg]                         : {math.degrees(THETA):.15f}")
    emit(f"f_c                                 : {fc:.15f}")

    emit()

    emit(
        f"A' analytic                         : "
        f"{A_prime_analytic:.15f}"
    )

    emit(
        f"A' engine                           : "
        f"{A_prime_engine:.15f}"
    )

    emit(
        f"B' analytic                         : "
        f"{B_prime_analytic:.15f}"
    )

    emit(
        f"B' engine                           : "
        f"{B_prime_engine:.15f}"
    )

    emit()

    emit(
        f"P_geo analytic                      : "
        f"{P_analytic:.15f}"
    )

    emit(
        f"P_geo engine                        : "
        f"{P_engine:.15f}"
    )

    emit(
        f"P_geo closed                        : "
        f"{P_closed:.15f}"
    )

    emit()

    emit(
        f"H_geo engine                        : "
        f"{H_engine:.12f}"
    )

    emit(
        f"H_geo closed                        : "
        f"{H_closed:.12f}"
    )

    # -------------------------------------------------------------------------
    # FINAL ERRORS
    # -------------------------------------------------------------------------

    section("FINAL NUMERICAL ERRORS")

    conservation_error = abs(
        (A + B) - 1.0
    )

    efficiency_error = abs(
        fc ** 2 - ETA
    )

    radial_error = abs(
        float(g.R) ** 3
        - MU_REFERENCE
    )

    A_error = abs(
        A_prime_engine
        - A_prime_analytic
    )

    B_error = abs(
        B_prime_engine
        - B_prime_analytic
    )

    P_analytic_error = abs(
        P_analytic
        - P_closed
    )

    P_engine_error = abs(
        P_engine
        - P_closed
    )

    H_error = abs(
        H_engine
        - H_closed
    )

    emit(
        f"|A+B-1|                            : "
        f"{conservation_error:.15e}"
    )

    emit(
        f"|f_c^2-eta|                        : "
        f"{efficiency_error:.15e}"
    )

    emit(
        f"|R^3-mu_eff|                       : "
        f"{radial_error:.15e}"
    )

    emit(
        f"|A'_engine-A'_analytic|            : "
        f"{A_error:.15e}"
    )

    emit(
        f"|B'_engine-B'_analytic|            : "
        f"{B_error:.15e}"
    )

    emit(
        f"|P_analytic-sqrt(6/5)|             : "
        f"{P_analytic_error:.15e}"
    )

    emit(
        f"|P_engine-sqrt(6/5)|               : "
        f"{P_engine_error:.15e}"
    )

    emit(
        f"|H_engine-H_closed|                : "
        f"{H_error:.15e}"
    )

    # -------------------------------------------------------------------------
    # FINAL NUMERICAL CHECKS
    # -------------------------------------------------------------------------

    section("FINAL MATHEMATICAL CHECKS")

    checks = {
        "Conservation A+B=1":
            conservation_error < TOL,

        "Quadratic efficiency f_c^2=eta":
            efficiency_error < TOL,

        "Correct radial law R^3=mu_eff":
            radial_error < TOL,

        "Analytic / engine A' agreement":
            A_error < TOL,

        "Analytic / engine B' agreement":
            B_error < TOL,

        "Analytic P_geo=sqrt(6/5)":
            P_analytic_error < TOL,

        "Engine P_geo=sqrt(6/5)":
            P_engine_error < TOL,

        "Hubble multiplication closure":
            H_error < TOL_H,
    }

    for name, passed in checks.items():
        status(name, passed)

        if not passed:
            failures.append(name)

    # -------------------------------------------------------------------------
    # SCIENTIFIC DEPENDENCY CHAIN
    # -------------------------------------------------------------------------

    section("FROZEN SCIENTIFIC DEPENDENCY CHAIN")

    emit("CANONICAL ARCHITECTURE")
    emit()
    emit("  A + B = 1")
    emit("  A = eta = 3/5")
    emit("  B = 2/5")
    emit("  eta = f_c^2")
    emit("  f_c = sqrt(3/5)")
    emit()

    emit("RADIAL BRANCH")
    emit()
    emit("  mu_eff -> R = mu_eff^(1/3)")
    emit()
    emit("  mu_eff is not universally identical to eta.")
    emit()

    emit("PROJECTION BRANCH")
    emit()
    emit("  theta = pi/4")
    emit("  v' = Q(theta) v")
    emit("  A' = (A+B)/sqrt(2)")
    emit("     = 1/sqrt(2)")
    emit()

    emit("CANONICAL DIMENSIONLESS FACTOR")
    emit()
    emit("  P_geo = f_c / A'")
    emit("        = sqrt(3/5) / (1/sqrt(2))")
    emit("        = sqrt(6/5)")
    emit()

    emit("PHYSICAL HUBBLE APPLICATION HYPOTHESIS")
    emit()
    emit("  H_projected / H_base = P_geo")
    emit()
    emit("therefore")
    emit()
    emit("  H_projected = H_base * sqrt(6/5)")

    # -------------------------------------------------------------------------
    # CLAIM BOUNDARY
    # -------------------------------------------------------------------------

    section("CLAIM BOUNDARY")

    emit("Established by the mathematical / executable audit:")
    emit()
    emit("  P_geo = sqrt(6/5)")
    emit()

    emit("Introduced separately as the physical hypothesis:")
    emit()
    emit("  H_projected / H_base = P_geo")
    emit()

    emit("Therefore the numerical Hubble value is conditional")
    emit("on that physical mapping.")
    emit()

    emit(
        "Internal numerical closure is not itself observational "
        "validation of cosmology."
    )

    # -------------------------------------------------------------------------
    # FINAL RESULT
    # -------------------------------------------------------------------------

    section("FINAL REPRODUCTION VERDICT")

    all_script_pass = all(
        stage_pass.get(name, False)
        for name in REQUIRED_SCRIPTS
    )

    all_math_pass = all(checks.values())

    status(
        "All required scripts",
        all_script_pass,
    )

    status(
        "All independent mathematical checks",
        all_math_pass,
    )

    emit()

    if failures or not all_script_pass or not all_math_pass:

        emit("OVERALL RESULT: FAIL")

        if failures:
            emit()
            emit("Failures:")

            for failure in failures:
                emit(f"  - {failure}")

        exit_code = 1

    else:

        emit("OVERALL RESULT: PASS")
        emit()

        emit("Canonical GEO projection factor:")
        emit()

        emit(
            f"  P_geo = {P_engine:.15f}"
        )

        emit()

        emit("Closed form:")
        emit()

        emit("  P_geo = sqrt(6/5)")
        emit()

        emit("External baseline:")
        emit()

        emit(
            f"  H_base = {H_base:.12f} "
            "km s^-1 Mpc^-1"
        )

        emit()

        emit("Conditional GEO-Hubble projection:")
        emit()

        emit(
            f"  H_geo = {H_engine:.12f} "
            "km s^-1 Mpc^-1"
        )

        emit()

        emit(
            "The corrected radial law and the canonical "
            "projection are numerically compatible."
        )

        emit(
            "No identity mu_eff = eta is required to obtain "
            "the canonical projection factor."
        )

        emit(
            "No local-H0 target is used in deriving P_geo."
        )

        exit_code = 0

    # -------------------------------------------------------------------------
    # SAVE
    # -------------------------------------------------------------------------

    OUTPUT_FILE.write_text(
        "\n".join(REPORT_LINES) + "\n",
        encoding="utf-8",
    )

    emit()
    emit("Saved full reproduction report:")
    emit(str(OUTPUT_FILE))

    return exit_code


if __name__ == "__main__":
    sys.exit(main())
