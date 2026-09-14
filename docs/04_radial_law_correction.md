# 04 — Radial-Law Correction and Historical Notation Audit

## Purpose

This document records the correction of a historical notation error that appeared in some GEO-Hubble materials.

The purpose is not to alter the GEO framework.

The purpose is to restore the canonical distinction between:

\[
\eta
\]

and

\[
\mu_{\rm eff},
\]

and therefore between the two independent relations

\[
\eta=f_c^2
\]

and

\[
R=\mu_{\rm eff}^{1/3}.
\]

The corrected formulation used throughout this repository is:

\[
\boxed{
R^3=\mu_{\rm eff}
}
\]

or equivalently

\[
\boxed{
R=\mu_{\rm eff}^{1/3}.
}
\]

The expression

\[
R=\eta^{1/3}
\]

must not be interpreted as the general GEO radial law.

---

# 1. Two independent GEO relations

The corrected architecture contains two different operator chains.

The first is the canonical efficiency chain:

\[
\boxed{
f_c
\longrightarrow
\eta=f_c^2.
}
\]

The second is the radial/effective chain:

\[
\boxed{
\mu_{\rm eff}
\longrightarrow
R=\mu_{\rm eff}^{1/3}.
}
\]

These relations operate on different quantities.

They therefore must not be collapsed into a single identity.

---

# 2. Canonical architectural efficiency

The canonical GEO architecture uses

\[
\boxed{
\eta=\frac35.
}
\]

The corresponding coupling amplitude is

\[
f_c=\sqrt{\eta}.
\]

Thus

\[
\boxed{
f_c
=
\sqrt{\frac35}.
}
\]

Numerically,

\[
f_c
=
0.774596669241483\ldots
\]

The relation is exactly

\[
\boxed{
f_c^2=\eta.
}
\]

---

# 3. Effective-state variable

The quantity

\[
\mu_{\rm eff}
\]

belongs to a different mathematical level.

It represents an effective state supplied by a concrete realization, application, or numerical experiment.

It is not automatically determined by

\[
\eta.
\]

Therefore the general architecture requires

\[
\boxed{
\mu_{\rm eff}
\text{ to remain independent of }
\eta
}
\]

unless a particular application explicitly derives a relation between them.

---

# 4. Canonical radial law

The effective state is converted into a linear/radial response through

\[
\boxed{
R^3=\mu_{\rm eff}.
}
\]

Taking the real cube root gives

\[
\boxed{
R=\mu_{\rm eff}^{1/3}.
}
\]

The inverse relation is

\[
\boxed{
\mu_{\rm eff}=R^3.
}
\]

The closure identity is therefore

\[
\boxed{
R^3-\mu_{\rm eff}=0.
}
\]

---

# 5. Why the cube root appears

Suppose an effective normalized quantity is represented through a cubic ratio

\[
\mu_{\rm eff}
=
\frac{V_{\rm eff}}
{V_{\rm ref}}.
\]

If the corresponding geometric scale obeys

\[
V\propto\ell^3,
\]

then

\[
\frac{V_{\rm eff}}
{V_{\rm ref}}
=
\left(
\frac{\ell_{\rm eff}}
{\ell_{\rm ref}}
\right)^3.
\]

Define

\[
R
=
\frac{\ell_{\rm eff}}
{\ell_{\rm ref}}.
\]

Then

\[
\mu_{\rm eff}=R^3.
\]

Hence

\[
\boxed{
R=\mu_{\rm eff}^{1/3}.
}
\]

Thus the cube-root relation converts a cubic effective quantity into its corresponding normalized linear scale.

---

# 6. The historical transcription

Some historical GEO-Hubble materials used

\[
\boxed{
R=\eta^{1/3}.
}
\]

This expression can only follow from the canonical radial law if one first assumes

\[
\boxed{
\mu_{\rm eff}=\eta.
}
\]

Indeed,

\[
R
=
\mu_{\rm eff}^{1/3}
\]

combined with

\[
\mu_{\rm eff}=\eta
\]

would give

\[
R=\eta^{1/3}.
\]

Therefore the historical expression implicitly inserted the identification

