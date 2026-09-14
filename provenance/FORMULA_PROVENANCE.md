# Formula Provenance Map

## Purpose

This document records the logical and historical status of every formula used in the GEO-Hubble Geometric Projection repository.

Its purpose is to answer, for each relation:

- where it comes from;
- what variables it depends on;
- whether it is a definition, law, algebraic consequence, executable identity, correction, or physical hypothesis;
- whether it participates directly in the Hubble projection derivation;
- whether it has been verified analytically;
- whether it has been verified by the GEO External Operator.

This map is intended to prevent formulas from being silently promoted from:

- historical shorthand to canonical law;
- implementation detail to mathematical axiom;
- mathematical identity to physical claim;
- post hoc numerical agreement to prediction.

---

# 1. Provenance classes

The following provenance classes are used throughout this file.

## O — Original GEO

A relation originating in the earlier GEO Hidden Geometry framework.

## F — GEO Foundations

A relation preserved, clarified, or formalized in the later mathematical architecture.

## E — External Operator

A relation implemented or numerically reproduced by the GEO External Operator.

## C — Corrected notation

A historical relation whose variable assignment or notation requires correction.

## N — New derivation

A relation derived explicitly in the present GEO-Hubble Geometric Projection repository.

## H — Hubble application hypothesis

A physical mapping introduced specifically for the Hubble-scale application.

---

# 2. Formula status categories

Each formula also receives a logical status.

The principal categories are:

- Definition
- Conservation law
- Canonical constant
- Structural law
- Algebraic consequence
- Projection identity
- Executable identity
- Historical notation
- Corrected statement
- Derived theorem
- Physical hypothesis
- Numerical consequence

These categories are distinct from provenance.

---

# 3. Conservation law

Formula:

\[
\boxed{
A+B=1
}
\]

Provenance:

\[
\boxed{
O/F
}
\]

Logical status:

Conservation law.

Dependencies:

None within the reduced conservative architecture.

Meaning:

The active and complementary coordinates form a normalized total.

Used directly in Hubble derivation:

YES.

Analytically verified:

YES.

Executable verification:

YES, through projection and reconstruction closure.

Important consequence:

At the canonical tangent angle,

\[
A'
=
\frac{A+B}{\sqrt2}
=
\frac1{\sqrt2}.
\]

---

# 4. Active-coordinate identification

Formula:

\[
\boxed{
A=\eta
}
\]

Provenance:

\[
\boxed{
O/F
}
\]

Logical status:

Canonical architectural identification.

Dependencies:

\[
\eta.
\]

Used directly in Hubble derivation:

YES.

Meaning:

The active coordinate of the reduced canonical state is identified with the architectural efficiency parameter.

---

# 5. Complementary-coordinate relation

Formula:

\[
\boxed{
B=1-\eta
}
\]

Provenance:

\[
\boxed{
O/F
}
\]

Logical status:

Algebraic consequence.

Derived from:

\[
A+B=1
\]

and

\[
A=\eta.
\]

Used directly in Hubble derivation:

YES.

For the canonical state:

\[
B
=
1-\frac35
=
\frac25.
\]

---

# 6. Canonical efficiency value

Formula:

\[
\boxed{
\eta=\frac35
}
\]

Numerically:

\[
\boxed{
\eta=0.6
}
\]

Provenance:

\[
\boxed{
O/F
}
\]

Logical status:

Canonical architectural constant.

Used directly in Hubble derivation:

YES.

Fitted to Hubble:

NO.

Adjusted using local \(H_0\):

NO.

---

# 7. Quadratic efficiency law

Formula:

\[
\boxed{
\eta=f_c^2
}
\]

Provenance:

\[
\boxed{
O/F
}
\]

Logical status:

Structural law.

Dependencies:

\[
f_c.
\]

Used directly in Hubble derivation:

YES.

Inverse form:

\[
\boxed{
f_c=\sqrt{\eta}.
}
\]

