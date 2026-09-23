# GEO Original Framework — Mathematical Provenance

## Purpose

This document records the mathematical provenance of the relations used in the GEO-Hubble Geometric Projection repository.

Its purpose is to distinguish clearly between:

- relations inherited from the original GEO Hidden Geometry framework;
- relations preserved by the current GEO foundations;
- executable relations reproduced by the GEO External Operator;
- notation corrections introduced in the present repository;
- new derivations performed specifically for the corrected GEO-Hubble projection.

This provenance record is intended to prevent retrospective attribution.

A relation derived in the present repository must not be described as an original GEO formula unless it can be traced to an earlier source.

Likewise, a historical expression that is now known to contain a notation error must not be silently propagated as canonical.

---

# 1. Upstream framework

Primary upstream repository:

https://github.com/LeoTorreblanca/GEO-hidden-geometry-framework

Repository role:

- historical development of GEO — Hidden Geometry;
- canonical partition structure;
- efficiency relations;
- radial/effective response;
- geometric projection concepts;
- early cosmological applications;
- Hubble-related exploratory material.

The exact commit used for a frozen release of this repository must be recorded below.

## Upstream reference

Repository:

`GEO-hidden-geometry-framework`

Repository URL:

https://github.com/LeoTorreblanca/GEO-hidden-geometry-framework

Branch:

`main`

Role:

Historical and mathematical provenance of the GEO architecture used in
the present derivation.

Unlike the GEO External Operator dependency, this repository is used
here as a provenance reference rather than as an executable dependency
of the GEO-Hubble reproduction chain.

The formulas attributed to the original GEO framework are documented
individually below and in `FORMULA_PROVENANCE.md`.

---

# 2. Provenance classes

Every mathematical relation used in this repository is assigned one of the following provenance classes.

## Class O — Original GEO relation

A relation already present in the historical GEO development.

## Class F — Foundations-preserved relation

A relation explicitly retained or formalized in the later GEO Foundations structure.

## Class E — Executable relation

A relation implemented and reproduced by the GEO External Operator.

## Class C — Corrected notation

A historical expression whose notation or variable identification is corrected without changing the intended general architecture.

## Class N — New derivation in this repository

A mathematical consequence derived here from already existing GEO relations.

## Class H — Hubble application hypothesis

A physical identification introduced specifically to connect the GEO mathematical ratio to the Hubble observable.

These classes should be kept distinct.

---

# 3. Conservative partition

The relation

$$
\boxed{A+B=1}
$$

belongs to the canonical conservative architecture.

Provenance class:

$$
\boxed{O/F}
$$

The present repository uses this relation as the normalization condition for the reduced conservative state.

For the canonical realization,

$$
A=\eta,
$$

and therefore

$$
B=1-\eta.
$$

This is not introduced for Hubble.

It belongs to the general GEO organization.

---

# 4. Canonical efficiency parameter

The canonical value

$$
\boxed{\eta=\frac35}
$$

belongs to the GEO architectural structure used throughout the framework.

Provenance class:

$$
\boxed{O/F}
$$

Numerically,

$$
\eta=0.6.
$$

The present repository does not estimate \(\eta\) from Hubble data.

It is treated as a frozen architectural quantity.

---

# 5. Quadratic efficiency relation

The relation

$$
\boxed{\eta=f_c^2}
$$

and therefore

$$
\boxed{f_c=\sqrt{\eta}}
$$

belongs to the GEO efficiency/coupling structure.

Provenance class:

$$
\boxed{O/F}
$$

For the canonical value,

$$
f_c=\sqrt{\frac35}.
$$

Numerically,

$$
f_c=0.774596669241483\ldots
$$

This quantity is not derived from Hubble.

---

# 6. Complementary component

From

$$
A+B=1
$$

and

$$
A=\eta,
$$

the complementary coordinate is

$$
\boxed{B=1-\eta.}
$$

For

$$
\eta=\frac35,
$$

we obtain

$$
\boxed{B=\frac25.}
$$

Provenance class:

$$
\boxed{O/F}
$$

The algebraic evaluation is trivial, but the partition structure itself belongs to GEO.

---

# 7. Fundamental radial/effective law

The general radial relation is

$$
\boxed{R^3=\mu_{\rm eff}}
$$

or equivalently

$$
\boxed{R=\mu_{\rm eff}^{1/3}.}
$$

Provenance class:

$$
\boxed{O/F/E}
$$

This is one of the central distinctions preserved in the present repository.

The effective-state variable

$$
\mu_{\rm eff}
$$

and the architectural efficiency

$$
\eta
$$

must not be assumed identical in the general theory.

---

