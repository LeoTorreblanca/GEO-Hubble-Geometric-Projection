# GEO-Hubble Geometric Projection

## A reproducible geometric-projection derivation from the canonical GEO architecture

**Author:** Leonel Hernán Torreblanca  
**Framework:** GEO — Hidden Geometry  
**Status:** Research / reproducibility repository  
**Version:** 1.0.0

---

# 1. Purpose

This repository presents a focused mathematical and computational reconstruction of the GEO-Hubble geometric-projection hypothesis.

The objective is deliberately narrow:

> Determine whether a fixed dimensionless projection factor follows from the canonical GEO geometry before any local Hubble-scale value is supplied, and then examine the consequence of applying that factor to an external baseline Hubble value.

The calculation is organized so that:

1. the GEO architecture is fixed first;
2. the projection factor is derived analytically;
3. the same geometry is reproduced with the public GEO External Operator;
4. the radial and projection sectors are tested for independence;
5. only then is a Hubble baseline introduced.

No local-Hubble target is used to determine the geometric factor.

---

# 2. Main result

For the canonical conservative GEO architecture,

\[
A+B=1,
\]

with

\[
A=\eta,
\qquad
B=1-\eta,
\]

and

\[
\eta=\frac35,
\]

the GEO coupling amplitude is

\[
f_c=\sqrt{\eta}
=
\sqrt{\frac35}.
\]

At the canonical membrane orientation

\[
\theta_M=\frac{\pi}{4},
\]

the first projected coordinate is

\[
A'
=
A\cos\theta_M
+
B\sin\theta_M.
\]

Since

\[
\cos\left(\frac{\pi}{4}\right)
=
\sin\left(\frac{\pi}{4}\right)
=
\frac1{\sqrt2},
\]

and

\[
A+B=1,
\]

we obtain

\[
\boxed{
A'=\frac1{\sqrt2}
}.
\]

The GEO projection ratio is therefore