Positive branch used:

YES.

Reason:

\(f_c\) is treated as a positive normalized coupling amplitude.

---

# 8. Canonical coupling amplitude

Formula:

\[
\boxed{
f_c=\sqrt{\frac35}
}
\]

Numerically:

\[
\boxed{
f_c
=
0.774596669241483\ldots
}
\]

Provenance:

\[
\boxed{
O/F
}
\]

Logical status:

Algebraic consequence of the quadratic efficiency law.

Used directly in Hubble derivation:

YES.

Executable verification:

Indirectly yes, through the same canonical input \(\eta\).

---

# 9. Effective-state variable

Symbol:

\[
\boxed{
\mu_{\rm eff}
}
\]

Provenance:

\[
\boxed{
O/F/E
}
\]

Logical status:

Application-specific effective state.

Universal identity with \(\eta\):

NO.

Used directly in corrected Hubble projection proposition:

NO.

Used in radial branch:

YES.

---

# 10. Fundamental radial law

Formula:

\[
\boxed{
R^3=\mu_{\rm eff}
}
\]

Equivalent form:

\[
\boxed{
R=\mu_{\rm eff}^{1/3}.
}
\]

Provenance:

\[
\boxed{
O/F/E
}
\]

Logical status:

Structural law.

Dependencies:

\[
\mu_{\rm eff}.
\]

Used directly in corrected projection proposition:

NO.

Used in broader GEO architecture:

YES.

Executable verification:

YES.

Observed numerical closure:

Approximately machine precision.

---

# 11. Radial inverse relation

Formula:

\[
\boxed{
\mu_{\rm eff}=R^3.
}
\]

Provenance:

\[
\boxed{
O/F/E
}
\]

Logical status:

Algebraic inverse of the radial law.

Used in Hubble projection proposition:

NO.

Used for consistency checks:

YES.

---

# 12. Historical radial shorthand

Formula:

\[
R=\eta^{1/3}.
\]

Provenance:

\[
\boxed{
C
}
\]

Logical status:

Historical notation / special reduction.

General canonical law:

NO.

Equivalent only if:

\[
\mu_{\rm eff}:=\eta.
\]

Used in present derivation:

NO.

Allowed in historical reproduction:

YES, if explicitly labelled.

---

# 13. Corrected radial statement

Formula:

\[
\boxed{
R=\mu_{\rm eff}^{1/3}.
}
\]

Provenance:

\[
\boxed{
C/O/F/E
}
\]

Logical status:

Corrected general statement.

Binding in this repository:

YES.

Any script using:

\[
R=\eta^{1/3}
\]

without explicitly declaring a historical special case:

INVALID.

---

# 14. Canonical tangent angle

Formula:

\[
\boxed{
\theta_0=\frac{\pi}{4}.
}
\]

Equivalent:

\[
\theta_0=45^\circ.
\]

Provenance:

\[
\boxed{
O/F/E
}
\]

Logical status:

Canonical geometric state.

Used directly in Hubble projection proposition:

YES.

Fitted to Hubble data:

NO.

---

# 15. Trigonometric values at the canonical angle

Formula:

\[
\cos\frac{\pi}{4}
=
\sin\frac{\pi}{4}
=
\frac1{\sqrt2}.
\]

Provenance:

Standard mathematics.

Logical status:

Trigonometric identity.

Used directly:

YES.

Numerically:

\[
\frac1{\sqrt2}
=
0.7071067811865475\ldots
\]

---

# 16. Tangent projection matrix

Formula:

\[
\boxed{
Q(\theta)
=
\begin{pmatrix}
\cos\theta & \sin\theta\\
-\sin\theta & \cos\theta
\end{pmatrix}.
}
\]

Provenance:

\[
\boxed{
F/E
}
\]

Logical status:

Projection operator.

Used directly in Hubble theorem:

YES.

Executable implementation:

YES.

---

# 17. Orthogonality identity

Formula:

