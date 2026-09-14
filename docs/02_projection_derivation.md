# 02 — Formal Derivation of the Canonical GEO Projection

## Purpose

This document gives the complete mathematical derivation of the canonical GEO projection used in the Hubble demonstration.

The objective is to derive, step by step,

\[
\boxed{
P_{\rm GEO}
=
\sqrt{\frac65}
}
\]

starting only from the canonical GEO architecture:

\[
A+B=1,
\]

\[
A=\eta,
\]

\[
\eta=\frac35,
\]

\[
\eta=f_c^2,
\]

and the canonical tangent operator

\[
Q\left(\frac{\pi}{4}\right).
\]

No Hubble-scale measurement enters this derivation.

No local value of \(H_0\) is used.

No assumption

\[
\mu_{\rm eff}=\eta
\]

is required.

The radial law

\[
R=\mu_{\rm eff}^{1/3}
\]

remains mathematically valid and independent of the projection derivation.

---

# 1. Starting conservative state

The reduced conservative GEO architecture satisfies

\[
\boxed{
A+B=1.
}
\]

The canonical active component is

\[
\boxed{
A=\eta.
}
\]

For the canonical GEO value

\[
\boxed{
\eta=\frac35,
}
\]

we obtain

\[
A=\frac35.
\]

Therefore

\[
B
=
1-A
=
1-\frac35
=
\frac25.
\]

Hence

\[
\boxed{
\mathbf v
=
\begin{pmatrix}
A\\
B
\end{pmatrix}
=
\begin{pmatrix}
3/5\\
2/5
\end{pmatrix}.
}
\]

Numerically,

\[
\mathbf v
=
\begin{pmatrix}
0.6\\
0.4
\end{pmatrix}.
\]

---

# 2. Canonical coupling amplitude

The quadratic GEO relation is

\[
\boxed{
\eta=f_c^2.
}
\]

Solving for the positive normalized amplitude,

\[
f_c
=
\sqrt{\eta}.
\]

With

\[
\eta=\frac35,
\]

we obtain

\[
\boxed{
f_c
=
\sqrt{\frac35}.
}
\]

Numerically,

\[
\boxed{
f_c
=
0.774596669241483\ldots
}
\]

This quantity will later form the numerator of the canonical projection ratio.

---

# 3. Tangent transformation

The canonical tangent/membrane transformation is the orthogonal matrix

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

The projected state is defined by

\[
\boxed{
\mathbf v'
=
Q(\theta)\mathbf v.
}
\]

Explicitly,

\[
\begin{pmatrix}
A'\\
B'
\end{pmatrix}
=
\begin{pmatrix}
\cos\theta & \sin\theta\\
-\sin\theta & \cos\theta
\end{pmatrix}
\begin{pmatrix}
A\\
B
\end{pmatrix}.
\]

Therefore,

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

# 4. Orthogonality of the tangent operator

Let

\[
c=\cos\theta,
\qquad
s=\sin\theta.
\]

Then

\[
Q
=
\begin{pmatrix}
c&s\\
-s&c
\end{pmatrix}.
\]

Its transpose is

\[
Q^T
=
\begin{pmatrix}
c&-s\\
s&c
\end{pmatrix}.
\]

Multiply:

\[
Q^TQ
=
\begin{pmatrix}
c&-s\\
s&c
\end{pmatrix}
\begin{pmatrix}
c&s\\
-s&c
\end{pmatrix}.
\]

The result is

\[
Q^TQ
=
\begin{pmatrix}
c^2+s^2 & cs-cs\\
sc-sc & s^2+c^2
\end{pmatrix}.
\]

Using the trigonometric identity

\[
c^2+s^2=1,
\]

we obtain

\[
\boxed{
Q^TQ=I.
}
\]

Therefore the transformation is orthogonal.

---

# 5. Consequence: norm preservation

For

\[
\mathbf v'
=
Q\mathbf v,
\]

we have

\[
\|\mathbf v'\|^2
=
\mathbf v'^T\mathbf v'.
\]

Substituting,

\[
\|\mathbf v'\|^2
=
\mathbf v^TQ^TQ\mathbf v.
\]

Since

\[
Q^TQ=I,
\]

it follows that

\[
\|\mathbf v'\|^2
=
\mathbf v^T\mathbf v.
\]

Therefore

\[
\boxed{
\|\mathbf v'\|
=
\|\mathbf v\|.
}
\]

The tangent transformation reorganizes the conservative state without changing its Euclidean norm.