# 8. Meaning of the radial law

The radial law maps an effective normalized state into a linear response.

The conceptual structure is

$$
\boxed{\mu_{\rm eff}\longrightarrowR.}
$$

The present repository interprets the cube-root form as the conversion of a cubic/distributed normalized quantity into a corresponding linear scale.

This interpretation is consistent with the mathematical role assigned to the radial operator in GEO.

---

# 9. Historical expression requiring correction

Some historical GEO-Hubble material contained the expression

$$
R=\eta^{1/3}.
$$

This is not used as the general radial law in the present repository.

The canonical relation is

$$
R=\mu_{\rm eff}^{1/3}.
$$

Therefore the historical form is treated as requiring one of two interpretations:

1. a transcription in which \(\eta\) was written where \(\mu_{\rm eff}\) was intended; or
2. a special realization in which

$$
\mu_{\rm eff}:=\eta
$$

was imposed.

It must not be treated as a universal identity.

Provenance class:

$$
\boxed{
C
}
$$

---

# 10. Corrected radial statement

The correction adopted in this repository is

$$
\boxed{R=\mu_{\rm eff}^{1/3}.}
$$

The following statement is explicitly rejected as a universal relation:

$$
\boxed{R=\eta^{1/3}.}
$$

This correction does not modify the GEO architecture.

It restores the distinction already supported by the general formulation and current executable implementation.

---

# 11. Tangent / membrane angle

The balanced tangent orientation

$$
\boxed{\theta_0=\frac{\pi}{4}}
$$

belongs to the canonical projection geometry.

Provenance class:

$$
\boxed{O/F/E}
$$

At this angle,

$$
\cos\theta_0=\sin\theta_0=\frac1{\sqrt2}.
$$

The current External Operator implements this projection structure.

---

# 12. Tangent transformation

The orthogonal operator

$$
\boxed{Q(\theta)=\begin{pmatrix}\cos\theta & \sin\theta\\-\sin\theta & \cos\theta\end{pmatrix}}
$$

belongs to the GEO projection architecture.

Provenance class:

$$
\boxed{F/E}
$$

The present repository uses the canonical value

$$
\theta=\frac{\pi}{4}.
$$

---

# 13. Projected coordinates

Applying

$$
Q(\theta)
$$

to the conservative state

$$
\begin{pmatrix}A\\B\end{pmatrix}
$$

gives

$$
A'=A\cos\theta+B\sin\theta
$$

and

$$
B'=-A\sin\theta+B\cos\theta.
$$

Provenance class:

$$
\boxed{F/E}
$$

These relations follow directly from the matrix definition of the tangent operator.

---

# 14. Canonical projected observable

The identity

$$
A'=\frac1{\sqrt2}
$$

for a conservative state at

$$
\theta=\frac{\pi}{4}
$$

is derived in the present repository from

$$
A+B=1.
$$

Indeed,

$$
A'=A\frac1{\sqrt2}+B\frac1{\sqrt2}
$$

so

$$
A'=\frac{A+B}{\sqrt2}
$$

and therefore

