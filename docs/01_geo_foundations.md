# 01 — GEO Mathematical Foundations Used in the Hubble Projection Demonstration

## Purpose

This document defines the mathematical objects from GEO — Hidden Geometry that are required by the GEO-Hubble Geometric Projection demonstration.

Its purpose is not to reproduce the complete GEO framework.

Instead, it isolates the minimum canonical structure needed for the present derivation while preserving the distinction between:

- architectural quantities;
- effective-state quantities;
- radial response;
- tangent projection;
- observable interpretation.

This separation is essential because a historical notation error conflated two quantities that belong to different levels of the GEO construction.

The canonical radial law is

\[
\boxed{
R=\mu_{\rm eff}^{1/3}
}
\]

and not

\[
R=\eta^{1/3}.
\]

No universal identity

\[
\mu_{\rm eff}=\eta
\]

is assumed anywhere in this repository.

---

# 1. Mathematical hierarchy

The GEO quantities used here belong to different mathematical layers.

The minimum hierarchy is

\[
\boxed{
\text{conservation}
\rightarrow
\text{canonical partition}
\rightarrow
\text{coupling amplitude}
}
\]

together with the independent branch

\[
\boxed{
\text{effective state}
\rightarrow
\text{radial response}
}
\]

and the geometric projection branch

\[
\boxed{
\text{conserved pair}
\rightarrow
\text{tangent operator}
\rightarrow
\text{projected coordinates}.
}
\]

The principal quantities are:

\[
A,\quad
B,\quad
\eta,\quad
f_c,\quad
\mu_{\rm eff},\quad
R,\quad
\theta,\quad
Q(\theta).
\]

They must not be treated as interchangeable symbols.

---

# 2. Conservative normalization

The reduced GEO architecture is normalized by

\[
\boxed{
A+B=1.
}
\]

Here:

\[
A
\]

denotes the active or observable-side component, while

\[
B
\]

denotes its complementary component.

The equality

\[
A+B=1
\]

is a conservation statement.

It does not require

\[
A=B.
\]

It requires only that the two components form a normalized complementary pair.

For an arbitrary admissible state,

\[
0<A<1,
\]

and therefore

\[
B=1-A.
\]

---

# 3. Canonical partition

For the canonical GEO state used in the present demonstration,

\[
\boxed{
A=\eta.
}
\]

The canonical value is

\[
\boxed{
\eta=\frac35.
}
\]

Therefore

\[
A=\frac35.
\]

By conservation,

\[
B=1-A,
\]

so

\[
B
=
1-\frac35
=
\frac25.
\]

Hence the canonical conservative state is

\[
\boxed{
(A,B)
=
\left(
\frac35,
\frac25
\right).
}
\]

Numerically,

\[
\boxed{
A=0.6,
\qquad
B=0.4.
}
\]

The conservation check is immediate:

\[
0.6+0.4=1.
\]

---

# 4. Canonical efficiency parameter

The quantity

\[
\eta
\]

is the canonical architectural efficiency used by GEO.

Within the present construction,

\[
\boxed{
\eta=\frac35.
}
\]

It is important to distinguish the role of \(\eta\) from the role of the effective-state variable

\[
\mu_{\rm eff}.
\]

The former belongs to the canonical architecture.

The latter belongs to a concrete realization or physical/numerical state.

Therefore,

\[
\boxed{
\eta
\text{ and }
\mu_{\rm eff}
\text{ are different mathematical objects.}
}
\]

They may numerically coincide in a specially declared realization, but such coincidence is not a universal GEO identity.

---

# 5. Quadratic efficiency law

The canonical coupling amplitude is denoted

\[
f_c.
\]

The GEO quadratic efficiency relation is

\[
\boxed{
\eta=f_c^2.
}
\]

Solving for the positive normalized amplitude gives

\[
\boxed{
f_c=\sqrt{\eta}.
}
\]

The positive branch is selected because the quantity is used as a normalized coupling amplitude.

For the canonical value

\[
\eta=\frac35,
\]

we obtain

\[
f_c
=
\sqrt{\frac35}.
\]

Therefore

\[
\boxed{
f_c
=
\sqrt{\frac35}
=
0.774596669241483\ldots
}
\]

The inverse identity is

\[
f_c^2
=
\left(
\sqrt{\frac35}
\right)^2
=
\frac35
=
\eta.
\]