---

# 6. Canonical balanced angle

The canonical balanced GEO orientation is

\[
\boxed{
\theta_0=\frac{\pi}{4}.
}
\]

Thus,

\[
\cos\theta_0
=
\sin\theta_0
=
\frac1{\sqrt2}.
\]

Hence

\[
Q\left(\frac{\pi}{4}\right)
=
\frac1{\sqrt2}
\begin{pmatrix}
1&1\\
-1&1
\end{pmatrix}.
\]

---

# 7. First projected coordinate

The observable-side projected coordinate is

\[
A'
=
A\cos\theta+B\sin\theta.
\]

At

\[
\theta=\frac{\pi}{4},
\]

this becomes

\[
A'
=
A\frac1{\sqrt2}
+
B\frac1{\sqrt2}.
\]

Factorizing,

\[
A'
=
\frac{A+B}{\sqrt2}.
\]

Using

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

Numerically,

\[
\boxed{
A'
=
0.7071067811865475\ldots
}
\]

This is one of the central results of the projection derivation.

---

# 8. Important independence from the canonical partition split

The expression

\[
A'
=
\frac{A+B}{\sqrt2}
\]

depends only on the sum

\[
A+B.
\]

Since

\[
A+B=1,
\]

the value

\[
A'=\frac1{\sqrt2}
\]

does not depend on the individual split between \(A\) and \(B\), provided the conservative condition remains satisfied.

Therefore, at the canonical balanced angle,

\[
\boxed{
A'
=
\frac1{\sqrt2}
}
\]

is a consequence of conservation and projection symmetry.

---

# 9. Second projected coordinate

The complementary projected coordinate is

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
B'
=
-\frac{A}{\sqrt2}
+
\frac{B}{\sqrt2}.
\]

Thus,

\[
\boxed{
B'
=
\frac{B-A}{\sqrt2}.
}
\]

For the canonical partition

\[
A=\frac35,
\qquad
B=\frac25,
\]

we have

\[
B-A
=
-\frac15.
\]

Therefore,

\[
B'
=
-\frac1{5\sqrt2}.
\]

Numerically,

\[
\boxed{
B'
=
-0.1414213562373095\ldots
}
\]

---

# 10. Full projected vector

The canonical projected state is therefore

\[
\boxed{
\mathbf v'
=
\begin{pmatrix}
1/\sqrt2\\[4pt]
-1/(5\sqrt2)
\end{pmatrix}.
}
\]

Numerically,

\[
\mathbf v'
=
\begin{pmatrix}
0.7071067811865475\\
-0.1414213562373095
\end{pmatrix}.
\]

---

# 11. Direct matrix derivation

The same result follows directly from matrix multiplication.

Start with

\[
Q\left(\frac{\pi}{4}\right)
=
\frac1{\sqrt2}
\begin{pmatrix}
1&1\\
-1&1
\end{pmatrix}.
\]

Apply it to

\[
\mathbf v
=
\begin{pmatrix}
3/5\\
2/5
\end{pmatrix}.
\]

Then

\[
\mathbf v'
=
\frac1{\sqrt2}
\begin{pmatrix}
1&1\\
-1&1
\end{pmatrix}
\begin{pmatrix}
3/5\\
2/5
\end{pmatrix}.
\]

For the first coordinate,

\[
A'
=
\frac1{\sqrt2}
\left(
\frac35+\frac25
\right).
\]

Therefore

\[
A'
=
\frac1{\sqrt2}.
\]

For the second coordinate,

\[
B'
=
\frac1{\sqrt2}
\left(
-\frac35+\frac25
\right).
\]

Therefore

\[
B'
=
-\frac1{5\sqrt2}.
\]

Thus,

\[
\boxed{
Q\left(\frac{\pi}{4}\right)
\begin{pmatrix}
3/5\\
2/5
\end{pmatrix}
=
\begin{pmatrix}
1/\sqrt2\\
-1/(5\sqrt2)
\end{pmatrix}.
}
\]

---

# 12. Reconstruction

Since \(Q\) is orthogonal,

\[
Q^{-1}=Q^T.
\]

Therefore,

\[
\boxed{
\mathbf v
=
Q^T\mathbf v'.
}
\]

This means the projected coordinates retain enough information to reconstruct the original conservative pair.

Explicitly,

\[
\begin{pmatrix}
A\\
B
\end{pmatrix}
=
Q^T
\begin{pmatrix}
A'\\
B'
\end{pmatrix}.
\]