$$
\boxed{A'=\frac1{\sqrt2}.}
$$

Provenance class:

$$
\boxed{N}
$$

The ingredients are inherited from GEO, but the explicit theorem-style derivation is part of this repository.

---

# 15. Canonical complementary projection

For the canonical state

$$
A=\frac35,\qquadB=\frac25,
$$

the second projected coordinate is

$$
B'=\frac{B-A}{\sqrt2}.
$$

Therefore

$$
\boxed{B'=-\frac1{5\sqrt2}.}
$$

Numerically,

$$
B'=-0.141421356237309\ldots
$$

Provenance class:

$$
\boxed{N/E}
$$

The value is analytically derived here and reproduced by the External Operator.

---

# 16. Orthogonality and reconstruction

The tangent matrix satisfies

$$
Q^TQ=I.
$$

Therefore

$$
Q^{-1}=Q^T.
$$

Consequently the projected state can be inverted to recover the original conservative state.

Provenance class:

$$
\boxed{F/E}
$$

The present repository provides the explicit proof and numerical closure test.

---

# 17. Projection norm preservation

Because \(Q\) is orthogonal,

$$
\|\mathbf v'\|=\|\mathbf v\|.
$$

Provenance class:

$$
\boxed{F/E}
$$
The External Operator reports the corresponding projection-norm error.

The tested value is at approximately floating-point machine precision.

---

# 18. Canonical projection factor

The present repository defines

$$
\boxed{P_{\rm GEO}=\frac{f_c}{A'}.}
$$

Using

$$
f_c=\sqrt{\frac35}
$$

and

$$
A'=\frac1{\sqrt2},
$$

we derive

$$
P_{\rm GEO}=\frac{\sqrt{3/5}}{1/\sqrt2}.
$$

Therefore

$$
\boxed{P_{\rm GEO}=\sqrt{\frac65}.}
$$

Provenance class:

$$
\boxed{N}
$$

This closed-form derivation is the central new mathematical consolidation of the present repository.

---

# 19. Relationship to the historical simple GEO-Hubble rule

Historical GEO-Hubble material used a compact projection relation of the form

$$
H_{\rm GEO}=H_{\rm base}\frac{f_c}{\cos\theta}.
$$

At

$$
\theta=\frac{\pi}{4},
$$

this becomes

$$
H_{\rm GEO}=H_{\rm base}\frac{f_c}{1/\sqrt2}.
$$

The present repository does not merely reuse this formula numerically.

Instead, it reconstructs the denominator from the full tangent transformation:

$$
A'=A\cos\theta+B\sin\theta.
$$

Under the conservative condition and canonical angle,

$$
A'=\frac1{\sqrt2}.
$$

Thus the historical compact denominator is recovered as a consequence of the conservative tangent geometry.

This is an important distinction.

---

# 20. New formal projection proposition

The theorem

$$
A+B=1,
$$

$$
A=\eta,
$$

$$
\eta=\frac35,
$$

$$
f_c=\sqrt{\eta},
$$

and

$$
Q=Q(\pi/4)
$$

imply

$$
\boxed{P_{\rm GEO}=\sqrt{\frac65}}
$$

is formalized in this repository.

Provenance class:

$$
\boxed{N}
$$

The theorem is not retrospectively attributed to the original repository in this exact formal form.

Its ingredients come from GEO.

Its explicit closed derivation is new here.

---

# 21. Independence from \(\mu_{\rm eff}\)

The present repository derives that

$$
P_{\rm GEO}
$$

contains no dependence on

$$
\mu_{\rm eff}.
$$

Thus

$$
\boxed{\frac{\partial P_{\rm GEO}}{\partial\mu_{\rm eff}}=0.}
$$

Provenance class:

$$
\boxed{N/E}
$$

This follows analytically from the dependency graph and is separately reproduced by the External Operator sweep.

---

# 22. External Operator sweep confirmation

At fixed

$$
\eta=0.6,
$$

the following values of

$$
\mu_{\rm eff}
$$

were tested:

$$
0.4,\,
0.5,\,
0.6,\,
0.7,\,
0.8,\,
0.8104,\,
0.9,\,
1.0.
$$

The radial response changed as expected.

The projection factor remained

$$
\boxed{P_{\rm GEO}=1.095445115010332\ldots}
$$

for every tested state.

Provenance class:

$$
\boxed{E}
$$

This is executable confirmation, not a new mathematical axiom.

---

# 23. Spectral quantities

The External Operator also computes quantities including

$$
\Phi
$$

and

$$
\alpha.
$$

These belong to the broader GEO operator chain.

They are not required to derive

$$
P_{\rm GEO}=\sqrt{\frac65}
$$

in the present repository.

Therefore they are treated as auxiliary outputs for this particular demonstration.

This choice does not remove them from GEO.

It limits only the mathematical dependencies required for the corrected Hubble projection.

---

# 24. Status of the historical radial-defect Hubble expression

Historical materials used a later expression involving quantities of the form

$$
1+\alpha(1-R).
$$

The present repository does not assume that this expression is algebraically equivalent to

$$
\frac{f_c}{A'}.
$$

Any equivalence would require a separate derivation.

Therefore the historical radial-defect construction is outside the proof chain of the present canonical projection proposition.

---

# 25. Hubble application mapping

The statement

$$
\boxed{\frac{H_{\rm GEO}}{H_{\rm base}}=P_{\rm GEO}}
$$

is not an internal theorem of the projection algebra alone.

It is the physical GEO-Hubble application hypothesis.

Provenance class:

$$
\boxed{H}
$$

The resulting equation is

$$
\boxed{H_{\rm GEO}=H_{\rm base}\sqrt{\frac65}.}
$$

---

# 26. Reference numerical Hubble output

For

$$
H_{\rm base}=67.40\ {\rm km\,s^{-1}\,Mpc^{-1}},
$$

the application hypothesis gives

$$
H_{\rm GEO}=67.40\sqrt{\frac65}.
$$

Therefore

$$
\boxed{H_{\rm GEO}=73.833000751696\ {\rm km\,s^{-1}\,Mpc^{-1}}.}
$$

Provenance class:

$$
\boxed{N/H}
$$

This number is a consequence of the derived projection factor plus the independently supplied baseline.

It is not an original canonical GEO constant.

---

# 27. Formula provenance table

| Relation | Provenance class | Status |
|---|---|---|
| \(A+B=1\) | O/F | inherited canonical architecture |
| \(A=\eta\) | O/F | canonical identification |
| \(B=1-\eta\) | O/F | algebraic consequence |
| \(\eta=3/5\) | O/F | frozen canonical value |
| \(\eta=f_c^2\) | O/F | inherited efficiency law |
| \(f_c=\sqrt{\eta}\) | O/F | algebraic inverse |
| \(R^3=\mu_{\rm eff}\) | O/F/E | canonical radial law |
| \(R=\mu_{\rm eff}^{1/3}\) | O/F/E | canonical radial law |
| \(R=\eta^{1/3}\) | C | historical special reduction / notation issue |
| \(\theta=\pi/4\) | O/F/E | canonical tangent orientation |
| \(Q(\theta)\) | F/E | tangent projection operator |
| \(A'=A\cos\theta+B\sin\theta\) | F/E | operator expansion |
| \(B'=-A\sin\theta+B\cos\theta\) | F/E | operator expansion |
| \(A'=1/\sqrt2\) | N/E | derived and engine-verified |
| \(B'=-1/(5\sqrt2)\) | N/E | derived and engine-verified |
| \(P_{\rm GEO}=f_c/A'\) | N | present repository definition |
| \(P_{\rm GEO}=\sqrt{6/5}\) | N/E | derived and engine-verified |
| \(H_{\rm GEO}/H_{\rm base}=P_{\rm GEO}\) | H | physical application hypothesis |
| \(H_{\rm GEO}=H_{\rm base}\sqrt{6/5}\) | N/H | consequence of hypothesis |

---

# 28. What is original and what is new

The following are inherited:

$$
A+B=1,
$$

$$
\eta=\frac35,
$$

$$
\eta=f_c^2,
$$

$$
R=\mu_{\rm eff}^{1/3},
$$

$$
\theta=\frac{\pi}{4},
$$

and the tangent projection structure.

The following are explicitly consolidated in this repository:

$$
A'=\frac{A+B}{\sqrt2}=\frac1{\sqrt2},
$$

$$
P_{\rm GEO}=\frac{f_c}{A'},
$$

and therefore

$$
P_{\rm GEO}=\sqrt{\frac65}.
$$

The Hubble interpretation is then stated separately.

---

# 29. No retrospective rewriting

The present repository does not claim that every historical GEO document already contained the complete corrected derivation in its current form.

Instead, the purpose is to reconstruct the logical consequence of the canonical relations after correcting the variable-level notation issue.

Historical development and current formalization are therefore both preserved.

---

# 30. Citation discipline

When describing the original GEO framework, cite the original upstream repository and its archival record.

When describing the executable implementation, cite the GEO External Operator.

When describing the theorem

$$
P_{\rm GEO}=\sqrt{\frac65},
$$

cite the present repository once it has an archival release.

This prevents new derivations from being incorrectly assigned to earlier sources.

---

# 31. Frozen-source requirement

Before public archival release, record the exact upstream commit with:

`git rev-parse HEAD`

The result must replace:

`TO_BE_RECORDED`

near the beginning of this file.

Also record:

- branch;
- retrieval date;
- repository URL;
- clean/dirty working-tree status.

---

# 32. Working-tree status

The release provenance should indicate whether the upstream source had uncommitted local modifications.

Recommended command:

`git status --short`

For a frozen public release, the preferred state is a clean working tree.

---

# 33. Historical material handling

Historical equations should not be deleted from archival provenance merely because they were later corrected.

Instead:

- preserve the historical expression;
- identify its context;
- state the corrected general law;
- explain the mathematical distinction.

This allows the development of the framework to remain auditable.

---

# 34. Provenance conclusion

The corrected GEO-Hubble projection presented here is not constructed from an isolated new numerical ansatz.

It is assembled from already existing GEO structures:

$$
A+B=1,
$$

$$
\eta=\frac35,
$$

$$
\eta=f_c^2,
$$

$$
R=\mu_{\rm eff}^{1/3},
$$

and

$$
Q(\pi/4).
$$

The new contribution of this repository is the explicit separation of these layers and the formal derivation

$$
\boxed{A'=\frac1{\sqrt2}}
$$

followed by

$$
\boxed{P_{\rm GEO}=\frac{f_c}{A'}=\sqrt{\frac65}.}
$$

The Hubble mapping is then stated separately as a testable physical hypothesis.

This provenance distinction is binding for the remainder of the repository.

