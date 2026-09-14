# 05 — Validation and Reproducibility Protocol

## Purpose

This document defines the validation protocol for the GEO-Hubble Geometric Projection repository.

Its purpose is to establish, before final release, exactly:

- which mathematical identities must hold;
- which software outputs must agree with analytic calculations;
- which quantities must remain independent;
- which numerical tolerances are accepted;
- what constitutes PASS;
- what constitutes FAIL;
- which results are mathematical;
- which results are physical hypotheses;
- which results must not be used as tuning targets.

This protocol is intended to prevent accidental circularity, undocumented assumptions, and silent reintroduction of the historical radial-law notation error.

---

# 1. Validation philosophy

The repository separates validation into four levels.

## Level 1 — Analytic mathematics

The canonical GEO relations must be derived independently of software.

These include:

\[
A+B=1,
\]

\[
A=\eta,
\]

\[
B=1-\eta,
\]

\[
\eta=f_c^2,
\]

\[
f_c=\sqrt{\eta},
\]

\[
R=\mu_{\rm eff}^{1/3},
\]

and

\[
Q(\theta)
=
\begin{pmatrix}
\cos\theta & \sin\theta\\
-\sin\theta & \cos\theta
\end{pmatrix}.
\]

---

## Level 2 — Executable reproduction

The GEO External Operator must reproduce the same canonical quantities numerically.

The software is not allowed to define the analytic result retrospectively.

The analytic derivation and executable calculation must be independently reproducible.

---

## Level 3 — Projection-factor closure

The canonical projection factor must be reconstructed from operator outputs.

It must not be hard-coded.

The expected mathematical identity is

\[
\boxed{
P_{\rm GEO}
=
\sqrt{\frac65}.
}
\]

---

## Level 4 — Hubble application

Only after Levels 1–3 pass may the projection factor be applied to an independently supplied baseline Hubble value.

The Hubble application must not influence any earlier step.

---

# 2. Frozen canonical quantities

The following architectural values are frozen for the canonical test:

\[
\boxed{
\eta=\frac35=0.6
}
\]

and

\[
\boxed{
L=0.
}
\]

The complementary coordinate is

\[
\boxed{
B=1-\eta=\frac25=0.4.
}
\]

The canonical coupling amplitude is derived as

\[
\boxed{
f_c=\sqrt{\eta}.
}
\]

The canonical tangent angle is

\[
\boxed{
\theta=\frac{\pi}{4}.
}
\]

These values must not be modified in response to Hubble measurements.

---

# 3. Test 1 — Conservative partition

## Objective

Verify the canonical conservation relation.

The test evaluates

\[
A=\eta
\]

and

\[
B=1-\eta.
\]

Then it checks

\[
A+B.
\]

## Expected result

\[
A+B=1.
\]

## Numerical reference

\[
A=0.6,
\]

\[
B=0.4,
\]

and

\[
A+B=1.
\]

## PASS criterion

\[
|A+B-1|
<
10^{-14}.
\]

## FAIL criterion

The test fails if

\[
|A+B-1|
\geq
10^{-14}.
\]

---

# 4. Test 2 — Quadratic efficiency law

## Objective

Verify

\[
\eta=f_c^2.
\]

The coupling amplitude is independently calculated as

\[
f_c=\sqrt{\eta}.
\]

## Expected result

For

\[
\eta=0.6,
\]

\[
f_c
=
0.774596669241483\ldots
\]

and

\[
f_c^2
=
0.6.
\]

## PASS criterion

\[
|f_c^2-\eta|
<
10^{-14}.
\]

---

# 5. Test 3 — Correct radial law

## Objective

Verify that the radial response is calculated from

\[
\mu_{\rm eff}
\]

and not from

\[
\eta.
\]

The required law is

\[
\boxed{
R=\mu_{\rm eff}^{1/3}.
}
\]

## Procedure

For each selected input

\[
\mu_i,
\]

calculate

\[
R_i
\]

using the GEO External Operator.

Independently calculate