For

\[
\theta=\frac{\pi}{4},
\]

the inverse is

\[
Q^T
=
\frac1{\sqrt2}
\begin{pmatrix}
1&-1\\
1&1
\end{pmatrix}.
\]

Substitution returns

\[
\boxed{
A=\frac35,
\qquad
B=\frac25.
}
\]

---

# 13. External Operator confirmation

The GEO External Operator returns, for the canonical architecture,

\[
\boxed{
A'_{\rm engine}
=
0.7071067811865475
}
\]

and

\[
\boxed{
B'_{\rm engine}
=
-0.1414213562373094.
}
\]

The independent analytic calculation gives

\[
A'_{\rm analytic}
=
0.7071067811865475
\]

and

\[
B'_{\rm analytic}
=
-0.1414213562373095.
\]

At the displayed precision,

\[
\boxed{
|A'_{\rm analytic}-A'_{\rm engine}|=0
}
\]

and

\[
\boxed{
|B'_{\rm analytic}-B'_{\rm engine}|=0.
}
\]

The projection is therefore separately reproduced by the executable implementation.

---

# 14. Projection norm audit

The External Operator also evaluates the norm of the state before and after projection.

Because \(Q\) is orthogonal, the expected identity is

\[
\|\mathbf v'\|
=
\|\mathbf v\|.
\]

The observed projection norm error is approximately

\[
1.11\times10^{-16}.
\]

This is consistent with floating-point machine precision.

Thus the engine confirms the analytic norm-preserving property of the tangent projection.

---

# 15. Canonical projection ratio

The canonical coupling amplitude is

\[
f_c
=
\sqrt{\frac35}.
\]

The canonical observable-side projected coordinate is

\[
A'
=
\frac1{\sqrt2}.
\]

Define