\[
\boxed{
Q^TQ=I.
}
\]

Provenance:

Standard consequence of \(Q\).

Logical status:

Derived matrix identity.

Used directly in Hubble factor:

NO.

Used for validation:

YES.

Consequence:

\[
Q^{-1}=Q^T.
\]

---

# 18. Norm preservation

Formula:

\[
\boxed{
\|Q\mathbf v\|
=
\|\mathbf v\|.
}
\]

Provenance:

Standard orthogonal-matrix result.

Logical status:

Derived identity.

Executable verification:

YES.

Observed projection norm error:

Approximately

\[
10^{-16}.
\]

---

# 19. Conservative state vector

Formula:

\[
\boxed{
\mathbf v
=
\begin{pmatrix}
A\\
B
\end{pmatrix}.
}
\]

Canonical value:

\[
\boxed{
\mathbf v
=
\begin{pmatrix}
3/5\\
2/5
\end{pmatrix}.
}
\]

Provenance:

\[
\boxed{
F/N
}
\]

Logical status:

Vector representation of the canonical partition.

Used directly:

YES.

---

# 20. Projected state vector

Formula:

\[
\boxed{
\mathbf v'
=
Q(\theta)\mathbf v.
}
\]

Provenance:

\[
\boxed{
F/E
}
\]

Logical status:

Projection definition.

Expanded form:

\[
\boxed{
A'
=
A\cos\theta+B\sin\theta
}
\]

and

\[
\boxed{
B'
=
-A\sin\theta+B\cos\theta.
}
\]

---

# 21. First projected coordinate

Formula:

\[
\boxed{
A'
=
A\cos\theta+B\sin\theta.
}
\]

Provenance:

\[
\boxed{
F/E
}
\]

Logical status:

Matrix-expansion identity.

Used directly in Hubble theorem:

YES.

---

# 22. Second projected coordinate

Formula:

\[
\boxed{
B'
=
-A\sin\theta+B\cos\theta.
}
\]

Provenance:

\[
\boxed{
F/E
}
\]

Logical status:

Matrix-expansion identity.

Used directly in Hubble theorem:

Not in final ratio, but used for full projection closure.

---

# 23. Canonical first-coordinate derivation

At

\[
\theta=\frac{\pi}{4},
\]

the first coordinate is

\[
A'
=
A\frac1{\sqrt2}
+
B\frac1{\sqrt2}.
\]

Therefore

\[
A'
=
\frac{A+B}{\sqrt2}.
\]

Using conservation,

\[
A+B=1,
\]

we obtain

\[
\boxed{
A'
=
\frac1{\sqrt2}.
}
\]

Provenance:

\[
\boxed{
N/E
}
\]

Logical status:

Derived theorem.

Used directly in Hubble projection:

YES.

Executable verification:

YES.

---

# 24. Canonical second-coordinate derivation

At

\[
\theta=\frac{\pi}{4},
\]

\[
B'
=
\frac{B-A}{\sqrt2}.
\]

For

\[
A=\frac35,
\qquad
B=\frac25,
\]

we obtain

\[
B-A
=
-\frac15.
\]

Therefore

\[
\boxed{
B'
=
-\frac1{5\sqrt2}.
}
\]

Numerically:

\[
\boxed{
B'
=
-0.141421356237309\ldots
}
\]

Provenance:

\[
\boxed{
N/E
}
\]

Logical status:

Derived coordinate.

Executable verification:

YES.

---

# 25. Canonical engine projection

External Operator output:

\[
A'_{\rm engine}
=
0.7071067811865475.
\]

External Operator output:

\[
B'_{\rm engine}
=
-0.1414213562373094.
\]

Provenance:

\[
\boxed{
E
}
\]

Logical status:

Executable result.

Analytic agreement:

YES.

---

# 26. Analytic / engine projection error

Formula:

\[
\Delta A'
=
A'_{\rm analytic}
-
A'_{\rm engine}.
\]