\[
R_{i,\rm analytic}
=
\mu_i^{1/3}.
\]

Compare both values.

## PASS criterion

For every tested state,

\[
|R_i-R_{i,\rm analytic}|
<
10^{-13}.
\]

Additionally,

\[
|R_i^3-\mu_i|
<
10^{-13}.
\]

---

# 6. Test 4 — Independence of \(\mu_{\rm eff}\) and \(\eta\)

## Objective

Verify that changing

\[
\mu_{\rm eff}
\]

while holding

\[
\eta
\]

fixed changes

\[
R.
\]

## Required comparison

Use at least two unequal values

\[
\mu_1\neq\mu_2.
\]

For example,

\[
\mu_1=0.6
\]

and

\[
\mu_2=0.8104.
\]

The engine should return

\[
R_1
=
0.843432665301749\ldots
\]

and

\[
R_2
=
0.932323170115423\ldots
\]

while

\[
\eta=0.6
\]

remains unchanged.

## PASS criterion

The test passes if

\[
R_1\neq R_2
\]

and both individually satisfy

\[
R_i^3=\mu_i
\]

within tolerance.

## FAIL criterion

The test fails if changing

\[
\mu_{\rm eff}
\]

does not change

\[
R.
\]

Such a result would indicate accidental reintroduction of

\[
R=\eta^{1/3}.
\]

---

# 7. Test 5 — Canonical tangent matrix

## Objective

Verify the canonical tangent operator

\[
Q\left(\frac{\pi}{4}\right).
\]

The analytic matrix is

\[
Q
=
\frac1{\sqrt2}
\begin{pmatrix}
1&1\\
-1&1
\end{pmatrix}.
\]

## Orthogonality check

Calculate

\[
Q^TQ.
\]

## Expected result

\[
Q^TQ=I.
\]

## PASS criterion

The maximum absolute matrix-element error must satisfy

\[
\max
\left|
Q^TQ-I
\right|
<
10^{-14}.
\]

---

# 8. Test 6 — Analytic canonical projection

## Objective

Calculate the projected coordinates independently of the engine.

Use

\[
A=0.6,
\]

\[
B=0.4,
\]

and

\[
\theta=\frac{\pi}{4}.
\]

The first coordinate is

\[
A'
=
A\cos\theta+B\sin\theta.
\]

The second coordinate is

\[
B'
=
-A\sin\theta+B\cos\theta.
\]

## Expected results

\[
\boxed{
A'
=
\frac1{\sqrt2}
=
0.7071067811865475\ldots
}
\]

and

\[
\boxed{
B'
=
-\frac{0.2}{\sqrt2}
=
-0.1414213562373095\ldots
}
\]

---

# 9. Test 7 — Analytic versus External Operator projection

## Objective

Compare the independently derived projected coordinates with the GEO External Operator outputs.

## Required quantities

Analytic:

\[
A'_{\rm analytic},
\]

\[
B'_{\rm analytic}.
\]

Engine:

\[
A'_{\rm engine},
\]

\[
B'_{\rm engine}.
\]

## PASS criterion

\[
|A'_{\rm analytic}-A'_{\rm engine}|
<
10^{-14}
\]

and

\[
|B'_{\rm analytic}-B'_{\rm engine}|
<
10^{-14}.
\]

The current reference test produced zero difference at the displayed precision.

---

# 10. Test 8 — Projection norm closure

## Objective

Verify that the tangent projection is norm preserving.

Because

\[
Q^TQ=I,
\]

we expect

\[
\|\mathbf v'\|
=
\|\mathbf v\|.
\]

## PASS criterion

The GEO External Operator quantity

\[
\texttt{projection\_norm\_error}
\]

must satisfy

\[
|\texttt{projection\_norm\_error}|
<
10^{-13}.
\]

The current reference execution produced approximately

\[
1.11\times10^{-16}.
\]

---

# 11. Test 9 — Reconstruction closure

## Objective

Verify that the projected state reconstructs the original conservative state.

The engine returns