Thus the quadratic closure is exact:

\[
\boxed{
f_c^2-\eta=0.
}
\]

---

# 6. Meaning of the square-root relation

The relation

\[
\eta=f_c^2
\]

and therefore

\[
f_c=\sqrt{\eta}
\]

must not be confused with the radial law.

The square root acts between

\[
f_c
\]

and

\[
\eta.
\]

The cube root acts between

\[
\mu_{\rm eff}
\]

and

\[
R.
\]

The two operator chains are therefore

\[
\boxed{
f_c
\longrightarrow
\eta=f_c^2
}
\]

and

\[
\boxed{
\mu_{\rm eff}
\longrightarrow
R=\mu_{\rm eff}^{1/3}.
}
\]

This distinction is one of the central bookkeeping rules of the corrected GEO-Hubble derivation.

---

# 7. Fundamental geometric effectiveness law

The canonical radial/effectiveness relation is

\[
\boxed{
R^3=\mu_{\rm eff}.
}
\]

Equivalently,

\[
\boxed{
R=\mu_{\rm eff}^{1/3}.
}
\]

The roles of the variables are:

- \(\mu_{\rm eff}\): effective normalized input/state;
- \(R\): corresponding radial or linear geometric response.

The mapping converts a cubic effective quantity into its associated linear scale.

---

# 8. Derivation of the cube-root response

Suppose a normalized effective quantity is represented by a cubic ratio

\[
\mu_{\rm eff}
=
\frac{V_{\rm eff}}{V_{\rm ref}}.
\]

If the relevant geometric measure satisfies

\[
V\propto \ell^3,
\]

then

\[
\frac{V_{\rm eff}}{V_{\rm ref}}
=
\left(
\frac{\ell_{\rm eff}}
{\ell_{\rm ref}}
\right)^3.
\]

Define the normalized radial response

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

Taking the real cube root gives

\[
\boxed{
R=\mu_{\rm eff}^{1/3}.
}
\]

The inverse reconstruction is

\[
\boxed{
\mu_{\rm eff}=R^3.
}
\]

Therefore the closure condition is

\[
\boxed{
R^3-\mu_{\rm eff}=0.
}
\]

---

# 9. The historical notation error

Some historical GEO-Hubble material contained the expression

\[
R=\eta^{1/3}.
\]

That expression implicitly makes the substitution

\[
\mu_{\rm eff}\rightarrow\eta.
\]

However, the canonical law is

\[
R=\mu_{\rm eff}^{1/3}.
\]

Therefore the general substitution

\[
\boxed{
R=\eta^{1/3}
}
\]

is not used in the corrected derivation.

The correct dependency is

\[
\boxed{
\mu_{\rm eff}
\rightarrow
R.
}
\]

The canonical architectural dependency is separately

\[
\boxed{
f_c
\rightarrow
\eta.
}
\]

Graphically:

\[
\begin{array}{ccc}
f_c & \longrightarrow & \eta=f_c^2 \\[4pt]
\mu_{\rm eff} & \longrightarrow & R=\mu_{\rm eff}^{1/3}
\end{array}
\]

The two rows must not be crossed without an independently justified application rule.

---

# 10. Independence of \(\eta\) and \(\mu_{\rm eff}\)

A useful way to see the distinction is to hold

\[
\eta
\]

fixed while varying

\[
\mu_{\rm eff}.
\]

Let

\[
\eta=0.6.
\]

Then

\[
f_c
=
\sqrt{0.6}
=
0.774596669241483\ldots
\]

is fixed.

Now consider different effective states.

For

\[
\mu_{\rm eff}=0.4,
\]

the radial response is

\[
R
=
0.4^{1/3}
=
0.736806299728077\ldots
\]

For

\[
\mu_{\rm eff}=0.6,
\]

\[
R
=
0.6^{1/3}
=
0.843432665301749\ldots
\]

For

\[
\mu_{\rm eff}=0.8104,
\]

\[
R
=
0.8104^{1/3}
=
0.932323170115423\ldots
\]

For

\[
\mu_{\rm eff}=1,
\]

\[
R=1.
\]

Thus

\[
R
\]

varies even though

\[
\eta
\]

and

\[
f_c
\]

remain fixed.