\[
\boxed{
P_{\rm GEO}
=
\frac{f_c}{A'}.
}
\]

Substituting,

\[
P_{\rm GEO}
=
\frac{\sqrt{3/5}}
{1/\sqrt2}.
\]

Multiply numerator and denominator appropriately:

\[
P_{\rm GEO}
=
\sqrt{\frac35}\sqrt2.
\]

Therefore

\[
P_{\rm GEO}
=
\sqrt{\frac65}.
\]

Hence

\[
\boxed{
P_{\rm GEO}
=
\sqrt{\frac65}.
}
\]

Numerically,

\[
\boxed{
P_{\rm GEO}
=
1.095445115010332\ldots
}
\]

---

# 16. Closed-form verification

The engine-based reconstruction gives

\[
P_{\rm engine}
=
1.095445115010332.
\]

The analytic closed form gives

\[
P_{\rm analytic}
=
\sqrt{\frac65}
=
1.095445115010332.
\]

The numerical difference is

\[
\boxed{
|P_{\rm engine}-P_{\rm analytic}|
\approx
2.22\times10^{-16}.
}
\]

This difference is consistent with standard double-precision floating-point rounding.

---

# 17. Why the result is not fitted

The derivation uses only

\[
A+B=1,
\]

\[
A=\eta,
\]

\[
\eta=\frac35,
\]

\[
\eta=f_c^2,
\]

and

\[
\theta=\frac{\pi}{4}.
\]

No Hubble measurement appears.

Therefore

\[
\boxed{
P_{\rm GEO}
=
\sqrt{\frac65}
}
\]

is derived before any cosmological comparison is made.

---

# 18. Independence from the radial state

The radial branch is

\[
\boxed{
R=\mu_{\rm eff}^{1/3}.
}
\]

The projection ratio is

\[
\boxed{
P_{\rm GEO}
=
\frac{f_c}{A'}.
}
\]

The numerator depends on

\[
\eta,
\]

while the denominator depends on

\[
A+B
\]

and

\[
\theta.
\]

No term contains

\[
\mu_{\rm eff}.
\]

Therefore,

\[
\boxed{
\frac{\partial P_{\rm GEO}}
{\partial\mu_{\rm eff}}
=
0.
}
\]

This is an algebraic result.

---

# 19. Numerical independence sweep

The External Operator was evaluated with

\[
\eta=0.6
\]

held fixed and

\[
\mu_{\rm eff}
\]

varied over the set

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

The radial response changed as expected.

Examples:

\[
\mu_{\rm eff}=0.4
\Rightarrow
R=0.736806299728077\ldots
\]

\[
\mu_{\rm eff}=0.6
\Rightarrow
R=0.843432665301749\ldots
\]

\[
\mu_{\rm eff}=0.8104
\Rightarrow
R=0.932323170115423\ldots
\]

\[
\mu_{\rm eff}=1
\Rightarrow
R=1.
\]

However, for every tested value,

\[
A'
=
0.707106781186547\ldots
\]

and

\[
P_{\rm GEO}
=
1.095445115010332\ldots
\]

remained unchanged.

The measured numerical spans were

\[
\boxed{
\Delta A'=0
}
\]

and

\[
\boxed{
\Delta P_{\rm GEO}=0
}
\]

at the displayed precision.

---

# 20. Meaning of the invariance test

The sweep verifies that the canonical projection factor belongs to the projection architecture, not to the selected radial state.

The numerical experiment therefore supports the analytic dependency separation

\[
\mu_{\rm eff}
\rightarrow
R
\]

and

\[
(\eta,\theta)
\rightarrow
P_{\rm GEO}.
\]

This is particularly important because a historical Hubble construction used

\[
\mu_{\rm eff}:=\eta.
\]

The present derivation does not require that reduction.

---

# 21. General balanced-angle identity

For any conservative pair satisfying

\[
A+B=1,
\]

the first coordinate after a \(45^\circ\) tangent transformation is

\[
A'
=
A\frac1{\sqrt2}
+
B\frac1{\sqrt2}.
\]

Thus,

\[
A'
=
\frac{A+B}{\sqrt2}.
\]

Therefore,

\[
\boxed{
A'=\frac1{\sqrt2}
}
\]

for every conservative pair at this balanced angle.

This means the first-coordinate result is structurally stronger than the particular numerical partition

\[
A=0.6,
\qquad
B=0.4.
\]

The canonical value

\[
\eta=\frac35
\]

enters the final ratio through

\[
f_c=\sqrt{\eta},
\]

not through the derivation of \(A'\).

---

# 22. General projection ratio as a function of \(\eta\)

Since

\[
A'
=
\frac1{\sqrt2}
\]

at the balanced angle, while

\[
f_c=\sqrt{\eta},
\]

the general balanced-angle ratio is

\[
P(\eta)
=
\frac{\sqrt{\eta}}
{1/\sqrt2}.
\]

Hence

\[
\boxed{
P(\eta)
=
\sqrt{2\eta}.
}
\]

For the canonical GEO value

\[
\eta=\frac35,
\]

we recover

\[
P\left(\frac35\right)
=
\sqrt{
2\frac35
}
\]

and therefore

\[
\boxed{
P_{\rm GEO}
=
\sqrt{\frac65}.
}
\]

This is a useful analytic generalization.

---

# 23. Sensitivity to \(\eta\)

From

\[
P(\eta)=\sqrt{2\eta},
\]

we obtain

\[
\frac{dP}{d\eta}
=
\frac{1}{\sqrt{2\eta}}.
\]

At

\[
\eta=\frac35,
\]

this becomes

\[
\frac{dP}{d\eta}
=
\frac1{\sqrt{6/5}}.
\]

Therefore,

\[
\boxed{
\left.
\frac{dP}{d\eta}
\right|_{\eta=3/5}
=
\sqrt{\frac56}.
}
\]

This derivative characterizes how the projection ratio would change if the canonical architectural efficiency were changed.

In the present demonstration, however,

\[
\eta=\frac35
\]

is frozen and not fitted.

---

# 24. Sensitivity to the projection angle

For a general angle,

\[
A'(\theta)
=
A\cos\theta+B\sin\theta.
\]

The corresponding ratio is

\[
P(\theta)
=
\frac{f_c}
{A\cos\theta+B\sin\theta}.
\]

Differentiating,

\[
\frac{dP}{d\theta}
=
-f_c
\frac{
-A\sin\theta+B\cos\theta
}{
\left(
A\cos\theta+B\sin\theta
\right)^2
}.
\]

At

\[
\theta=\frac{\pi}{4},
\]

the numerator contains

\[
-A\frac1{\sqrt2}
+
B\frac1{\sqrt2}
=
\frac{B-A}{\sqrt2}.
\]

Thus,

\[
\left.
\frac{dP}{d\theta}
\right|_{\pi/4}
=
-f_c
\frac{
(B-A)/\sqrt2
}{
(1/\sqrt2)^2
}.
\]

Since

\[
(1/\sqrt2)^2=\frac12,
\]

we obtain

\[
\left.
\frac{dP}{d\theta}
\right|_{\pi/4}
=
-\sqrt2\,f_c(B-A).
\]

For

\[
A=\frac35,
\qquad
B=\frac25,
\]

we have

\[
B-A=-\frac15.
\]

Therefore,

\[
\boxed{
\left.
\frac{dP}{d\theta}
\right|_{\pi/4}
=
\frac{\sqrt2}{5}f_c.
}
\]

This result is not used to tune the canonical angle.

It simply characterizes local angular sensitivity.

---

# 25. Why \(\pi/4\) is mathematically special

At

\[
\theta=\frac{\pi}{4},
\]

we have

\[
\cos\theta=\sin\theta.
\]

Therefore the first projected coordinate becomes proportional to the conserved sum

\[
A+B.
\]

Specifically,

\[
A'
=
(A+B)\frac1{\sqrt2}.
\]

This is why the conservation relation collapses the first coordinate to the exact constant

\[
\frac1{\sqrt2}.
\]

Thus the canonical angle is special because it converts the first projected coordinate into a direct readout of the conserved total.

---

# 26. No use of the radial law in the projection proposition

The radial law

\[
R=\mu_{\rm eff}^{1/3}
\]

does not appear anywhere in the derivation

\[
(A,B)
\rightarrow
Q(\pi/4)
\rightarrow
A'
\rightarrow
P_{\rm GEO}.
\]

This is deliberate.

The projection proposition establishes a result about the conservative tangent layer.

The radial law establishes a result about an effective-state response.

The two may coexist in the full GEO architecture without being algebraically identified.

---

# 27. Why the historical substitution is unnecessary here

Suppose one imposed

\[
\mu_{\rm eff}=\eta.
\]

Then

\[
R=\eta^{1/3}.
\]

However, none of the following steps requires \(R\):

\[
A+B=1,
\]

\[
f_c=\sqrt{\eta},
\]

\[
Q(\pi/4),
\]

\[
A'=\frac1{\sqrt2},
\]

\[
P_{\rm GEO}
=
\frac{f_c}{A'}.
\]

Therefore the historical substitution does not contribute to the canonical projection proposition.

The corrected derivation simply omits it.

---

# 28. Mathematical statement established by this document

The result established here is:

\[
\boxed{
A+B=1,
\quad
A=\eta,
\quad
\eta=\frac35,
\quad
f_c=\sqrt{\eta},
\quad
\theta=\frac{\pi}{4}
}
\]

imply

\[
\boxed{
A'=\frac1{\sqrt2}
}
\]

and therefore

\[
\boxed{
P_{\rm GEO}
=
\frac{f_c}{A'}
=
\sqrt{\frac65}.
}
\]

This result is:

- analytic;
- closed-form;
- independent of \(\mu_{\rm eff}\);
- reproduced by the GEO External Operator;
- independent of any local Hubble target.

---

# 29. What remains outside this theorem

This document does not yet assert

\[
\frac{H_{\rm local}}
{H_{\rm base}}
=
P_{\rm GEO}.
\]

That is the physical application hypothesis.

It will be treated separately in

`03_hubble_hypothesis.md`.

Keeping that hypothesis separate ensures that the mathematical theorem remains valid regardless of whether the cosmological interpretation is ultimately supported by data.

---

# 30. Final derivation summary

The canonical conservative state is

\[
\mathbf v
=
\begin{pmatrix}
3/5\\
2/5
\end{pmatrix}.
\]

The canonical tangent transformation is

\[
Q\left(\frac{\pi}{4}\right)
=
\frac1{\sqrt2}
\begin{pmatrix}
1&1\\
-1&1
\end{pmatrix}.
\]

Thus,

\[
Q
\begin{pmatrix}
3/5\\
2/5
\end{pmatrix}
=
\begin{pmatrix}
1/\sqrt2\\
-1/(5\sqrt2)
\end{pmatrix}.
\]

Therefore,

\[
A'
=
\frac1{\sqrt2}.
\]

The coupling amplitude is

\[
f_c
=
\sqrt{\frac35}.
\]

Hence,

\[
P_{\rm GEO}
=
\frac{
\sqrt{3/5}
}{
1/\sqrt2
}.
\]

Therefore,

\[
\boxed{
P_{\rm GEO}
=
\sqrt{\frac65}
=
1.095445115010332\ldots
}
\]

with analytic-to-engine agreement at approximately machine precision.

This is the fixed geometric factor carried forward into the GEO-Hubble application hypothesis.