\[
A_{\rm rec},
\]

\[
B_{\rm rec},
\]

and optionally latent-state reconstruction.

## Expected result

\[
A_{\rm rec}=A,
\]

\[
B_{\rm rec}=B.
\]

## PASS criterion

\[
|A_{\rm rec}-A|
<
10^{-13}
\]

and

\[
|B_{\rm rec}-B|
<
10^{-13}.
\]

---

# 12. Test 10 — Projection-factor reconstruction

## Objective

Reconstruct the projection ratio from independently obtained quantities.

The script must calculate

\[
f_c=\sqrt{\eta}
\]

and obtain

\[
A'
\]

from the projection calculation or engine output.

Then it must calculate

\[
\boxed{
P_{\rm engine}
=
\frac{f_c}{A'}.
}
\]

The script must not assign

\[
P_{\rm engine}
=
\sqrt{\frac65}
\]

directly.

---

# 13. Test 11 — Closed-form projection-factor comparison

The independently derived analytic value is

\[
\boxed{
P_{\rm analytic}
=
\sqrt{\frac65}.
}
\]

The reconstructed engine value is

\[
P_{\rm engine}
=
\frac{f_c}{A'_{\rm engine}}.
\]

## PASS criterion

\[
|P_{\rm engine}-P_{\rm analytic}|
<
10^{-13}.
\]

The current reference execution produced

\[
2.22\times10^{-16}.
\]

---

# 14. Test 12 — Independence of projection from radial state

## Objective

Verify that the projection factor remains constant when

\[
\mu_{\rm eff}
\]

is varied independently.

## Required sweep

At minimum evaluate

\[
\mu_{\rm eff}
=
0.4,
0.5,
0.6,
0.7,
0.8,
0.9,
1.0.
\]

Additional intermediate states are permitted.

## Quantities recorded

For each state record:

\[
\mu_{\rm eff},
\]

\[
R,
\]

\[
A',
\]

\[
f_c,
\]

\[
P_{\rm GEO},
\]

\[
\Phi,
\]

\[
\alpha.
\]

## Expected behavior

The following may change:

\[
R,
\]

\[
\Phi,
\]

\[
\alpha.
\]

The following should remain fixed:

\[
\eta,
\]

\[
f_c,
\]

\[
A',
\]

\[
P_{\rm GEO}.
\]

---

# 15. Projection-invariance PASS criterion

Define

\[
P_{\rm max}
=
\max_i P_i
\]

and

\[
P_{\rm min}
=
\min_i P_i.
\]

The projection span is

\[
\Delta P
=
P_{\rm max}-P_{\rm min}.
\]

## PASS criterion

\[
\boxed{
\Delta P
<
10^{-13}.
}
\]

The current reference run produced

\[
\Delta P=0
\]

at the displayed precision.

---

# 16. Projected-coordinate invariance criterion

Similarly define

\[
A'_{\rm max}
\]

and

\[
A'_{\rm min}.
\]

The span is

\[
\Delta A'
=
A'_{\rm max}-A'_{\rm min}.
\]

## PASS criterion

\[
\boxed{
\Delta A'
<
10^{-13}.
}
\]

The current reference run produced

\[
\Delta A'=0.
\]

---

# 17. Test 13 — Hubble factor is generated only after projection closure

The Hubble test may run only after the projection-factor tests pass.

The Hubble script receives an external input

\[
H_{\rm base}.
\]

It then calculates

\[
H_{\rm pred}
=
P_{\rm GEO}H_{\rm base}.
\]

The script must obtain

\[
P_{\rm GEO}
\]

from the operator reconstruction.

It must not hard-code

\[
73.833000751696.
\]

---

# 18. Reference Hubble test

For the reference value

\[
H_{\rm base}=67.4,
\]

the expected output is

\[
H_{\rm pred}
=
67.4P_{\rm GEO}.
\]

Using the independently reconstructed factor,

\[
P_{\rm GEO}
=
1.095445115010332\ldots
\]

gives

\[
\boxed{
H_{\rm pred}
=
73.833000751696\ldots
}
\]

---

# 19. Hubble calculation PASS criterion

The Hubble script should independently compare its output with the analytic expression

\[
H_{\rm analytic}
=
H_{\rm base}\sqrt{\frac65}.
\]

## PASS criterion

\[
|H_{\rm pred}-H_{\rm analytic}|
<
10^{-11}.
\]

The looser tolerance relative to dimensionless tests allows for normal floating-point propagation in the final multiplication.

---

# 20. Forbidden tuning operations

The following operations are not permitted in the canonical reproduction.

The script must not solve for

\[
\eta
\]

using a target value of

\[
H_{\rm local}.
\]

It must not solve for

\[
\theta
\]

using a target value of

\[
H_{\rm local}.
\]

It must not solve for

\[
f_c
\]

using a target value of

\[
H_{\rm local}.
\]

It must not solve for

\[
\mu_{\rm eff}
\]

using a target value of

\[
H_{\rm local}.
\]

It must not set

\[
P_{\rm GEO}
=
\frac{H_{\rm local}}
{H_{\rm base}}
\]

and then claim that value was predicted.

---

# 21. Forbidden radial shortcut

The canonical scripts must not calculate

\[
R=\eta^{1/3}.
\]

The radial response must always be calculated as

\[
\boxed{
R=\mu_{\rm eff}^{1/3}.
}
\]

An explicit historical-reproduction script may use

\[
\mu_{\rm eff}:=\eta
\]

only if it is clearly labelled as a historical special case.

No such historical case may be used as evidence for the corrected general derivation.

---

# 22. No hidden Hubble target

The repository must contain no hard-coded local-Hubble target in the core mathematical scripts.

Searches such as the following should be used during release preparation:

- `73.04`
- `73.0`
- `SH0ES`
- `local_H0`
- `target_H0`

Any occurrence must be reviewed.

A target value may appear in a later empirical comparison script, but never in the geometric derivation scripts.

---

# 23. Separation between prediction and comparison

The workflow must be:

\[
\text{derive geometry}
\]

then

\[
\text{freeze geometry}
\]

then

\[
\text{calculate prediction}
\]

then

\[
\text{compare with observation}.
\]

It must never be:

\[
\text{inspect observation}
\]

then

\[
\text{adjust geometry}
\]

then

\[
\text{report agreement}.
\]

---

# 24. External Operator version control

Every archival release of this repository must record the exact commit of the GEO External Operator used for validation.

The commit hash must be stored in

`provenance/EXTERNAL_OPERATOR.md`.

The command used to obtain the hash is:

`git rev-parse HEAD`

The repository URL must also be recorded.

---

# 25. Original GEO framework version control

The exact revision of

`GEO-hidden-geometry-framework`

used for provenance must also be recorded.

The commit hash must be stored in

`provenance/GEO_ORIGINAL.md`.

This allows later reviewers to distinguish the historical mathematical source from subsequent changes.

---

# 26. Clean-environment reproduction

Before archival release, the complete validation chain must be reproduced from a clean environment.

Recommended procedure:

1. create a new Python virtual environment;
2. install the frozen dependencies;
3. install the GEO External Operator;
4. run its native tests;
5. run this repository's tests;
6. run the full reproduction script;
7. compare generated outputs with the archived reference outputs.

No cached local development state should be required.

---

# 27. Required dependency verification

The environment should record at minimum:

- Python version;
- NumPy version;
- SciPy version if used;
- pytest version;
- GEO External Operator version;
- compiler information if the C extension is rebuilt;
- operating system information.

This information should be written to a reproducibility log.

---

# 28. Required local test suite

The repository's own tests must include:

`test_radial_law.py`

`test_projection.py`

`test_mu_eta_independence.py`

`test_hubble_factor.py`

All tests must pass before release.

---

# 29. Required script sequence

The reference reproduction sequence is:

`01_verify_geo_core.py`

followed by

`02_verify_projection_matrix.py`

followed by

`03_verify_radial_projection_independence.py`

followed by

`04_hubble_projection_factor.py`

followed by

`05_full_reproduction.py`

Each script must be executable independently.

The final script may call the earlier logic internally, but the earlier scripts must remain usable as isolated audit stages.

---

# 30. Required result files

The reproduction chain should generate at minimum:

`results/01_geo_core_check.txt`

`results/02_projection_check.txt`

`results/03_radial_projection_console.log`

`results/03_radial_projection_independence.txt`

`results/04_hubble_projection.txt`

`results/05_full_reproduction.txt`

These outputs must be generated.

They must not be manually edited.

---

# 31. Required radial/projection-independence audit contents

The Stage 03 radial/projection-independence audit must preserve both the
execution trace and a concise human-readable result.

The reference files are:

`results/03_radial_projection_console.log`

and

`results/03_radial_projection_independence.txt`

For every tested effective state, the audit should report or preserve the
following quantities:

- `mu_eff`
- `eta`
- `R`
- `R^3 - mu_eff`
- `projected_observable`
- `fc`
- `projection_factor`
- `Phi`
- `alpha`
- `projection_norm_error`

The audit must make it possible to verify simultaneously that

\[
R^3=\mu_{m eff}
\]

to floating-point precision and that, with the canonical architecture held
fixed,

\[
P_{m GEO}
=
rac{f_c}{A'}
\]

remains unchanged throughout the tested \(\mu_{m eff}\) sweep.

The console log preserves the full execution trace.

The TXT result preserves the concise human-readable audit summary.

A CSV file is not required by the current reference implementation.

---

# 32. Final reproduction summary

The final reproduction script should report a compact status block.

The intended structure is:

GEO CORE — PASS

RADIAL LAW — PASS

MU / ETA INDEPENDENCE — PASS

ORTHOGONAL PROJECTION — PASS

ANALYTIC / ENGINE PROJECTION — PASS

RECONSTRUCTION — PASS

PROJECTION INVARIANCE — PASS

PROJECTION FACTOR — PASS

HUBBLE REFERENCE CALCULATION — PASS

The final script must return a non-zero exit status if any required test fails.

---

# 33. Machine-precision interpretation

Agreement at

\[
10^{-16}
\]

does not constitute empirical evidence about cosmology.

It means only that:

- the analytic formulas;
- the software implementation;
- and the selected floating-point representation

agree numerically to machine precision.

This distinction must be preserved in all scientific documentation.

---

# 34. Mathematical validation versus physical validation

The validation hierarchy is:

## Mathematical validation

Does the algebra close?

## Software validation

Does the engine reproduce the algebra?

## Numerical validation

Are the expected invariances reproduced across the test domain?

## Physical validation

Does the resulting fixed prediction agree with independent cosmological measurements?

Passing the first three levels does not automatically imply the fourth.

---

# 35. Empirical comparison protocol

Empirical Hubble comparisons should be performed only after the mathematical repository is frozen.

For an independently measured pair

\[
H_{\rm base}\pm\sigma_b
\]

and

\[
H_{\rm high}\pm\sigma_h,
\]

calculate

\[
H_{\rm pred}
=
P_{\rm GEO}H_{\rm base}.
\]

If

\[
P_{\rm GEO}
\]

is frozen, then

\[
\sigma_{\rm pred}
=
P_{\rm GEO}\sigma_b.
\]

Then calculate

\[
\Delta_H
=
H_{\rm high}-H_{\rm pred}.
\]

For a simplified independent Gaussian comparison,

\[
\sigma_\Delta
=
\sqrt{
\sigma_h^2
+
\sigma_{\rm pred}^2
}.
\]

Finally,

\[
\boxed{
Z_{\rm GEO}
=
\frac{\Delta_H}{\sigma_\Delta}.
}
\]

This statistic is only a simplified diagnostic.

A full cosmological likelihood comparison may require covariance and model-specific inference.

---

# 36. Empirical PASS is not binary framework validation

The repository should not define a universal physical PASS threshold such as

\[
|Z|<1
\]

as proof of GEO.

Instead, the empirical comparison should report the measured residual transparently.

For example:

- predicted ratio;
- observed ratio;
- uncertainty;
- residual;
- standardized residual.

Interpretation should remain proportional to the evidence.

---

# 37. Falsification condition

The specific canonical GEO-Hubble projection hypothesis predicts

\[
\boxed{
\frac{H_{\rm high}}
{H_{\rm base}}
=
\sqrt{\frac65}.
}
\]

If sufficiently precise independent measurements establish a ratio significantly incompatible with this value, then this specific projection hypothesis is disfavored or falsified.

The projection factor must not be adjusted after such a result.

---

# 38. Regression protection

Future code changes must not silently alter the canonical values.

Regression tests should protect at minimum:

\[
\eta=0.6,
\]

\[
f_c=\sqrt{0.6},
\]

\[
A'=\frac1{\sqrt2},
\]

and

\[
P_{\rm GEO}=\sqrt{\frac65}.
\]

The radial tests must simultaneously ensure that

\[
R
\]

continues to depend on

\[
\mu_{\rm eff}.
\]

---

# 39. Release checklist

Before a release is tagged, verify:

- all documentation files are complete;
- no historical radial typo remains unlabelled;
- External Operator commit is recorded;
- original GEO commit is recorded;
- all local tests pass;
- External Operator native tests pass;
- full reproduction passes;
- generated results are current;
- no Hubble target appears in the derivation scripts;
- dependencies are frozen;
- citation metadata is complete;
- license is complete;
- mathematical PDF matches the repository equations;
- release archive reproduces from a clean environment.

---

# 40. Validation table

| Test | Quantity | Expected result | Tolerance |
|---|---|---:|---:|
| Conservation | \(A+B\) | \(1\) | \(10^{-14}\) |
| Quadratic efficiency | \(f_c^2-\eta\) | \(0\) | \(10^{-14}\) |
| Radial law | \(R^3-\mu_{\rm eff}\) | \(0\) | \(10^{-13}\) |
| Tangent orthogonality | \(Q^TQ-I\) | \(0\) | \(10^{-14}\) |
| Analytic projection | \(A'\) | \(1/\sqrt2\) | \(10^{-14}\) |
| Engine projection | \(A'_{\rm eng}-A'_{\rm ana}\) | \(0\) | \(10^{-14}\) |
| Complementary projection | \(B'_{\rm eng}-B'_{\rm ana}\) | \(0\) | \(10^{-14}\) |
| Projection norm | norm error | \(0\) | \(10^{-13}\) |
| Reconstruction | reconstructed-original | \(0\) | \(10^{-13}\) |
| Projection factor | \(P_{\rm eng}-\sqrt{6/5}\) | \(0\) | \(10^{-13}\) |
| \(\mu\)-sweep projection span | \(\Delta P\) | \(0\) | \(10^{-13}\) |
| Reference Hubble calculation | engine-analytic | \(0\) | \(10^{-11}\) |

---

# 41. Current reference validation state

The tests already performed manually established:

\[
R^3=\mu_{\rm eff}
\]

to machine precision over the tested sweep.

The projection output remained

\[
A'
=
0.707106781186547\ldots
\]

for all tested

\[
\mu_{\rm eff}.
\]

The reconstructed projection factor remained

\[
P_{\rm GEO}
=
1.095445115010332\ldots
\]

with zero displayed span.

The analytic-versus-engine projection errors were zero at the displayed precision.

The closed-form factor difference was approximately

\[
2.22\times10^{-16}.
\]

These manual results will be converted into automated scripts and tests.

---

# 42. Final protocol rule

The central release rule is:

\[
\boxed{
\text{derive first, freeze second, compare last}.
}
\]

The geometry must be completed before observational comparison.

No observational target may be used to repair, tune, or redefine the canonical derivation after the fact.

This rule governs every numerical and scientific result in the GEO-Hubble Geometric Projection repository.