This establishes the mathematical independence required by the corrected architecture.

---

# 11. External Operator verification of the radial law

The GEO External Operator exposes an API of the form

\[
\mathrm{compute}
(
\eta,
L,
\mu_{\rm eff}
).
\]

This interface itself preserves the distinction between

\[
\eta
\]

and

\[
\mu_{\rm eff}.
\]

For each tested state, the engine returns

\[
R
\]

such that

\[
R^3
\approx
\mu_{\rm eff}
\]

to floating-point precision.

The numerical residual

\[
R^3-\mu_{\rm eff}
\]

was found to be at the level of

\[
10^{-16}
\]

or zero at the displayed precision.

The executable implementation therefore reproduces the corrected radial law directly.

---

# 12. Canonical tangent angle

The projection layer uses the canonical balanced angle

\[
\boxed{
\theta_0=\frac{\pi}{4}.
}
\]

In degrees,

\[
\theta_0=45^\circ.
\]

At this angle,

\[
\cos\theta_0
=
\sin\theta_0.
\]

Using the standard trigonometric identity,

\[
\cos\frac{\pi}{4}
=
\sin\frac{\pi}{4}
=
\frac{\sqrt2}{2}
=
\frac1{\sqrt2}.
\]

Therefore

\[
\boxed{
c_0=s_0=\frac1{\sqrt2}.
}
\]

---

# 13. Orthogonal tangent operator

The canonical tangent/membrane operator is the two-dimensional orthogonal transformation

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

Let

\[
c=\cos\theta,
\qquad
s=\sin\theta.
\]

Then

\[
Q(\theta)
=
\begin{pmatrix}
c&s\\
-s&c
\end{pmatrix}.
\]

---

# 14. Orthogonality proof

The transpose is

\[
Q^T
=
\begin{pmatrix}
c&-s\\
s&c
\end{pmatrix}.
\]

Then

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

Multiplying,

\[
Q^TQ
=
\begin{pmatrix}
c^2+s^2 & cs-cs\\
sc-sc & s^2+c^2
\end{pmatrix}.
\]

Using

\[
c^2+s^2=1,
\]

we obtain

\[
Q^TQ
=
\begin{pmatrix}
1&0\\
0&1
\end{pmatrix}.
\]

Therefore

\[
\boxed{
Q^TQ=I.
}
\]

Hence \(Q\) is orthogonal.

---

# 15. Norm preservation

Let

\[
\mathbf v
=
\begin{pmatrix}
A\\
B
\end{pmatrix}.
\]

The projected state is

\[
\mathbf v'
=
Q\mathbf v.
\]

Because \(Q\) is orthogonal,

\[
\|\mathbf v'\|^2
=
\mathbf v'^T\mathbf v'.
\]

Substitute

\[
\mathbf v'=Q\mathbf v:
\]

\[
\|\mathbf v'\|^2
=
\mathbf v^TQ^TQ\mathbf v.
\]

Since

\[
Q^TQ=I,
\]

we obtain

\[
\|\mathbf v'\|^2
=
\mathbf v^T\mathbf v
=
\|\mathbf v\|^2.
\]

Therefore

\[
\boxed{
\|\mathbf v'\|
=
\|\mathbf v\|.
}
\]

The projection is norm-preserving.

This is also tested by the GEO External Operator through its projection-norm closure diagnostic.

---

# 16. Projection of the conservative state

Apply

\[
Q(\theta)
\]

to

\[
\mathbf v
=
\begin{pmatrix}
A\\
B
\end{pmatrix}.
\]

Then

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

Matrix multiplication gives

\[
\boxed{
A'
=
A\cos\theta
+
B\sin\theta
}
\]

and

\[
\boxed{
B'
=
-A\sin\theta
+
B\cos\theta.
}
\]

These are the two projected coordinates.

---

# 17. Canonical projection

At

\[
\theta=\frac{\pi}{4},
\]

we have

\[
\cos\theta
=
\sin\theta
=
\frac1{\sqrt2}.
\]

Therefore

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

By conservation,

\[
A+B=1.
\]

Therefore

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

This result does not depend on the individual values of \(A\) and \(B\) as long as:

\[
A+B=1
\]

and

\[
\theta=\frac{\pi}{4}.
\]

---

# 18. Complementary canonical projection

The second coordinate is