\[
\mu_{\rm eff}=\eta.
\]

That identification is not part of the general GEO radial law.

---

# 7. Why this matters

The difference is not cosmetic.

If

\[
\eta=0.6,
\]

then

\[
\eta^{1/3}
=
0.843432665301749\ldots
\]

But if

\[
\mu_{\rm eff}=0.8104,
\]

then

\[
R
=
0.8104^{1/3}
=
0.932323170115423\ldots
\]

Both calculations can coexist while

\[
\eta
\]

remains fixed.

Therefore the radial response is controlled by

\[
\mu_{\rm eff},
\]

not directly by

\[
\eta.
\]

---

# 8. Executable evidence from the GEO External Operator

The GEO External Operator exposes a public computation interface of the form

\[
\mathrm{compute}
(
\eta,
L,
\mu_{\rm eff}
).
\]

The interface accepts

\[
\eta
\]

and

\[
\mu_{\rm eff}
\]

as independent inputs.

This design directly reflects the corrected architecture.

The engine then calculates

\[
R
=
\mu_{\rm eff}^{1/3}.
\]

---

# 9. Native test-suite evidence

The External Operator native test suite includes explicit tests for:

- API consistency;
- independence of \(\mu_{\rm eff}\) from \(\eta\);
- the canonical radial law;
- projection norm closure;
- reconstruction closure.

The observed test run reported:

\[
5\ \text{passed}
\]

with one optional test skipped.

In particular, the following tests passed:

\[
\texttt{test\_mu\_eff\_independent\_from\_eta}
\]

and

\[
\texttt{test\_canonical\_radial\_law}.
\]

This executable evidence supports the corrected interpretation.

---

# 10. Direct radial-law sweep

The External Operator was evaluated with

\[
\eta=0.6
\]

held fixed while

\[
\mu_{\rm eff}
\]

was varied.

The tested values included

\[
0.4,\,
0.5,\,
0.6,\,
0.7,\,
0.8,\,
0.8104,\,
0.9,\,
1.0.
\]

For each input, the engine returned

\[
R=\mu_{\rm eff}^{1/3}
\]

to floating-point precision.

---

# 11. Example: \(\mu_{\rm eff}=0.4\)

For

\[
\mu_{\rm eff}=0.4,
\]

the engine returned

\[
R
=
0.736806299728077\ldots
\]

The direct cube-root calculation gives the same value.

The closure residual was approximately

\[
R^3-\mu_{\rm eff}
=
-2.22\times10^{-16}.
\]

This is consistent with machine precision.

---

# 12. Example: \(\mu_{\rm eff}=0.6\)

For

\[
\mu_{\rm eff}=0.6,
\]

the engine returned

\[
R
=
0.843432665301749\ldots
\]

This value is numerically identical to

\[
0.6^{1/3}.
\]

However, in this test the reason is explicitly

\[
\mu_{\rm eff}=0.6,
\]

not the architectural statement

\[
\eta=0.6.
\]

The numerical coincidence must not be confused with a universal identity.

---

# 13. Example: \(\mu_{\rm eff}=0.8104\)

For

\[
\mu_{\rm eff}=0.8104,
\]

the engine returned

\[
R
=
0.932323170115423\ldots
\]

while

\[
\eta
\]

remained fixed at

\[
0.6.
\]

Thus

\[
R
\]

changed while the canonical architecture remained unchanged.

This is direct numerical evidence that

\[
\mu_{\rm eff}
\]

and

\[
\eta
\]

are independent variables in the executable GEO implementation.

---

# 14. Example: \(\mu_{\rm eff}=1\)

For

\[
\mu_{\rm eff}=1,
\]

the engine returned

\[
R=1.
\]

The closure is exact at the displayed precision:

\[
R^3-\mu_{\rm eff}=0.
\]

---

# 15. Independence test

Compare two states with the same architectural efficiency:

\[
\eta=0.6.
\]

State 1:

\[
\mu_{\rm eff}=0.6,
\]

\[
R_1
=
0.843432665301749.
\]

State 2:

\[
\mu_{\rm eff}=0.8104,
\]

\[
R_2
=
0.932323170115423.
\]

