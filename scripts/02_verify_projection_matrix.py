#!/usr/bin/env python3

"""
02_verify_projection_matrix.py

GEO-Hubble Geometric Projection
Canonical tangent-projection verification.

Purpose
-------
Starting only from the canonical conservative GEO state,

    A = eta
    B = 1 - eta
    A + B = 1

and the canonical tangent angle

    theta = pi/4,

this script independently reconstructs the projection

    v' = Q(theta) v

with

             [ cos(theta)   sin(theta) ]
    Q(theta)=[                         ]
             [-sin(theta)   cos(theta) ]

It then compares the analytic projection against the public
GEO External Operator.

Only after projection closure is established does the script
construct

    f_c = sqrt(eta)

and the dimensionless geometric ratio

    P_geo = f_c / A'.

No Hubble value, local-H0 measurement, or fitted cosmological
target is used anywhere in this script.
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
    print("Activate the External Operator environment first:")
    print()
    print(
        "  source "
        "~/GEO-EXTERNAL-TEST/GEO-External-Operator/.venv/bin/activate"
    )
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

OUTPUT_FILE = RESULTS_DIR / "02_projection_check.txt"


# =============================================================================
# CANONICAL GEO STATE
# =============================================================================

ETA = 3.0 / 5.0
A = ETA
B = 1.0 - ETA

L = 0.0

THETA = math.pi / 4.0

# mu_eff is deliberately NOT used to derive the projection.
#
# We provide one admissible value only because the public compute()
# interface requires an effective-state input.
#
# A later script will sweep mu_eff independently.
MU_EFF = 0.8104


# =============================================================================
# NUMERICAL TOLERANCES
# =============================================================================

TOL_MATRIX = 1.0e-14
TOL_PROJECTION = 1.0e-14
TOL_RECONSTRUCTION = 1.0e-14
TOL_FACTOR = 1.0e-14


# =============================================================================
# REPORT
# =============================================================================

REPORT_LINES: list[str] = []


def emit(text: str = "") -> None:
    print(text)
    REPORT_LINES.append(text)


def section(title: str, width: int = 110) -> None:
    emit()
    emit("=" * width)
    emit(title)
    emit("=" * width)


def status_line(name: str, passed: bool) -> None:
    emit(f"{name:<76} {'PASS' if passed else 'FAIL'}")


# =============================================================================
# SMALL 2x2 MATRIX HELPERS
# =============================================================================

def matmul_2x2(A_, B_):
    return (
        (
            A_[0][0] * B_[0][0] + A_[0][1] * B_[1][0],
            A_[0][0] * B_[0][1] + A_[0][1] * B_[1][1],
        ),
        (
            A_[1][0] * B_[0][0] + A_[1][1] * B_[1][0],
            A_[1][0] * B_[0][1] + A_[1][1] * B_[1][1],
        ),
    )


def transpose_2x2(M):
    return (
        (M[0][0], M[1][0]),
        (M[0][1], M[1][1]),
    )


def matvec_2x2(M, v):
    return (
        M[0][0] * v[0] + M[0][1] * v[1],
        M[1][0] * v[0] + M[1][1] * v[1],
    )


def matrix_max_error(M, N):
    return max(
        abs(M[i][j] - N[i][j])
        for i in range(2)
        for j in range(2)
    )


# =============================================================================
# MAIN
# =============================================================================

def main() -> int:

    failures: list[str] = []

    section(
        "GEO-HUBBLE GEOMETRIC PROJECTION — "
        "CANONICAL PROJECTION VERIFICATION"
    )

    emit()
    emit("This test contains no Hubble measurement.")
    emit("It tests only the canonical GEO projection geometry.")
    emit()
    emit("Dependency chain:")
    emit()
    emit("  eta -> (A,B)")
    emit("  eta -> f_c")
    emit("  (A,B,theta) -> (A',B')")
    emit("  (f_c,A') -> P_geo")
    emit()
    emit("mu_eff is NOT used to derive A', B', f_c, or P_geo.")

    # -------------------------------------------------------------------------
    # API
    # -------------------------------------------------------------------------

    section("SOFTWARE / API")

    api = api_version()

    emit(f"geo_external_operator API version : {api}")
    emit(f"project root                      : {PROJECT_ROOT}")
    emit(f"output file                       : {OUTPUT_FILE}")

    # -------------------------------------------------------------------------
    # CANONICAL STATE
    # -------------------------------------------------------------------------

    section("TEST 1 — CANONICAL CONSERVATIVE STATE")

    conservation = A + B
    conservation_error = abs(conservation - 1.0)

    emit(f"eta                               : {ETA:.15f}")
    emit(f"A                                 : {A:.15f}")
    emit(f"B                                 : {B:.15f}")
    emit(f"A + B                             : {conservation:.15f}")
    emit(f"|A+B-1|                           : {conservation_error:.15e}")

    pass_state = conservation_error < TOL_MATRIX

    status_line("Canonical conservative state", pass_state)

    if not pass_state:
        failures.append("canonical conservative state")

    # -------------------------------------------------------------------------
    # BUILD Q
    # -------------------------------------------------------------------------

    section("TEST 2 — CANONICAL TANGENT MATRIX")

    c = math.cos(THETA)
    s = math.sin(THETA)

    Q = (
        (c, s),
        (-s, c),
    )

    QT = transpose_2x2(Q)

    identity_calc = matmul_2x2(QT, Q)

    identity_expected = (
        (1.0, 0.0),
        (0.0, 1.0),
    )

    orthogonality_error = matrix_max_error(
        identity_calc,
        identity_expected,
    )

    determinant = (
        Q[0][0] * Q[1][1]
        - Q[0][1] * Q[1][0]
    )

    determinant_error = abs(determinant - 1.0)

    emit(f"theta                             : {THETA:.15f}")
    emit(f"theta degrees                     : {math.degrees(THETA):.15f}")
    emit(f"cos(theta)                        : {c:.15f}")
    emit(f"sin(theta)                        : {s:.15f}")

    emit()
    emit("Q(theta)")
    emit()
    emit(f"  [{Q[0][0]: .15f}  {Q[0][1]: .15f}]")
    emit(f"  [{Q[1][0]: .15f}  {Q[1][1]: .15f}]")

    emit()
    emit("Q^T Q")
    emit()
    emit(
        f"  [{identity_calc[0][0]: .15f}  "
        f"{identity_calc[0][1]: .15f}]"
    )
    emit(
        f"  [{identity_calc[1][0]: .15f}  "
        f"{identity_calc[1][1]: .15f}]"
    )

    emit()
    emit(f"max |Q^T Q - I|                   : {orthogonality_error:.15e}")
    emit(f"det(Q)                            : {determinant:.15f}")
    emit(f"|det(Q)-1|                        : {determinant_error:.15e}")

    pass_orthogonality = (
        orthogonality_error < TOL_MATRIX
        and determinant_error < TOL_MATRIX
    )

    status_line("Orthogonal tangent operator", pass_orthogonality)

    if not pass_orthogonality:
        failures.append("orthogonal tangent operator")

    # -------------------------------------------------------------------------
    # ANALYTIC PROJECTION
    # -------------------------------------------------------------------------

    section("TEST 3 — ANALYTIC PROJECTION")

    v = (A, B)

    A_prime_manual, B_prime_manual = matvec_2x2(Q, v)

    A_prime_closed = (A + B) / math.sqrt(2.0)
    B_prime_closed = (B - A) / math.sqrt(2.0)

    expected_A_prime = 1.0 / math.sqrt(2.0)
    expected_B_prime = -1.0 / (5.0 * math.sqrt(2.0))

    emit(f"A' matrix                         : {A_prime_manual:.15f}")
    emit(f"A' closed                         : {A_prime_closed:.15f}")
    emit(f"1/sqrt(2)                         : {expected_A_prime:.15f}")

    emit()

    emit(f"B' matrix                         : {B_prime_manual:.15f}")
    emit(f"B' closed                         : {B_prime_closed:.15f}")
    emit(f"-1/(5 sqrt(2))                    : {expected_B_prime:.15f}")

    A_closed_error = abs(
        A_prime_manual - expected_A_prime
    )

    B_closed_error = abs(
        B_prime_manual - expected_B_prime
    )

    emit()
    emit(f"|A' - 1/sqrt(2)|                  : {A_closed_error:.15e}")
    emit(f"|B' + 1/(5sqrt(2))|               : {B_closed_error:.15e}")

    pass_analytic_projection = (
        A_closed_error < TOL_PROJECTION
        and B_closed_error < TOL_PROJECTION
    )

    status_line(
        "Closed-form canonical projection",
        pass_analytic_projection,
    )

    if not pass_analytic_projection:
        failures.append("closed-form canonical projection")

    # -------------------------------------------------------------------------
    # NORM PRESERVATION
    # -------------------------------------------------------------------------

    section("TEST 4 — ANALYTIC NORM PRESERVATION")

    norm_before_sq = A * A + B * B

    norm_after_sq = (
        A_prime_manual * A_prime_manual
        + B_prime_manual * B_prime_manual
    )

    norm_error = abs(norm_before_sq - norm_after_sq)

    emit(f"||v||^2                           : {norm_before_sq:.15f}")
    emit(f"||Qv||^2                          : {norm_after_sq:.15f}")
    emit(f"|difference|                      : {norm_error:.15e}")

    pass_norm = norm_error < TOL_PROJECTION

    status_line("Analytic projection norm", pass_norm)

    if not pass_norm:
        failures.append("analytic projection norm")

    # -------------------------------------------------------------------------
    # EXTERNAL OPERATOR
    # -------------------------------------------------------------------------

    section("TEST 5 — EXTERNAL OPERATOR PROJECTION")

    g = compute(
        eta=ETA,
        L=L,
        mu_eff=MU_EFF,
    )

    A_prime_engine = float(g.projected_observable)
    B_prime_engine = float(g.projected_complementary)

    engine_A_error = abs(
        A_prime_engine - A_prime_manual
    )

    engine_B_error = abs(
        B_prime_engine - B_prime_manual
    )

    emit(f"mu_eff supplied to engine         : {MU_EFF:.15f}")
    emit(f"R returned by engine              : {float(g.R):.15f}")

    emit()

    emit(f"A' analytic                       : {A_prime_manual:.15f}")
    emit(f"A' engine                         : {A_prime_engine:.15f}")
    emit(f"|difference|                      : {engine_A_error:.15e}")

    emit()

    emit(f"B' analytic                       : {B_prime_manual:.15f}")
    emit(f"B' engine                         : {B_prime_engine:.15f}")
    emit(f"|difference|                      : {engine_B_error:.15e}")

    pass_engine_projection = (
        engine_A_error < TOL_PROJECTION
        and engine_B_error < TOL_PROJECTION
    )

    status_line(
        "Analytic / engine projection closure",
        pass_engine_projection,
    )

    if not pass_engine_projection:
        failures.append("analytic / engine projection closure")

    # -------------------------------------------------------------------------
    # ENGINE NORM
    # -------------------------------------------------------------------------

    section("TEST 6 — ENGINE NORM CLOSURE")

    engine_norm_error = abs(
        float(g.projection_norm_error)
    )

    emit(
        f"engine projection_norm_error      : "
        f"{engine_norm_error:.15e}"
    )

    emit(
        f"independent analytic norm error   : "
        f"{norm_error:.15e}"
    )

    pass_engine_norm = (
        engine_norm_error < TOL_PROJECTION
    )

    status_line("Engine projection norm closure", pass_engine_norm)

    if not pass_engine_norm:
        failures.append("engine projection norm closure")

    # -------------------------------------------------------------------------
    # RECONSTRUCTION
    # -------------------------------------------------------------------------

    section("TEST 7 — INVERSE RECONSTRUCTION")

    reconstructed_manual = matvec_2x2(
        QT,
        (A_prime_manual, B_prime_manual),
    )

    A_rec_manual = reconstructed_manual[0]
    B_rec_manual = reconstructed_manual[1]

    A_rec_engine = float(g.reconstructed_observable)
    B_rec_engine = float(g.reconstructed_complementary)

    manual_A_rec_error = abs(A_rec_manual - A)
    manual_B_rec_error = abs(B_rec_manual - B)

    engine_A_rec_error = abs(A_rec_engine - A)
    engine_B_rec_error = abs(B_rec_engine - B)

    emit(f"A original                        : {A:.15f}")
    emit(f"A reconstructed analytic          : {A_rec_manual:.15f}")
    emit(f"A reconstructed engine            : {A_rec_engine:.15f}")

    emit()

    emit(f"B original                        : {B:.15f}")
    emit(f"B reconstructed analytic          : {B_rec_manual:.15f}")
    emit(f"B reconstructed engine            : {B_rec_engine:.15f}")

    emit()

    emit(
        f"analytic A reconstruction error   : "
        f"{manual_A_rec_error:.15e}"
    )

    emit(
        f"analytic B reconstruction error   : "
        f"{manual_B_rec_error:.15e}"
    )

    emit(
        f"engine A reconstruction error     : "
        f"{engine_A_rec_error:.15e}"
    )

    emit(
        f"engine B reconstruction error     : "
        f"{engine_B_rec_error:.15e}"
    )

    pass_reconstruction = all(
        error < TOL_RECONSTRUCTION
        for error in (
            manual_A_rec_error,
            manual_B_rec_error,
            engine_A_rec_error,
            engine_B_rec_error,
        )
    )

    status_line(
        "Projection inverse reconstruction",
        pass_reconstruction,
    )

    if not pass_reconstruction:
        failures.append("projection inverse reconstruction")

    # -------------------------------------------------------------------------
    # COUPLING AMPLITUDE
    # -------------------------------------------------------------------------

    section("TEST 8 — CANONICAL COUPLING")

    fc = math.sqrt(ETA)

    efficiency_error = abs(fc * fc - ETA)

    emit(f"eta                               : {ETA:.15f}")
    emit(f"f_c = sqrt(eta)                   : {fc:.15f}")
    emit(f"f_c^2                             : {fc*fc:.15f}")
    emit(f"|f_c^2-eta|                       : {efficiency_error:.15e}")

    pass_fc = efficiency_error < TOL_FACTOR

    status_line("Canonical coupling amplitude", pass_fc)

    if not pass_fc:
        failures.append("canonical coupling amplitude")

    # -------------------------------------------------------------------------
    # GEO PROJECTION FACTOR
    # -------------------------------------------------------------------------

    section("TEST 9 — DIMENSIONLESS GEO PROJECTION FACTOR")

    P_manual = fc / A_prime_manual
    P_engine = fc / A_prime_engine

    P_closed = math.sqrt(6.0 / 5.0)

    manual_closed_error = abs(P_manual - P_closed)
    engine_closed_error = abs(P_engine - P_closed)
    manual_engine_error = abs(P_manual - P_engine)

    emit("Constructed only after projection closure:")
    emit()
    emit("  P_geo = f_c / A'")
    emit()

    emit(f"f_c                               : {fc:.15f}")
    emit(f"A' analytic                       : {A_prime_manual:.15f}")
    emit(f"A' engine                         : {A_prime_engine:.15f}")

    emit()

    emit(f"P_geo analytic                    : {P_manual:.15f}")
    emit(f"P_geo engine                      : {P_engine:.15f}")
    emit(f"sqrt(6/5)                         : {P_closed:.15f}")

    emit()

    emit(
        f"|P_analytic - sqrt(6/5)|          : "
        f"{manual_closed_error:.15e}"
    )

    emit(
        f"|P_engine - sqrt(6/5)|            : "
        f"{engine_closed_error:.15e}"
    )

    emit(
        f"|P_analytic - P_engine|           : "
        f"{manual_engine_error:.15e}"
    )

    pass_factor = all(
        error < TOL_FACTOR
        for error in (
            manual_closed_error,
            engine_closed_error,
            manual_engine_error,
        )
    )

    status_line(
        "Canonical projection factor closure",
        pass_factor,
    )

    if not pass_factor:
        failures.append("canonical projection factor closure")

    # -------------------------------------------------------------------------
    # DERIVATION DISPLAY
    # -------------------------------------------------------------------------

    section("DERIVATION")

    emit("A + B = 1")
    emit()
    emit("At theta = pi/4:")
    emit()
    emit("A' = A cos(theta) + B sin(theta)")
    emit("   = (A+B)/sqrt(2)")
    emit("   = 1/sqrt(2)")
    emit()
    emit("The quadratic efficiency law gives:")
    emit()
    emit("f_c = sqrt(eta)")
    emit("    = sqrt(3/5)")
    emit()
    emit("Therefore:")
    emit()
    emit("P_geo = f_c / A'")
    emit("      = sqrt(3/5) / (1/sqrt(2))")
    emit("      = sqrt(3/5) * sqrt(2)")
    emit("      = sqrt(6/5)")

    # -------------------------------------------------------------------------
    # DEPENDENCY AUDIT
    # -------------------------------------------------------------------------

    section("DEPENDENCY AUDIT")

    emit("P_geo depends on:")
    emit()
    emit("  eta")
    emit("  A+B=1")
    emit("  theta=pi/4")
    emit("  eta=f_c^2")
    emit()
    emit("P_geo does NOT depend on:")
    emit()
    emit("  mu_eff")
    emit("  R")
    emit("  Phi")
    emit("  alpha")
    emit("  H_base")
    emit("  H_local")
    emit()
    emit("No Hubble target appears anywhere in the derivation.")

    # -------------------------------------------------------------------------
    # FINAL VERDICT
    # -------------------------------------------------------------------------

    section("FINAL PROJECTION VERDICT")

    tests = {
        "Canonical conservative state": pass_state,
        "Orthogonal tangent operator": pass_orthogonality,
        "Closed-form canonical projection": pass_analytic_projection,
        "Analytic norm preservation": pass_norm,
        "Analytic / engine projection closure": pass_engine_projection,
        "Engine norm closure": pass_engine_norm,
        "Inverse reconstruction": pass_reconstruction,
        "Canonical coupling": pass_fc,
        "Projection factor": pass_factor,
    }

    for name, passed in tests.items():
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

        emit("The canonical projection is analytically and")
        emit("computationally closed.")
        emit()

        emit(
            f"A' = {A_prime_engine:.15f} "
            "= 1/sqrt(2)"
        )

        emit(
            f"B' = {B_prime_engine:.15f} "
            "= -1/(5 sqrt(2))"
        )

        emit()

        emit(
            f"P_geo = {P_engine:.15f} "
            "= sqrt(6/5)"
        )

        emit()
        emit(
            "No Hubble measurement was used to obtain this result."
        )

        exit_code = 0

    # -------------------------------------------------------------------------
    # SAVE REPORT
    # -------------------------------------------------------------------------

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