\[
B'
=
-A\frac1{\sqrt2}
+
B\frac1{\sqrt2}.
\]

Therefore

\[
B'
=
\frac{B-A}{\sqrt2}.
\]

For the canonical partition

\[
A=0.6,
\qquad
B=0.4,
\]

we obtain

\[
B-A=-0.2.
\]

Thus

\[
B'
=
-\frac{0.2}{\sqrt2}.
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

# 19. Engine reproduction of the tangent projection

The GEO External Operator returned

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

The direct analytic calculation returned the same values.

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

This establishes analytic-to-engine closure of the projection layer.

---

# 20. Reconstruction check

Because

\[
Q
\]

is orthogonal,

\[
Q^{-1}=Q^T.
\]

Therefore the original state can be reconstructed from the projected state:

\[
\mathbf v
=
Q^T\mathbf v'.
\]

The External Operator returned reconstructed values

\[
A_{\rm rec}
=
0.5999999999999999
\]

and

\[
B_{\rm rec}
=
0.39999999999999997.
\]

The reconstruction errors are therefore at floating-point precision.

This confirms that the projection is not an information-destroying scalar rescaling.

It is an invertible orthogonal reorganization of the two-dimensional conservative state.

---

# 21. Separation of radial and tangent layers

The two relevant transformations may now be written side by side.

## Radial/effective transformation

\[
\boxed{
\mu_{\rm eff}
\longrightarrow
R=\mu_{\rm eff}^{1/3}.
}
\]

## Tangent projection

\[
\boxed{
(A,B)
\longrightarrow
Q(\pi/4)(A,B).
}
\]

They are independent mathematical operations.

Changing

\[
\mu_{\rm eff}
\]

changes

\[
R.
\]

But with fixed canonical architecture

\[
A=\eta,
\qquad
B=1-\eta,
\]

the tangent projection remains determined by

\[
Q(\pi/4).
\]

This is precisely what was observed in the External Operator sweep.

---

# 22. Canonical projected observable as a conservation consequence

A particularly useful identity follows from

\[
A+B=1.
\]

At the balanced tangent angle,

\[
A'
=
A\cos\frac{\pi}{4}
+
B\sin\frac{\pi}{4}.
\]

Because

\[
\cos\frac{\pi}{4}
=
\sin\frac{\pi}{4},
\]

we obtain

\[
A'
=
(A+B)\cos\frac{\pi}{4}.
\]

Therefore

\[
A'
=
\cos\frac{\pi}{4}.
\]

Since

\[
A+B=1,
\]

this is

\[
\boxed{
A'
=
\frac1{\sqrt2}.
}
\]

Notice what has and has not happened.

We did not impose

\[
A'=\cos\frac{\pi}{4}
\]

as an additional law.

It emerged from:

\[
A+B=1
\]

and

\[
Q(\pi/4).
\]

That distinction is important for the later Hubble derivation.

---

# 23. Coupling-to-projection ratio

We now possess two independently derived canonical quantities.

The coupling amplitude is

\[
f_c
=
\sqrt{\frac35}.
\]

The projected observable coordinate is

\[
A'
=
\frac1{\sqrt2}.
\]

Define the dimensionless canonical ratio

\[
\boxed{
P_{\rm GEO}
=
\frac{f_c}{A'}.
}
\]

Substitution gives

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

# 24. Why the ratio is independent of \(\mu_{\rm eff}\)

The numerator

\[
f_c
\]

depends on

\[
\eta.
\]

The denominator

\[
A'
\]

depends on

\[
A+B=1
\]

and

\[
\theta=\frac{\pi}{4}.
\]

Neither quantity contains

\[
\mu_{\rm eff}.
\]

Therefore

\[
P_{\rm GEO}
\]

is algebraically independent of \(\mu_{\rm eff}\) in this construction.

Symbolically,

\[
\frac{\partial P_{\rm GEO}}
{\partial\mu_{\rm eff}}
=
0.
\]

This is not merely a numerical observation.

It follows from the dependency graph.

The External Operator sweep provides an executable verification of the same fact.

---

# 25. Dependency graph

The corrected mathematical dependencies are

\[
\eta
\longrightarrow
A=\eta
\]

and

\[
\eta
\longrightarrow
B=1-\eta.
\]

Also,

\[
\eta
\longrightarrow
f_c=\sqrt{\eta}.
\]

The projection branch is

\[
(A,B,\theta)
\longrightarrow
(A',B').
\]

The effective radial branch is independently

\[
\mu_{\rm eff}
\longrightarrow
R=\mu_{\rm eff}^{1/3}.
\]

Therefore the dependency graph is

\[
\boxed{
\eta
\rightarrow
\{A,B,f_c\}
}
\]

\[
\boxed{
\{A,B,\theta\}
\rightarrow
\{A',B'\}
}
\]

\[
\boxed{
\{f_c,A'\}
\rightarrow
P_{\rm GEO}
}
\]

while independently

\[
\boxed{
\mu_{\rm eff}
\rightarrow
R.
}
\]

There is no canonical arrow

\[
\eta\rightarrow R.
\]

---

# 26. Mathematical theorem used by GEO-Hubble

## Theorem

Let

\[
A+B=1,
\]

let

\[
A=\eta,
\]

and let

\[
\eta=f_c^2.
\]

Let the conservative pair be transformed by

\[
Q\left(\frac{\pi}{4}\right).
\]

Then

\[
A'=\frac1{\sqrt2}.
\]

For

\[
\eta=\frac35,
\]

the ratio

\[
\frac{f_c}{A'}
\]

is

\[
\sqrt{\frac65}.
\]

## Proof

From

\[
\eta=f_c^2
\]

and

\[
\eta=\frac35,
\]

we have

\[
f_c=\sqrt{\frac35}.
\]

From

\[
Q\left(\frac{\pi}{4}\right),
\]

the first projected coordinate is

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

Using

\[
A+B=1,
\]

we get

\[
A'
=
\frac1{\sqrt2}.
\]

Therefore

\[
\frac{f_c}{A'}
=
\frac{\sqrt{3/5}}
{1/\sqrt2}.
\]

Hence

\[
\boxed{
\frac{f_c}{A'}
=
\sqrt{\frac65}.
}
\]

QED.

---

# 27. What the theorem does not contain

The theorem contains no:

- Hubble constant;
- Planck value;
- SH0ES value;
- local-distance-ladder value;
- fitted cosmological parameter;
- target projection value.

Therefore

\[
P_{\rm GEO}
=
\sqrt{\frac65}
\]

is derived independently of the later Hubble comparison.

The physical identification of this ratio with a Hubble-scale ratio is introduced only in the application document

`03_hubble_hypothesis.md`.

---

# 28. Claim boundary

The results of this document establish the internal mathematical structure used by the later Hubble hypothesis.

They establish:

\[
A+B=1,
\]

\[
\eta=\frac35,
\]

\[
f_c=\sqrt{\eta},
\]

\[
R=\mu_{\rm eff}^{1/3},
\]

\[
Q=Q(\pi/4),
\]

\[
A'=\frac1{\sqrt2},
\]

and

\[
P_{\rm GEO}
=
\sqrt{\frac65}.
\]

They do not establish by themselves that

\[
\frac{H_{\rm local}}{H_{\rm base}}
=
P_{\rm GEO}.
\]

That statement is a physical application hypothesis and is treated separately.

---

# 29. Summary

The corrected GEO mathematical architecture required by this project is

\[
\boxed{
A+B=1
}
\]

\[
\boxed{
A=\eta=\frac35
}
\]

\[
\boxed{
B=\frac25
}
\]

\[
\boxed{
\eta=f_c^2
}
\]

\[
\boxed{
f_c=\sqrt{\frac35}
}
\]

\[
\boxed{
R=\mu_{\rm eff}^{1/3}
}
\]

\[
\boxed{
Q(\theta)
=
\begin{pmatrix}
\cos\theta & \sin\theta\\
-\sin\theta & \cos\theta
\end{pmatrix}
}
\]

\[
\boxed{
\theta=\frac{\pi}{4}
}
\]

\[
\boxed{
A'=\frac1{\sqrt2}
}
\]

and consequently

\[
\boxed{
P_{\rm GEO}
=
\frac{f_c}{A'}
=
\sqrt{\frac65}.
}
\]

The effective radial state

\[
\mu_{\rm eff}
\]

remains independent of the canonical architectural quantity

\[
\eta.
\]


This distinction is preserved throughout the remaining derivation.