Therefore

\[
R_2-R_1
=
0.088890504813674\ldots
\]

while

\[
\eta
\]

remains unchanged.

Thus

\[
\boxed{
\frac{\partial R}
{\partial\mu_{\rm eff}}
\neq0
}
\]

while

\[
\eta
\]

is independently fixed.

---

# 16. Analytic derivative of the radial law

From

\[
R
=
\mu_{\rm eff}^{1/3},
\]

differentiate:

\[
\frac{dR}
{d\mu_{\rm eff}}
=
\frac13
\mu_{\rm eff}^{-2/3}.
\]

Therefore

\[
\boxed{
\frac{dR}
{d\mu_{\rm eff}}
=
\frac{1}
{3\mu_{\rm eff}^{2/3}}.
}
\]

Since

\[
R^2
=
\mu_{\rm eff}^{2/3},
\]

this may also be written

\[
\boxed{
\frac{dR}
{d\mu_{\rm eff}}
=
\frac1{3R^2}.
}
\]

Thus \(R\) responds continuously to changes in the effective state.

---

# 17. The projection branch remains separate

During the same numerical sweep, the canonical projected observable remained

\[
A'
=
0.707106781186547\ldots
\]

for all tested values of

\[
\mu_{\rm eff}.
\]

Therefore the radial branch

\[
\mu_{\rm eff}
\rightarrow
R
\]

can change without altering the canonical tangent result

\[
A'
=
\frac1{\sqrt2}.
\]

This confirms the separation between radial response and canonical projection.

---

# 18. Projection-factor independence

The canonical projection ratio is