Observed:

\[
\boxed{
\Delta A'=0
}
\]

at displayed precision.

Likewise:

\[
\boxed{
\Delta B'=0
}
\]

at displayed precision.

Provenance:

\[
\boxed{
E
}
\]

Logical status:

Validation diagnostic.

---

# 27. Canonical projection-ratio definition

Formula:

\[
\boxed{
P_{\rm GEO}
=
\frac{f_c}{A'}.
}
\]

Provenance:

\[
\boxed{
N
}
\]

Logical status:

Definition introduced by the present repository to isolate the canonical transfer/projection ratio.

Dependencies:

\[
f_c,
\]

\[
A'.
\]

Hubble data required:

NO.

Radial state required:

NO.

---

# 28. Closed-form projection ratio

Substitute

\[
f_c=\sqrt{\frac35}
\]

and

\[
A'=\frac1{\sqrt2}.
\]

Then

\[
P_{\rm GEO}
=
\frac{\sqrt{3/5}}
{1/\sqrt2}.
\]

Therefore

\[
P_{\rm GEO}
=
\sqrt{\frac35}\sqrt2.
\]

Thus

\[
\boxed{
P_{\rm GEO}
=
\sqrt{\frac65}.
}
\]

Provenance:

\[
\boxed{
N
}
\]

Logical status:

Derived theorem.

Central result:

YES.

---

# 29. Numerical projection ratio

Formula:

\[
P_{\rm GEO}
=
\sqrt{\frac65}.
\]

Numerically:

\[
\boxed{
P_{\rm GEO}
=
1.095445115010332\ldots
}
\]

Provenance:

\[
\boxed{
N/E
}
\]

Logical status:

Numerical evaluation of the theorem.

Executable agreement:

YES.

---

# 30. Engine reconstruction of the factor

Formula:

\[
\boxed{
P_{\rm engine}
=
\frac{
\sqrt{\eta}
}{
A'_{\rm engine}
}.
}
\]

Observed:

\[
\boxed{
P_{\rm engine}
=
1.095445115010332.
}
\]

Difference from closed form:

\[
\boxed{
|P_{\rm engine}-\sqrt{6/5}|
\approx
2.22\times10^{-16}.
}
\]

Provenance:

\[
\boxed{
E
}
\]

Logical status:

Executable validation.

---

# 31. General balanced-angle factor

At

\[
\theta=\frac{\pi}{4},
\]

the first coordinate is

\[
A'=\frac1{\sqrt2}
\]

for any conservative pair.

Since

\[
f_c=\sqrt{\eta},
\]

the general balanced-angle factor is

\[
\boxed{
P(\eta)
=
\sqrt{2\eta}.
}
\]

Provenance:

\[
\boxed{
N
}
\]

Logical status:

Generalized analytic result.

Canonical evaluation:

\[
P\left(\frac35\right)
=
\sqrt{\frac65}.
\]

---

# 32. General angle-dependent factor

For arbitrary \(\theta\),

\[
A'(\eta,\theta)
=
\eta\cos\theta
+
(1-\eta)\sin\theta.
\]

Therefore

\[
\boxed{
P(\eta,\theta)
=
\frac{
\sqrt{\eta}
}{
\eta\cos\theta
+
(1-\eta)\sin\theta
}.
}
\]

Provenance:

\[
\boxed{
N
}
\]

Logical status:

Generalized projection formula.

Used to fit Hubble:

NO.

Canonical evaluation only:

YES.

---

# 33. Independence from \(\mu_{\rm eff}\)

Since

\[
P_{\rm GEO}
=
\frac{f_c}{A'},
\]

and neither factor contains

\[
\mu_{\rm eff},
\]

we obtain

\[
\boxed{
\frac{\partial P_{\rm GEO}}
{\partial\mu_{\rm eff}}
=
0.
}
\]

Provenance:

\[
\boxed{
N
}
\]

Logical status:

Dependency result.

Executable verification:

YES, through sweep.

---

# 34. Radial sweep

Input set:

\[
\mu_{\rm eff}
\in
\{
0.4,
0.5,
0.6,
0.7,
0.8,
0.8104,
0.9,
1.0
\}.
\]

Observed:

\[
R
\]

changes.

Observed:

\[
\Phi
\]

changes.

Observed:

\[
\alpha
\]

changes.

Observed:

\[
A'
\]

does not change.

Observed:

\[
P_{\rm GEO}
\]

does not change.

Provenance:

\[
\boxed{
E
}
\]

Logical status:

Numerical dependency audit.

---

# 35. Projection-factor span

Formula:

\[
\Delta P
=
P_{\rm max}
-
P_{\rm min}.
\]

Observed:

\[
\boxed{
\Delta P=0
}
\]

at displayed precision.

Provenance:

\[
\boxed{
E
}
\]

Logical status:

Invariance diagnostic.

---

# 36. Projected-coordinate span

Formula:

\[
\Delta A'
=
A'_{\rm max}
-
A'_{\rm min}.
\]

Observed:

\[
\boxed{
\Delta A'=0
}
\]

at displayed precision.

Provenance:

\[
\boxed{
E
}
\]

Logical status:

Invariance diagnostic.

---

# 37. Spectral radius

Symbol:

\[
\boxed{
\Phi
}
\]

Provenance:

\[
\boxed{
F/E
}
\]

Logical status:

Spectral quantity of the broader GEO operator chain.

Used in corrected projection proposition:

NO.

Changes with \(\mu_{\rm eff}\):

YES.

Retained as part of broader GEO:

YES.

---

# 38. Spectral coefficient

Formula:

\[
\boxed{
\alpha
=
\frac{\Phi B}{\sqrt2}
}
\]

Provenance:

\[
\boxed{
F/E
}
\]

Logical status:

Derived spectral quantity.

Used in corrected projection proposition:

NO.

Changes with \(\mu_{\rm eff}\):

YES.

---

# 39. Historical radial-defect expression

Representative form:

\[
1+\alpha(1-R).
\]

Provenance:

Historical later GEO-Hubble construction.

Logical status:

Separate construction.

Assumed equivalent to

\[
P_{\rm GEO}
\]

in this repository:

NO.

Reason:

No algebraic equivalence has yet been demonstrated under the corrected radial law.

---

# 40. Hubble application ratio

Formula:

\[
\boxed{
\frac{
H_{\rm GEO}
}{
H_{\rm base}
}
=
P_{\rm GEO}.
}
\]

Provenance:

\[
\boxed{
H
}
\]

Logical status:

Physical application hypothesis.

Internal mathematical proposition:

NO.

Testable physical statement:

YES.

---

# 41. GEO-Hubble projected relation

Substitute

\[
P_{\rm GEO}
=
\sqrt{\frac65}.
\]

Then

\[
\boxed{
H_{\rm GEO}
=
H_{\rm base}
\sqrt{\frac65}.
}
\]

Provenance:

\[
\boxed{
N/H
}
\]

Logical status:

Consequence of the Hubble application hypothesis.

---

# 42. Reference baseline

Formula:

\[
\boxed{
H_{\rm base}
=
67.40\ {\rm km\,s^{-1}\,Mpc^{-1}}
}
\]

Provenance:

External cosmological input.

Logical status:

Reference numerical input.

Derived by GEO:

NO.

Used to determine GEO architecture:

NO.

---

# 43. Reference projected Hubble output

Formula:

\[
H_{\rm GEO}
=
67.40
\sqrt{\frac65}.
\]

Numerically:

\[
\boxed{
H_{\rm GEO}
=
73.833000751696
\ {\rm km\,s^{-1}\,Mpc^{-1}}.
}
\]

Provenance:

\[
\boxed{
N/H
}
\]

Logical status:

Numerical consequence.

Used as fitting target:

NO.

---

# 44. Relative Hubble shift

Formula:

\[
\delta_H
=
\frac{
H_{\rm GEO}-H_{\rm base}
}{
H_{\rm base}
}.
\]

Since

\[
H_{\rm GEO}
=
P_{\rm GEO}H_{\rm base},
\]

we obtain

\[
\boxed{
\delta_H
=
P_{\rm GEO}-1.
}
\]

Therefore

\[
\boxed{
\delta_H
=
\sqrt{\frac65}-1.
}
\]

Numerically:

\[
\boxed{
\delta_H
\approx
0.095445115010332.
}
\]

Equivalent percentage:

Approximately

\[
9.5445\%.
\]

Provenance:

\[
\boxed{
N/H
}
\]

---

# 45. Inverse Hubble mapping

From

\[
H_{\rm GEO}
=
P_{\rm GEO}H_{\rm base},
\]

we obtain

\[
H_{\rm base}
=
\frac{
H_{\rm GEO}
}{
P_{\rm GEO}
}.
\]

Thus

\[
\boxed{
H_{\rm base}
=
H_{\rm GEO}
\sqrt{\frac56}.
}
\]

Provenance:

\[
\boxed{
N/H
}
\]

Logical status:

Algebraic inverse.

---

# 46. Observed-ratio diagnostic

Define

\[
\boxed{
\mathcal R_{\rm obs}
=
\frac{
H_{\rm high}
}{
H_{\rm base}
}.
}
\]

Provenance:

Standard empirical diagnostic.

The GEO prediction is

\[
\boxed{
\mathcal R_{\rm GEO}
=
\sqrt{\frac65}.
}
\]

Residual:

\[
\boxed{
\Delta_{\mathcal R}
=
\mathcal R_{\rm obs}
-
\sqrt{\frac65}.
}
\]

Logical status:

Physical comparison diagnostic.

---

# 47. Simplified standardized residual

For independent Gaussian uncertainties,

\[
H_{\rm base}\pm\sigma_b
\]

and

\[
H_{\rm high}\pm\sigma_h,
\]

the projected prediction is

\[
H_{\rm pred}
=
P_{\rm GEO}H_{\rm base}.
\]

Its propagated uncertainty is

\[
\sigma_{\rm pred}
=
P_{\rm GEO}\sigma_b.
\]

Then

\[
\boxed{
Z_{\rm GEO}
=
\frac{
H_{\rm high}
-
P_{\rm GEO}H_{\rm base}
}{
\sqrt{
\sigma_h^2
+
P_{\rm GEO}^2\sigma_b^2
}
}.
}
\]

Provenance:

\[
\boxed{
N/H
}
\]

Logical status:

Simplified empirical diagnostic.

Full cosmological likelihood substitute:

NO.

---

# 48. Formula dependency tree

The central mathematical dependency tree is:

\[
\eta=\frac35
\]

which gives

\[
A=\eta
\]

and

\[
B=1-\eta.
\]

Independently,

\[
\eta=f_c^2
\]

gives

\[
f_c=\sqrt{\eta}.
\]

Then

\[
Q(\pi/4)
\]

acts on

\[
(A,B).
\]

This gives

\[
A'=\frac1{\sqrt2}.
\]

Then

\[
P_{\rm GEO}
=
\frac{f_c}{A'}.
\]

Therefore

\[
P_{\rm GEO}
=
\sqrt{\frac65}.
\]

Only after this result is frozen does the physical Hubble mapping enter:

\[
H_{\rm GEO}
=
P_{\rm GEO}H_{\rm base}.
\]

Separately,

\[
\mu_{\rm eff}
\rightarrow
R=\mu_{\rm eff}^{1/3}.
\]

---

# 49. Formula dependency exclusions

The following arrows are not part of the corrected canonical proof:

\[
\eta
\not\rightarrow
R
\]

unless a separate application explicitly derives

\[
\mu_{\rm eff}=\eta.
\]

Likewise,

\[
R
\not\rightarrow
P_{\rm GEO}
\]

in the present proof.

Also,

\[
\Phi
\not\rightarrow
P_{\rm GEO}
\]

and

\[
\alpha
\not\rightarrow
P_{\rm GEO}
\]

in the present proof.

This does not deny broader relations elsewhere in GEO.

It defines only the minimal dependency chain required here.

---

# 50. Formula-level claim boundary

The following are internal mathematical statements:

\[
A+B=1,
\]

\[
\eta=f_c^2,
\]

\[
R=\mu_{\rm eff}^{1/3},
\]

\[
Q^TQ=I,
\]

\[
A'=\frac1{\sqrt2},
\]

\[
P_{\rm GEO}
=
\sqrt{\frac65}.
\]

The following is a physical hypothesis:

\[
\frac{
H_{\rm GEO}
}{
H_{\rm base}
}
=
P_{\rm GEO}.
\]

The following is a numerical consequence of that hypothesis:

\[
H_{\rm GEO}
=
73.833000751696
\]

when

\[
H_{\rm base}=67.40.
\]

These levels must remain separated.

---

# 51. Formula provenance summary table

| Formula | Class | Logical role | Hubble proof |
|---|---|---|---|
| \(A+B=1\) | O/F | conservation | required |
| \(A=\eta\) | O/F | canonical identification | required |
| \(B=1-\eta\) | O/F | consequence | required |
| \(\eta=3/5\) | O/F | canonical value | required |
| \(\eta=f_c^2\) | O/F | efficiency law | required |
| \(f_c=\sqrt{\eta}\) | O/F | consequence | required |
| \(R=\mu_{\rm eff}^{1/3}\) | O/F/E | radial law | preserved, not required |
| \(R=\eta^{1/3}\) | C | historical reduction | excluded |
| \(\theta=\pi/4\) | O/F/E | canonical angle | required |
| \(Q(\theta)\) | F/E | tangent operator | required |
| \(Q^TQ=I\) | F/E | orthogonality | validation |
| \(A'=A\cos\theta+B\sin\theta\) | F/E | projection | required |
| \(B'=-A\sin\theta+B\cos\theta\) | F/E | projection | validation |
| \(A'=1/\sqrt2\) | N/E | theorem | required |
| \(B'=-1/(5\sqrt2)\) | N/E | consequence | validation |
| \(P_{\rm GEO}=f_c/A'\) | N | ratio definition | required |
| \(P_{\rm GEO}=\sqrt{6/5}\) | N/E | theorem | central |
| \(H_{\rm GEO}/H_{\rm base}=P_{\rm GEO}\) | H | physical hypothesis | application |
| \(H_{\rm GEO}=H_{\rm base}\sqrt{6/5}\) | N/H | consequence | application |

---

# 52. Binding provenance rule

A formula must never be described as:

- original GEO;
- externally validated;
- physically demonstrated;
- observationally confirmed;

unless the corresponding provenance class and validation level support that description.

The required wording is:

- inherited;
- derived;
- implemented;
- reproduced;
- hypothesized;
- empirically compared;

according to the actual status.

---

# 53. Final provenance statement

The corrected GEO-Hubble construction rests on three layers.

First, inherited GEO mathematics:

\[
A+B=1,
\]

\[
\eta=\frac35,
\]

\[
\eta=f_c^2,
\]

\[
R=\mu_{\rm eff}^{1/3},
\]

and

\[
Q(\pi/4).
\]

Second, the present formal derivation:

\[
A'
=
\frac1{\sqrt2}
\]

and

\[
P_{\rm GEO}
=
\sqrt{\frac65}.
\]

Third, the physical application hypothesis:

\[
\frac{
H_{\rm GEO}
}{
H_{\rm base}
}
=
P_{\rm GEO}.
\]

This separation defines the formula provenance of the GEO-Hubble Geometric Projection repository.