\[
P_{\rm GEO}
=
\frac{f_c}{A'}.
\]

Hence

\[
P_{\rm GEO}
=
\frac{\sqrt{3/5}}
{1/\sqrt2}
=
\sqrt{\frac65}.
\]

Therefore

\[
\boxed{
P_{\rm GEO}
=
\sqrt{\frac65}
=
1.095445115010332\ldots
}
\]

This is the central mathematical result examined by this repository.

---

# 3. General projection form

Before fixing the canonical value of \(\eta\), the projection ratio may be written as

\[
P(\eta,\theta)
=
\frac{\sqrt{\eta}}
{\eta\cos\theta+(1-\eta)\sin\theta}.
\]

At the balanced membrane,

\[
\theta=\frac{\pi}{4},
\]

this becomes

\[
P\left(\eta,\frac{\pi}{4}\right)
=
\frac{\sqrt{\eta}}
{\left[\eta+(1-\eta)\right]/\sqrt2}.
\]

Since

\[
\eta+(1-\eta)=1,
\]

we obtain

\[
\boxed{
P\left(\eta,\frac{\pi}{4}\right)
=
\sqrt{2\eta}
}.
\]

For the canonical GEO value

\[
\eta=\frac35,
\]

this gives

\[
\boxed{
P_{\rm GEO}
=
\sqrt{2\frac35}
=
\sqrt{\frac65}
}.
\]

Thus \(6/5\) is not introduced as an independently fitted constant.

It is the closed algebraic form of the canonical GEO projection at

\[
\eta=\frac35
\]

and

\[
\theta=\frac{\pi}{4}.
\]

---

# 4. Canonical GEO inputs used here

## 4.1 Conservation

For the reduced conservative GEO state,

\[
\boxed{
A+B=1
}.
\]

## 4.2 Canonical partition

\[
\boxed{
A=\eta=\frac35
}
\]

and therefore

\[
\boxed{
B=1-\eta=\frac25
}.
\]

Numerically,

\[
A=0.6,
\qquad
B=0.4.
\]

## 4.3 Coupling relation

The canonical GEO coupling satisfies

\[
\boxed{
\eta=f_c^2
}.
\]

Therefore

\[
\boxed{
f_c=\sqrt{\eta}
}.
\]

For

\[
\eta=\frac35,
\]

\[
\boxed{
f_c
=
\sqrt{\frac35}
=
0.774596669241483\ldots
}.
\]

## 4.4 Canonical membrane

The balanced tangent/membrane orientation used in the present External Operator realization is

\[
\boxed{
\theta_M=\frac{\pi}{4}
}.
\]

This repository uses the exact membrane orientation.

More advanced angular reconstruction states belong to broader GEO developments and are outside the scope of this repository.

---

# 5. Projection operator

The conservative pair is

\[
\mathbf v
=
\begin{pmatrix}
A\\
B
\end{pmatrix}.
\]

The canonical orthogonal projection operator is

\[
\boxed{
Q(\theta)
=
\begin{pmatrix}
\cos\theta & \sin\theta\\
-\sin\theta & \cos\theta
\end{pmatrix}
}.
\]

The projected state is

\[
\mathbf v'
=
Q(\theta)\mathbf v.
\]

Therefore

\[
A'
=
A\cos\theta+B\sin\theta
\]

and

\[
B'
=
-A\sin\theta+B\cos\theta.
\]

At

\[
\theta=\frac{\pi}{4},
\]

we obtain

\[
A'
=
\frac{A+B}{\sqrt2}
=
\frac1{\sqrt2},
\]

and

\[
B'
=
\frac{B-A}{\sqrt2}.
\]

For

\[
A=0.6,
\qquad
B=0.4,
\]

the projected coordinates are

\[
\boxed{
A'
=
0.7071067811865475\ldots
}
\]

and

\[
\boxed{
B'
=
-0.1414213562373095\ldots
}.
\]

The GEO External Operator reproduces these values to floating-point precision.

---

# 6. GEO Canonical Projection Proposition

Let

\[
A+B=1,
\]

with

\[
A=\eta,
\qquad
B=1-\eta,
\]

and let

\[
f_c^2=\eta.
\]

Let the conservative pair be transformed by

\[
Q\left(\frac{\pi}{4}\right).
\]

Then

\[
A'
=
\frac1{\sqrt2}.
\]

Therefore

\[
\frac{f_c}{A'}
=
\sqrt{2\eta}.
\]

For the canonical value

\[
\eta=\frac35,
\]

it follows that

\[
\boxed{
\frac{f_c}{A'}
=
\sqrt{\frac65}
}.
\]

## Proof

At

\[
\theta=\frac{\pi}{4},
\]

\[
A'
=
A\frac1{\sqrt2}
+
B\frac1{\sqrt2}.
\]

Thus

\[
A'
=
\frac{A+B}{\sqrt2}.
\]

Since

\[
A+B=1,
\]

\[
A'
=
\frac1{\sqrt2}.
\]

Also,

\[
f_c=\sqrt{\eta}.
\]

Therefore

\[
\frac{f_c}{A'}
=
\frac{\sqrt{\eta}}
{1/\sqrt2}
=
\sqrt{2\eta}.
\]

For

\[
\eta=\frac35,
\]

\[
\frac{f_c}{A'}
=
\sqrt{\frac65}.
\]

QED.

---

# 7. Relation to the simpler GEO projection form

The projection ratio is not introduced as an additional fitted parameter.

At the canonical membrane,

\[
A'
=
\frac1{\sqrt2}
=
\cos\left(\frac{\pi}{4}\right).
\]

Therefore

\[
\frac{f_c}{A'}
=
\frac{f_c}
{\cos(\pi/4)}.
\]

The operator formulation used in this repository therefore reproduces the simpler GEO geometric projection form at the exact canonical membrane.

The closed form

\[
\sqrt{\frac65}
\]

is a derived algebraic consequence of that geometry.

It is not introduced from a Hubble target.

---

# 8. Corrected radial-law interpretation

GEO also contains a radial/effective relation.

The general law used in this repository is

\[
\boxed{
R^3=\mu_{\rm eff}
}
\]

or equivalently

\[
\boxed{
R=\mu_{\rm eff}^{1/3}
}.
\]

Here:

- \(\eta\) is the canonical architectural efficiency;
- \(\mu_{\rm eff}\) is an effective state supplied to the radial sector;
- \(R\) is the corresponding radial response.

These quantities must not be universally identified.

In general,

\[
\boxed{
\mu_{\rm eff}\neq\eta
}.
\]

Therefore

\[
R=\eta^{1/3}
\]

must not be interpreted as the general GEO radial law.

That expression can occur only in a special case in which an application independently establishes

\[
\mu_{\rm eff}=\eta.
\]

The present Hubble projection derivation does not require that identification.

---

# 9. Radial and projection sectors

The radial transformation

\[
\mu_{\rm eff}
\longrightarrow
R=\mu_{\rm eff}^{1/3}
\]

and the canonical projection

\[
(\eta,\theta_M)
\longrightarrow
P_{\rm GEO}
\]

belong to different layers of the tested GEO implementation.

This separation is verified numerically.

With

\[
\eta=0.6
\]

held fixed, \(\mu_{\rm eff}\) can be varied over a range of values.

The corresponding radial response \(R\) changes.

The External Operator also returns changes in state-dependent derived quantities such as \(\Phi\) and \(\alpha\).

At the same time, the canonical projected observable remains

\[
A'
=
0.7071067811865475\ldots
\]

and the projection ratio remains

\[
P_{\rm GEO}
=
1.095445115010332\ldots
\]

for the tested canonical projection.

Thus the present projection factor is not generated by imposing a particular value of \(\mu_{\rm eff}\).

---

# 10. GEO External Operator

This repository uses the public **GEO External Operator** as a separate executable implementation of the GEO architecture.

Repository:

https://github.com/LeoTorreblanca/GEO-External-Operator

Reference commit used for the present audit:

    003402ef5edff2fe6efa020c368de8064e711732

Reference API version:

    1

The External Operator is not modified by this repository to force a Hubble result.

It is used to reproduce and verify:

- the canonical partition;
- the independent \(\eta\) and \(\mu_{\rm eff}\) inputs;
- the radial law;
- the canonical tangent projection;
- forward projection;
- inverse reconstruction;
- projection norm closure;
- state-dependent spectral quantities;
- analytic-versus-engine agreement.

The more extensive GEO External Operator v2 is outside the scope of the present project.

---

# 11. Analytic versus engine closure

For

\[
A=0.6,
\qquad
B=0.4,
\qquad
\theta=\frac{\pi}{4},
\]

the analytic calculation gives

\[
A'_{\rm analytic}
=
0.707106781186547\ldots
\]

and

\[
B'_{\rm analytic}
=
-0.141421356237309\ldots
\]

The External Operator returns the same values at the displayed precision.

The projection ratio reconstructed from the engine is

\[
P_{\rm engine}
=
\frac{f_c}
{A'_{\rm engine}}
=
1.095445115010332\ldots
\]

while the analytic result is

\[
P_{\rm analytic}
=
\sqrt{\frac65}
=
1.095445115010332\ldots
\]

The observed difference in the reference reproduction is approximately

\[
\boxed{
\left|
P_{\rm engine}
-
P_{\rm analytic}
\right|
\approx
2.22\times10^{-16}
}.
\]

This difference is consistent with floating-point precision.

---

# 12. GEO-Hubble application hypothesis

The mathematical result above does not by itself establish a physical cosmological mapping.

A separate application hypothesis is required.

The hypothesis examined in this repository is

\[
\boxed{
\frac{H_{\rm GEO}}
{H_{\rm base}}
=
P_{\rm GEO}
}.
\]

Therefore

\[
\boxed{
H_{\rm GEO}
=
H_{\rm base}
P_{\rm GEO}
}.
\]

Using the derived canonical ratio,

\[
\boxed{
H_{\rm GEO}
=
H_{\rm base}
\sqrt{\frac65}
}.
\]

This distinction is fundamental:

- \(P_{\rm GEO}=\sqrt{6/5}\) is the mathematical consequence of the stated canonical projection;
- identifying a Hubble-scale ratio with \(P_{\rm GEO}\) is the physical GEO-Hubble application hypothesis.

The two statements are related but distinct.

---

# 13. Reference Hubble evaluation

Only after the geometric factor has been derived is a Hubble baseline introduced.

For the reference value

\[
H_{\rm base}
=
67.40\ {\rm km\,s^{-1}\,Mpc^{-1}},
\]

the application hypothesis gives

\[
H_{\rm GEO}
=
67.40
\sqrt{\frac65}.
\]

Therefore

\[
\boxed{
H_{\rm GEO}
=
73.833000751696
\ {\rm km\,s^{-1}\,Mpc^{-1}}
}.
\]

This numerical value is obtained by applying the frozen geometric factor to the stated external baseline.

It is not used to determine:

- \(\eta\);
- \(f_c\);
- \(\theta_M\);
- \(A'\);
- \(P_{\rm GEO}\).

No local value such as

\[
73.04\ {\rm km\,s^{-1}\,Mpc^{-1}}
\]

is used as a fitting target in this derivation.

---

# 14. No-target audit

The order of the calculation is

\[
\text{GEO architecture}
\]

\[
\Downarrow
\]

\[
\text{canonical membrane projection}
\]

\[
\Downarrow
\]

\[
P_{\rm GEO}
\]

\[
\Downarrow
\]

\[
\text{external } H_{\rm base}
\]

\[
\Downarrow
\]

\[
H_{\rm GEO}.
\]

The Hubble baseline enters only after the internal geometric factor has been obtained.

This ordering prevents a desired final Hubble value from determining the internal GEO parameters.

---

# 15. Automated validation

The repository contains automated mathematical and regression tests for:

- the corrected radial law;
- \(\eta/\mu_{\rm eff}\) independence;
- conservation;
- the canonical projection matrix;
- orthogonality;
- determinant closure;
- norm preservation;
- inverse reconstruction;
- analytic-versus-engine agreement;
- the closed-form projection factor;
- independence of \(P_{\rm GEO}\) from \(\mu_{\rm eff}\);
- independence of \(P_{\rm GEO}\) from the Hubble baseline;
- the final reference Hubble multiplication.

The frozen validation suite currently contains

\[
\boxed{
130\ {\rm passing\ tests}
}.
\]

To run the suite:

    pytest -q

Expected summary:

    130 passed

The exact runtime may vary by machine.

---

# 16. Full reproduction chain

The scientific reproduction scripts are executed in the following order.

## Stage 01 — GEO core

File:

    scripts/01_verify_geo_core.py

Checks:

- conservation;
- canonical partition;
- coupling relation;
- corrected radial law;
- External Operator core behavior.

## Stage 02 — Projection matrix

File:

    scripts/02_verify_projection_matrix.py

Checks:

- \(Q(\pi/4)\);
- orthogonality;
- determinant;
- analytic projection;
- External Operator projection;
- inverse reconstruction;
- norm closure.

## Stage 03 — Radial/projection independence

File:

    scripts/03_verify_radial_projection_independence.py

Checks:

- variation of \(\mu_{\rm eff}\);
- response of \(R\);
- response of state-dependent quantities;
- stability of the canonical projection;
- stability of \(P_{\rm GEO}\).

## Stage 04 — Hubble projection

File:

    scripts/04_hubble_projection_factor.py

Checks:

- reconstruction of \(P_{\rm GEO}\);
- comparison with \(\sqrt{6/5}\);
- introduction of an external Hubble baseline only after the geometry is frozen;
- dimensional consistency;
- no-target audit.

## Stage 05 — Full reproduction

File:

    scripts/05_full_reproduction.py

Runs the complete validation chain and performs an additional final reconstruction.

---

# 17. Running the reproduction

The project expects access to the GEO External Operator.

In the archived development environment used for the reference audit, the environment was activated with

    source ~/GEO-EXTERNAL-TEST/GEO-External-Operator/.venv/bin/activate

From the repository root, the complete sequence is

    python scripts/01_verify_geo_core.py
    python scripts/02_verify_projection_matrix.py
    python scripts/03_verify_radial_projection_independence.py
    python scripts/04_hubble_projection_factor.py
    python scripts/05_full_reproduction.py

To run the regression suite:

    pytest -q

The exact upstream revisions used in the reference audit are recorded under `provenance/` and `references/`.

---

# 18. Repository structure

The repository contains the following principal files and directories.

Root:

    README.md
    LICENSE
    CITATION.cff
    pyproject.toml
    requirements.txt

Documentation:

    docs/01_geo_foundations.md
    docs/02_projection_derivation.md
    docs/03_hubble_hypothesis.md
    docs/04_radial_law_correction.md
    docs/05_validation_protocol.md

Provenance:

    provenance/GEO_ORIGINAL.md
    provenance/EXTERNAL_OPERATOR.md
    provenance/FORMULA_PROVENANCE.md

External dependency documentation:

    external/README.md

References:

    references/README.md
    references/GEO-hidden-geometry-framework.url
    references/GEO-External-Operator.url

Reproduction scripts:

    scripts/01_verify_geo_core.py
    scripts/02_verify_projection_matrix.py
    scripts/03_verify_radial_projection_independence.py
    scripts/04_hubble_projection_factor.py
    scripts/05_full_reproduction.py

Regression tests:

    tests/test_radial_law.py
    tests/test_projection.py
    tests/test_mu_eta_independence.py
    tests/test_hubble_factor.py

Primary recorded results:

    results/01_geo_core_check.txt
    results/02_projection_check.txt
    results/03_radial_projection_independence.txt
    results/04_hubble_projection.txt
    results/05_full_reproduction.txt
    results/environment.txt
    results/pytest_full.log
    results/test_summary.txt

Additional console logs may also be present under `results/`.

---

# 19. Provenance

This project keeps three levels of provenance conceptually separate.

## 19.1 Original GEO framework

Repository:

https://github.com/LeoTorreblanca/GEO-hidden-geometry-framework

Reference commit used for the present audit:

    7606fef854aeb3fbe6082a78f7794209eab850da

This layer provides the mathematical and historical GEO framework from which the canonical architecture is taken.

## 19.2 GEO External Operator

Repository:

https://github.com/LeoTorreblanca/GEO-External-Operator

Reference commit:

    003402ef5edff2fe6efa020c368de8064e711732

API version:

    1

This layer provides the separate executable implementation used for numerical verification.

## 19.3 Present repository

This repository provides the focused GEO-Hubble reconstruction:

- corrected radial-law interpretation;
- canonical projection derivation;
- closed-form projection factor;
- analytic-versus-engine verification;
- radial/projection independence tests;
- Hubble application hypothesis;
- reference numerical consequence.

---

# 20. Formula provenance

The central quantities should be interpreted according to their role.

| Quantity | Role |
| --- | --- |
| \(A+B=1\) | conservative GEO relation |
| \(\eta=3/5\) | canonical GEO partition parameter |
| \(B=1-\eta\) | complementary partition |
| \(f_c=\sqrt{\eta}\) | canonical coupling amplitude |
| \(\theta_M=\pi/4\) | canonical membrane/tangent orientation used here |
| \(Q(\theta)\) | orthogonal projection operator |
| \(R=\mu_{\rm eff}^{1/3}\) | general radial/effective law |
| \(A'=1/\sqrt2\) | derived canonical projected coordinate |
| \(P_{\rm GEO}=f_c/A'\) | operator-form projection ratio used here |
| \(P_{\rm GEO}=\sqrt{6/5}\) | closed analytic form at canonical values |
| \(H_{\rm GEO}/H_{\rm base}=P_{\rm GEO}\) | physical GEO-Hubble application hypothesis |

The detailed dependency map is contained in

    provenance/FORMULA_PROVENANCE.md

---

# 21. Scope

This repository intentionally focuses on the simple GEO External Operator and the GEO-Hubble projection problem.

It does not attempt to reproduce every later development of the GEO research program.

In particular, this repository does not require:

- GEO External Operator v2;
- the complete GEO Object Reconstruction Lab;
- the complete GEO Gravity Dynamics Lab;
- the complete cosmological MCMC infrastructure;
- later extended GEO physical interpretations.

Those projects may provide additional context but are outside the reproducibility scope defined here.

---

# 22. Claim boundary

This repository establishes internal mathematical and executable closure for the stated canonical projection.

It does **not**, by itself, establish:

- a completed theory of gravity;
- a replacement for General Relativity;
- a universal modification of cosmological dynamics;
- that every cosmological observable obeys the same projection;
- that every local \(H_0\) determination must equal the projected value;
- that the Hubble tension is definitively resolved.

The mathematical statement tested here is

\[
\boxed{
P_{\rm GEO}
=
\sqrt{\frac65}
}.
\]

The physical hypothesis is

\[
\boxed{
\frac{H_{\rm GEO}}
{H_{\rm base}}
=
P_{\rm GEO}
}.
\]

Internal mathematical closure and empirical validation are different claims.

---

# 23. Falsifiability

Define an observed Hubble-scale ratio

\[
\mathcal R_{\rm obs}
=
\frac{H_{\rm local}}
{H_{\rm base}}.
\]

The specific GEO-Hubble projection hypothesis predicts

\[
\boxed{
\mathcal R_{\rm GEO}
=
\sqrt{\frac65}
}.
\]

A residual may therefore be defined as

\[
\boxed{
\Delta_{\rm GEO}
=
\mathcal R_{\rm obs}
-
\sqrt{\frac65}
}.
\]

Once observational estimates, uncertainties, and covariance assumptions are specified, this prediction can be tested statistically.

Persistent statistically significant disagreement with the fixed ratio would disfavor this specific GEO-Hubble projection hypothesis.

Compatibility would support the specific hypothesis without proving the wider GEO framework.

---

# 24. Reference environment

The frozen audit recorded the following reference configuration:

    Python 3.12.3
    pytest 9.1.1
    GEO External Operator API 1

The exact environment snapshot is stored in

    results/environment.txt

The complete regression output is stored in

    results/pytest_full.log

and the concise result in

    results/test_summary.txt

---

# 25. Reproducibility principles

The repository follows six explicit rules.

1. No local Hubble target is used to derive \(P_{\rm GEO}\).
2. \(\mu_{\rm eff}\) and \(\eta\) are not universally identified.
3. The radial law is evaluated as \(R=\mu_{\rm eff}^{1/3}\).
4. The numerical value \(\sqrt{6/5}\) is reconstructed rather than inserted as the primary computational result.
5. The Hubble baseline is introduced only after the geometric factor is frozen.
6. Mathematical closure and empirical validation are reported as different claims.

---

# 26. Citation

Citation metadata are provided in

    CITATION.cff

Author:

**Leonel Hernán Torreblanca**

ORCID:

https://orcid.org/0009-0001-2095-4499

Repository:

https://github.com/LeoTorreblanca/GEO-Hubble-Geometric-Projection

When a persistent archive or DOI is assigned to this repository, that record should be preferred for formal citation.

---

# 27. License

This repository is released under the MIT License.

See:

    LICENSE

---

# 28. Summary

The corrected GEO-Hubble reconstruction studied here is

\[
A+B=1,
\]

with

\[
A=\eta=\frac35,
\qquad
B=\frac25,
\]

and

\[
f_c=\sqrt{\eta}
=
\sqrt{\frac35}.
\]

At the canonical membrane,

\[
\theta_M=\frac{\pi}{4}.
\]

The projected observable is

\[
A'
=
A\cos\theta_M
+
B\sin\theta_M
=
\frac1{\sqrt2}.
\]

Therefore

\[
\boxed{
P_{\rm GEO}
=
\frac{f_c}{A'}
=
\sqrt{\frac65}
}.
\]

Separately, the GEO-Hubble physical application hypothesis is

\[
\boxed{
H_{\rm GEO}
=
H_{\rm base}
\sqrt{\frac65}
}.
\]

For the reference baseline

\[
H_{\rm base}
=
67.40\ {\rm km\,s^{-1}\,Mpc^{-1}},
\]

the conditional projected value is

\[
\boxed{
H_{\rm GEO}
=
73.833000751696
\ {\rm km\,s^{-1}\,Mpc^{-1}}.
\]

The general radial law remains

\[
\boxed{
R=\mu_{\rm eff}^{1/3}
},
\]

and no universal identity

\[
\mu_{\rm eff}=\eta
\]

is required by this projection derivation.

The implementation is protected by the automated regression suite and reproduced against the frozen GEO External Operator reference.