\[
P_{\rm GEO}
=
\frac{f_c}{A'}.
\]

Since

\[
f_c
=
\sqrt{\eta},
\]

and

\[
A'
=
\frac1{\sqrt2},
\]

the ratio is

\[
P_{\rm GEO}
=
\sqrt{\frac65}.
\]

The numerical sweep showed that

\[
P_{\rm GEO}
\]

remained unchanged while

\[
\mu_{\rm eff}
\]

varied from

\[
0.4
\]

to

\[
1.0.
\]

Thus the Hubble projection derivation used in this repository does not require selecting a special radial input.

---

# 19. What is corrected

The following statement is corrected:

\[
\boxed{
R=\eta^{1/3}.
}
\]

The corrected general statement is:

\[
\boxed{
R=\mu_{\rm eff}^{1/3}.
}
\]

This is the only radial law used in this repository.

---

# 20. What is not being changed

The correction does not alter the canonical GEO relations

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

or the tangent projection

\[
Q(\pi/4).
\]

It also does not alter the independent effective-state relation

\[
R^3=\mu_{\rm eff}.
\]

The correction restores consistency between these already distinct layers.

---

# 21. What is not being claimed

The correction does not imply that

\[
\mu_{\rm eff}
\]

can never equal

\[
\eta
\]

numerically.

A concrete application is free to derive

\[
\mu_{\rm eff}=\eta
\]

if such a relation follows independently from that application.

The corrected statement is narrower:

\[
\boxed{
\mu_{\rm eff}=\eta
\text{ is not a universal GEO identity.}
}
\]

Therefore it cannot be silently assumed.

---

# 22. Historical compatibility mode

The External Operator source contains historical compatibility paths in which a particular Hubble adapter sets

\[
\mu_H:=\eta.
\]

Such a path reproduces the historical reduction.

However, the core engine itself explicitly treats

\[
\eta
\]

and

\[
\mu_{\rm eff}
\]

as independent quantities.

Therefore compatibility behavior must not be confused with the general mathematical architecture.

---

# 23. Why the historical adapter is not used here

The corrected GEO-Hubble projection demonstration is intended to test whether the projection factor follows from the canonical geometry without importing the historical radial identification.

Therefore this repository does not use an adapter whose first step is

\[
\mu_H:=\eta.
\]

Instead it works directly with:

\[
A+B=1,
\]

\[
f_c=\sqrt{\eta},
\]

and

\[
Q(\pi/4).
\]

The radial law remains separately available as

\[
R=\mu_{\rm eff}^{1/3}.
\]

---

# 24. Historical radial-defect construction

Some earlier GEO-Hubble material used the quantity

\[
\Delta_R
=
1-R
\]

together with a later observable expression.

If that construction uses

\[
R=\eta^{1/3},
\]

then the numerical result depends on the historical identification

\[
\mu_H=\eta.
\]

Such a result must therefore be labelled as belonging to that historical realization.

It cannot automatically be presented as a consequence of the corrected general radial law.

---

# 25. Status of the later radial-defect operator

The present repository does not assume that a later expression such as

\[
1+\alpha(1-R)
\]

is equivalent to the canonical tangent projection factor

\[
\frac{f_c}{A'}.
\]

Any claimed equivalence between those expressions would require a separate mathematical derivation.

Until such a derivation exists, they are treated as distinct constructions.

This prevents numerical agreement from being mistaken for algebraic equivalence.

---

# 26. Why this separation improves the Hubble derivation

The corrected Hubble derivation obtains

\[
P_{\rm GEO}
=
\sqrt{\frac65}
\]

without using

\[
R=\eta^{1/3}.
\]

Therefore the projection result survives removal of the historical radial identification.

This means the new derivation does not need to rescue or reinterpret the erroneous substitution.

It simply does not use it.

---

# 27. Dependency graph before correction

The historical shorthand could be represented as

\[
\eta
\longrightarrow
f_c
\]

and simultaneously

\[
\eta
\longrightarrow
R.
\]

The second arrow is not part of the general architecture.

---

# 28. Corrected dependency graph

The corrected graph is

\[
\boxed{
\eta
\longrightarrow
f_c=\sqrt{\eta}
}
\]

and separately

\[
\boxed{
\mu_{\rm eff}
\longrightarrow
R=\mu_{\rm eff}^{1/3}.
}
\]

The projection branch is

\[
\boxed{
(\eta,1-\eta,\theta)
\longrightarrow
(A',B').
}
\]

Thus the full structure is

\[
\eta
\rightarrow
\{A,B,f_c\}
\]

\[
(A,B,\theta)
\rightarrow
(A',B')
\]

\[
\mu_{\rm eff}
\rightarrow
R.
\]

No canonical arrow

\[
\eta\rightarrow R
\]

exists.

---

# 29. Corrected Hubble dependency graph

For the projection demonstration,

\[
\eta
\rightarrow
f_c
\]

and

\[
(\eta,1-\eta,\pi/4)
\rightarrow
A'
\]

combine to give

\[
P_{\rm GEO}
=
\frac{f_c}{A'}.
\]

Therefore

\[
\boxed{
P_{\rm GEO}
=
\sqrt{\frac65}.
}
\]

The Hubble application then states

\[
H_{\rm GEO}
=
P_{\rm GEO}H_{\rm base}.
\]

The radial branch is not needed to derive this factor.

---

# 30. Numerical audit table

The following values summarize the corrected radial behavior at fixed

\[
\eta=0.6.
\]

| \(\mu_{\rm eff}\) | \(R=\mu_{\rm eff}^{1/3}\) |
|---:|---:|
| 0.4 | 0.736806299728077 |
| 0.5 | 0.793700525984100 |
| 0.6 | 0.843432665301749 |
| 0.7 | 0.887904001742601 |
| 0.8 | 0.928317766722556 |
| 0.8104 | 0.932323170115423 |
| 0.9 | 0.965489384605630 |
| 1.0 | 1.000000000000000 |

Throughout this sweep,

\[
\eta=0.6
\]

remains fixed.

---

# 31. Projection audit table

For the same sweep, the canonical tangent projection returned

\[
A'
=
0.707106781186547\ldots
\]

for every tested state.

The reconstructed projection ratio remained

\[
P_{\rm GEO}
=
1.095445115010332\ldots
\]

for every tested state.

Thus the numerical evidence is consistent with the analytic dependency graph.

---

# 32. Reproducibility requirement

Every script in this repository that uses the radial law must calculate

\[
R
\]

from

\[
\mu_{\rm eff}.
\]

The implementation must therefore follow

\[
\boxed{
R=\operatorname{cbrt}(\mu_{\rm eff}).
}
\]

A script must not calculate

\[
R=\operatorname{cbrt}(\eta)
\]

unless it is explicitly reproducing and labelling a historical special case.

---

# 33. Regression requirement

The automated test suite must include a regression test satisfying:

1. choose a fixed \(\eta\);
2. select two unequal values of \(\mu_{\rm eff}\);
3. calculate both radial responses;
4. verify both satisfy

\[
R^3=\mu_{\rm eff};
\]

5. verify the radial responses differ.

Thus, for

\[
\mu_1\neq\mu_2,
\]

the test must confirm

\[
R_1\neq R_2.
\]

This prevents accidental reintroduction of

\[
R=\eta^{1/3}.
\]

---

# 34. Documentation requirement

Future GEO-Hubble documentation should distinguish explicitly:

\[
\eta
\]

as canonical architectural efficiency,

\[
f_c
\]

as its coupling amplitude,

\[
\mu_{\rm eff}
\]

as application-specific effective state,

and

\[
R
\]

as the radial response determined from that effective state.

This terminology should remain stable across source code, mathematical documentation, and scientific manuscripts.

---

# 35. Superseded notation statement

The following notation is superseded as a statement of the general radial law:

\[
R=\eta^{1/3}.
\]

The current canonical statement is

\[
\boxed{
R=\mu_{\rm eff}^{1/3}.
}
\]

If the superseded notation is retained for historical documentation, it should be accompanied by an explicit statement that it corresponds to the special reduction

\[
\mu_{\rm eff}:=\eta
\]

and is not the general law.

---

# 36. Correction note suitable for scientific documentation

A concise correction statement may be written as follows:

> Earlier GEO-Hubble material contained the expression \(R=\eta^{1/3}\). The canonical GEO radial law is \(R=\mu_{\rm eff}^{1/3}\), where \(\mu_{\rm eff}\) is an application-specific effective state and is not universally identical to the architectural efficiency \(\eta\). The historical expression should therefore be understood as a special reduction or transcription inherited from an earlier realization, not as the general GEO radial law.

---

# 37. Consequence for the new Hubble demonstration

The corrected GEO-Hubble projection no longer depends on the historical radial substitution.

The projection factor is derived from

\[
A+B=1,
\]

\[
\eta=f_c^2,
\]

and

\[
Q(\pi/4).
\]

This gives

\[
A'
=
\frac1{\sqrt2}
\]

and

\[
f_c
=
\sqrt{\frac35}.
\]

Therefore

\[
\boxed{
P_{\rm GEO}
=
\sqrt{\frac65}.
}
\]

No value of

\[
\mu_{\rm eff}
\]

is required to derive this projection factor.

---

# 38. What remains open

The correction does not answer every possible question about the relationship between the radial, spectral, and observable layers of the full GEO framework.

In particular, a separate study may investigate whether a rigorous relation exists among

\[
R,
\]

\[
\Phi,
\]

\[
\alpha,
\]

and the tangent projection factor.

Such a derivation must be performed independently.

It must not be assumed solely because earlier formulas produced numerically similar Hubble-scale values.

---

# 39. Final corrected formulation

The mathematical distinction may be summarized in two equations:

\[
\boxed{
\eta=f_c^2
}
\]

and

\[
\boxed{
\mu_{\rm eff}=R^3.
}
\]

Equivalently,

\[
\boxed{
f_c=\sqrt{\eta}
}
\]

and

\[
\boxed{
R=\mu_{\rm eff}^{1/3}.
}
\]

These are different maps.

The corrected GEO-Hubble demonstration preserves both without conflating them.

---

# 40. Final statement

The historical notation issue can therefore be isolated cleanly.

The canonical architecture is not being redesigned.

The corrected formulation simply restores the intended separation:

\[
\boxed{
\eta
\neq
\mu_{\rm eff}
}
\]

in general,

with

\[
\boxed{
f_c=\sqrt{\eta}
}
\]

and

\[
\boxed{
R=\mu_{\rm eff}^{1/3}.
}
\]

The new Hubble projection derivation is independent of the historical substitution and is therefore internally consistent with the corrected GEO radial law.
