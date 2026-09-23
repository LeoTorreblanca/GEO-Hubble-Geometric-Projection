# GEO External Operator — Executable Provenance and Validation Record

## Purpose

This document records the executable provenance of the GEO External Operator used by the GEO-Hubble Geometric Projection repository.

The purpose is to establish:

- which external software implementation was used;
- which version and commit were tested;
- how the package was installed;
- which native tests were executed;
- which API was used;
- which outputs were produced;
- which mathematical relations were confirmed;
- which conclusions can legitimately be drawn from those tests;
- which conclusions remain physical hypotheses rather than software proofs.

The GEO External Operator is treated here as a separate executable implementation of the GEO mathematical architecture.

It is not modified in order to force the Hubble projection result.

---

# 1. Upstream repository

Primary repository:

https://github.com/LeoTorreblanca/GEO-External-Operator

Repository role:

- executable implementation of GEO operators;
- C/Python scientific interface;
- canonical partition evaluation;
- independent effective-state input;
- radial-law computation;
- projection;
- reconstruction;
- spectral calculations;
- optional cosmological adapters.

The exact commit used for the frozen release must be recorded below.

## Frozen revision

Repository:

`GEO-External-Operator`

Repository URL:

https://github.com/LeoTorreblanca/GEO-External-Operator

Reference commit:

`003402ef5edff2fe6efa020c368de8064e711732`

Branch:

`main`

API version:

`1`

Validation date:

`2026-09-14`

This is the frozen External Operator revision used by the present
GEO-Hubble Geometric Projection validation.

The reference commit is the same revision identified in the main
repository README and used for the reproducibility audit.

---

# 2. Test installation path

The External Operator was cloned into an isolated test location:

`~/GEO-EXTERNAL-TEST/GEO-External-Operator`

This test copy was used to avoid modifying pre-existing GEO repositories elsewhere in the system.

The isolation strategy ensures that the validation results correspond to a clean clone rather than an older local development tree.

---

# 3. Python environment

A dedicated Python virtual environment was created inside the test repository.

Environment path:

`.venv`

Activation command:

`source .venv/bin/activate`

The package configuration identified the project as a Python package with a compiled C component using scikit-build/CMake.

The project also declared scientific dependencies including NumPy and SciPy, together with optional test and Cobaya dependencies.

Exact package versions used in the frozen release must be recorded in the final environment log.

---

# 4. Installation method

The package was installed in editable mode with its test dependencies.

Installation form:

`pip install -e ".[test]"`

This installation strategy was chosen so that:

- the public Python API could be imported directly;
- the native test suite could be executed;
- the compiled operator could be exercised without altering the mathematical source;
- local validation scripts could call the installed package.

---

# 5. Public Python API

The validation used the public package:

`geo_external_operator`

The principal function used was:

`compute`

The API version function was:

`api_version`

A representative call has the form

$$
\mathrm{compute}
(
\eta,
L,
\mu_{\rm eff}
).
$$

This is important because the API itself exposes

$$
\eta
$$

and

$$
\mu_{\rm eff}
$$

as separate inputs.

Thus the executable interface does not require the universal identification

$$
\mu_{\rm eff}=\eta.
$$

---

# 6. API version

During the validation run, the reported API version was

$$
\boxed{
1
}
$$

This value should be re-recorded during the frozen release.

---

# 7. Returned result structure

The public result object returned the following fields:

- `eta`
- `L`
- `mu_eff`
- `R`
- `Phi`
- `alpha`
- `projected_observable`
- `projected_complementary`
- `projected_latent`
- `reconstructed_observable`
- `reconstructed_complementary`
- `reconstructed_latent`
- `projection_norm_error`
- `reconstruction_observable_error`
- `reconstruction_complementary_error`
- `reconstruction_latent_error`

This result structure makes it possible to test multiple layers of the GEO architecture independently.

---

# 8. Canonical input used for projection audit

The canonical architectural parameters used in the projection audit were

$$
\eta=0.6
$$

and

$$
L=0.
$$

A representative effective-state input was

$$
\mu_{\rm eff}=0.8104.
$$

This value was used only as one test point.

It was not treated as a universal Hubble value or a fitted cosmological parameter.

---

# 9. Representative engine output

For

$$
\eta=0.6,
$$

$$
L=0,
$$

and

$$
\mu_{\rm eff}=0.8104,
$$

the External Operator returned approximately:

$$R=0.9323231701154233,
$$

$$\Phi=1.8968957201959051,
$$

$$
\alpha=0.5365231307817058,
$$

$$
A'_{\rm engine}=0.7071067811865475,
$$

$$
B'_{\rm engine}=-0.1414213562373094.
$$

The reconstructed conservative coordinates were

$$
A_{\rm rec}=0.5999999999999999,
$$

and

$$
B_{\rm rec}=0.39999999999999997.
$$

These values agree with the canonical state to floating-point precision.

---

# 10. Projection norm closure

For the same state, the engine reported

$$
\text{projection\_norm\_error} = 1.1102230246251565 \times 10^{-16}
$$

This is consistent with the expected orthogonal norm-preserving behavior of the tangent operator.

The result should be interpreted as software-level mathematical closure.

It is not empirical cosmological evidence.

---

# 11. Reconstruction closure

The engine reported reconstruction errors of approximately

$$
1.11\times10^{-16}
$$

for the observable coordinate and approximately

$$
5.55\times10^{-17}
$$

for the complementary coordinate.

The latent reconstruction error was zero at the displayed precision.

This confirms that the executable projection is numerically invertible within floating-point precision for the tested state.

---

# 12. Radial-law audit

The External Operator was tested with

$$
\eta=0.6
$$

held fixed while

$$
\mu_{\rm eff}
$$

was varied.

The tested values were:

$$
0.4,
$$

$$
0.5,
$$

$$
0.6,
$$

$$
0.7,
$$

$$
0.8,
$$

$$
0.8104,
$$

$$
0.9,
$$

$$
1.0.
$$

For every tested state, the returned radial value agreed with

$$
\boxed{R=\mu_{\rm eff}^{1/3}.}
$$

---

# 13. Radial-law numerical table

The representative results were:

| $\mu_{\text{eff}}$ | $(R)$ |
|---:|---:|
| 0.400000 | 0.736806299728077 |
| 0.500000 | 0.793700525984100 |
| 0.600000 | 0.843432665301749 |
| 0.700000 | 0.887904001742601 |
| 0.800000 | 0.928317766722556 |
| 0.810400 | 0.932323170115423 |
| 0.900000 | 0.965489384605630 |
| 1.000000 | 1.000000000000000 |

The corresponding closure residuals

$$
R^3-\mu_{\rm eff}
$$

were zero or of order

$$
10^{-16}.
$$
---

# 14. Direct evidence of \(\mu_{\rm eff}\) / \(\eta\) independence

Compare two runs with

$$
\eta=0.6
$$

fixed.

For

$$
\mu_{\rm eff}=0.6,
$$

the engine returned

$$
R_1=0.843432665301749.
$$

For

$$
\mu_{\rm eff}=0.8104,
$$

the engine returned

$$R_2=0.932323170115423.
$$

Thus

$$
R_1\neq R_2
$$

while

$$
\eta
$$

remained unchanged.

This provides direct executable evidence that

$$
\mu_{\rm eff}
$$

and

$$
\eta
$$

are distinct inputs in the core implementation.

---

# 15. Native test-suite evidence

The External Operator native test suite was executed after installation.

The suite included explicit tests for:

- API behavior;
- independence of `mu_eff` from `eta`;
- canonical radial law;
- projection norm closure;
- reconstruction closure.

The observed native test result was:

$$
\boxed{5\ \text{passed}}
$$

with one optional test skipped.

The exact pytest output should be archived in the frozen release under the results or provenance directory.

---

# 16. Projection output independence from \(\mu_{\rm eff}\)

During the radial sweep, the engine returned the same projected observable for every tested effective state:

$$
\boxed{A'_{\rm engine}=0.707106781186547\ldots}
$$

The measured span was

$$
\boxed{\Delta A'=0}
$$

at the displayed numerical precision.

Thus, within the tested implementation, the canonical tangent projection is independent of the radial input.

---

# 17. Analytic reconstruction of the engine projection

Using

$$
A=\eta=0.6,
$$

$$
B=1-\eta=0.4,
$$

and

$$
\theta=\frac{\pi}{4},
$$

the analytic tangent projection gives

$$
A'_{\rm analytic}=A\cos\theta+B\sin\theta.
$$

Since

$$
\cos\theta=\sin\theta=\frac1{\sqrt2},
$$

we obtain

$$
A'_{\rm analytic}=\frac{A+B}{\sqrt2}.
$$

Because

$$
A+B=1,
$$

$$
\boxed{A'_{\rm analytic}=\frac1{\sqrt2}.}
$$

Numerically,

$$
A'_{\rm analytic}=0.707106781186547\ldots
$$

which matches the engine output exactly at the displayed precision.

---

# 18. Analytic complementary projection

The second analytic coordinate is

$$
B'_{\rm analytic}=-A\sin\theta+B\cos\theta.
$$

At

$$
\theta=\frac{\pi}{4},
$$

this becomes

$$
B'_{\rm analytic}=\frac{B-A}{\sqrt2}.
$$

For

$$A = 0.6, \quad B = 0.4$$

$$
B'_{\rm analytic}=-\frac{0.2}{\sqrt2}.
$$

Numerically,

$$\boxed{B'_{\rm analytic}=-0.141421356237309\ldots}
$$

matching the engine output at the displayed precision.

---

# 19. Analytic versus engine error

The measured differences were

$$
\boxed{|A'_{\rm analytic}-A'_{\rm engine}|=0}
$$

and

$$
\boxed{|B'_{\rm analytic}-B'_{\rm engine}|=0}
$$

at the displayed precision.

This provides direct analytic-to-engine closure of the projection layer.

---

# 20. Canonical coupling value

The canonical coupling amplitude was reconstructed independently as

$$
f_c=\sqrt{\eta}.
$$

For

$$
\eta=0.6,
$$

the value is

$$
\boxed{f_c=0.774596669241483.}
$$

This quantity is derived from the architectural efficiency and does not depend on

$$
\mu_{\rm eff}.
$$

---

# 21. Engine-based projection factor

The projection factor was reconstructed as

$$
\boxed{P_{\rm engine}=\frac{f_c}{A'_{\rm engine}}.}
$$

Using the engine output,

$$
P_{\rm engine}=\frac{0.774596669241483}{0.707106781186547}.
$$

The result was

$$
\boxed{P_{\rm engine}=1.095445115010332.}
$$

This value was not assigned directly.

It was reconstructed from the canonical coupling and the engine projection output.

---

# 22. Closed-form comparison

The independent analytic form is

$$
P_{\rm analytic}=\sqrt{\frac65}.
$$

Numerically,

$$
P_{\rm analytic}=1.095445115010332.
$$

The measured difference was approximately

$$
\boxed{|P_{\rm engine}-P_{\rm analytic}|=2.22\times10^{-16}.}
$$

This is consistent with floating-point machine precision.

---

# 23. Projection-factor invariance sweep

For every tested value of

$$
\mu_{\rm eff},
$$

the reconstructed factor was

$$
P_{\rm engine}=1.095445115010332.
$$

The reported span was

$$
\boxed{\Delta P_{\rm engine}=0}
$$

at the displayed precision.

This executable result confirms the analytic independence of the canonical projection factor from the radial effective state.

---

# 24. Reference Hubble calculation

After the projection factor had been reconstructed, a reference baseline value

$$
H_{\rm base}=67.4
$$

was supplied.

The predicted projected value was calculated as

$$
H_{\rm pred}=H_{\rm base}P_{\rm engine}.
$$

The engine-derived factor gave

$$
\boxed{H_{\rm pred}=73.833000751696.}
$$

No local-Hubble target was used to obtain the factor.

---

# 25. Important interpretation boundary

The External Operator proves neither

$$
H_{\rm local}=73.833000751696
$$

nor

$$
\frac{H_{\rm local}}{H_{\rm base}}=P_{\rm GEO}
$$

as an empirical fact.

What the engine verifies is the internal GEO operator structure used to construct the dimensionless projection factor.

The identification of that factor with a Hubble-scale ratio remains a physical application hypothesis.

---

# 26. What the External Operator confirms

Within the tested implementation, the External Operator confirms:

$$
\boxed{\eta\text{ and }\mu_{\rm eff}\text{ are independent inputs}}
$$

$$
\boxed{R=\mu_{\rm eff}^{1/3}}
$$

$$
\boxed{Q(\pi/4)\text{ produces the canonical tangent projection}}
$$

$$
\boxed{A'=\frac1{\sqrt2}}
$$

for the conservative canonical state,

and

$$
\boxed{\frac{f_c}{A'}=\sqrt{\frac65}}
$$

to floating-point precision.

---

# 27. What the External Operator does not confirm by itself

The software does not by itself establish:

- that the Universe realizes the GEO-Hubble mapping;
- that the local Hubble scale is exactly the projected state;
- that the Hubble tension is definitively resolved;
- that the GEO framework is a completed theory of gravity;
- that every cosmological observable uses the same projection ratio;
- that a particular historical Hubble value must be recovered.

These remain scientific interpretation questions.

---

# 28. Historical compatibility adapter

The External Operator repository contains an older Hubble/Cobaya compatibility path that uses a reduction of the form

$$
\mu_H:=\eta.
$$

This path should be understood as preserving an earlier realization.

It is not used in the corrected canonical projection proof contained in the present repository.

The core engine itself accepts

$$
\eta
$$

and

$$
\mu_{\rm eff}
$$

independently.

---

# 29. Why the historical adapter is excluded from the corrected proof

The corrected proof is intended to determine whether the canonical projection factor survives once the radial notation issue is removed.

Therefore it must not begin by imposing

$$
\mu_H=\eta.
$$

Instead, the proof uses only:

$$
A+B=1,
$$

$$
\eta=f_c^2,
$$

and

$$
Q(\pi/4).
$$

The radial branch remains independently validated through

$$
R=\mu_{\rm eff}^{1/3}.
$$

---

# 30. Role of \(\Phi\) and \(\alpha\)

The External Operator returns spectral quantities

$$
\Phi
$$

and

$$
\alpha.
$$

During the effective-state sweep, these quantities changed with

$$
\mu_{\rm eff}.
$$

For example, \(\Phi\) increased from approximately

$$
1.881156654418159
$$

at

$$
\mu_{\rm eff}=0.4
$$

to approximately

$$
1.902585570253989
$$

at

$$
\mu_{\rm eff}=1.
$$

Similarly, \(\alpha\) changed across the sweep.

However,

$$
P_{\rm GEO}
$$

remained fixed.

Therefore \(\Phi\) and \(\alpha\) are not required to derive the canonical projection factor used in this repository.

---

# 31. No claim that spectral quantities are irrelevant to GEO

The fact that

$$
\Phi
$$

and

$$
\alpha
$$

are not required in the present proof does not mean they are mathematically irrelevant to the broader GEO framework.

It means only that the corrected canonical Hubble projection factor can be derived without them.

Their broader role should be studied separately.

---

# 32. Numerical precision

The validation was performed using standard floating-point arithmetic.

Differences at the level of

$$
10^{-16}
$$

should be interpreted as numerical agreement to approximately machine precision.

They should not be interpreted as measurements of physical precision in cosmology.

---

# 33. Reproducibility commands to record for release

The frozen release should record the outputs of at least:

`git rev-parse HEAD`

`git branch --show-current`

`git status --short`

`python --version`

`pip freeze`

`pytest -vv`

and the custom GEO projection validation scripts.

These outputs should be preserved under the release provenance or results directories.

---

# 34. Required frozen metadata

Before release, replace the placeholders at the beginning of this document with:

- exact commit hash;
- exact branch;
- retrieval date;
- working-tree state;
- API version;
- Python version;
- package version if exposed;
- compiler/build information if relevant.

---

# 35. Suggested release statement

A concise executable-provenance statement may be written as follows:

> The GEO-Hubble Geometric Projection derivation was separately reproduced using a clean installation of the public GEO External Operator. The engine treats the canonical architectural efficiency \(\eta\) and effective radial state \(\mu_{\rm eff}\) as independent inputs, reproduces \(R^3=\mu_{\rm eff}\), returns the canonical tangent projection \(A'=1/\sqrt2\), and reproduces the analytic projection factor \(\sqrt{6/5}\) to floating-point machine precision.

---

# 36. Provenance status table

| Item | Status |
|---|---|
| Clean isolated clone | COMPLETE |
| Dedicated virtual environment | COMPLETE |
| Package installation | COMPLETE |
| Public API import | COMPLETE |
| API version check | COMPLETE |
| Native tests | COMPLETE |
| Radial-law sweep | COMPLETE |
| \(\mu_{\rm eff}\) / \(\eta\) independence | COMPLETE |
| Result-structure audit | COMPLETE |
| Analytic projection reproduction | COMPLETE |
| Engine projection reproduction | COMPLETE |
| Analytic/engine comparison | COMPLETE |
| Projection-factor reconstruction | COMPLETE |
| Closed-form comparison | COMPLETE |
| Projection-factor invariance sweep | COMPLETE |
| Reference Hubble calculation | COMPLETE |
| Frozen commit hash | PENDING |
| Frozen environment log | PENDING |
| Archived validation logs | PENDING |

---

# 37. Binding interpretation

For this repository, the GEO External Operator is used as:

$$
\boxed{\text{an executable implementation of the GEO mathematical architecture}}
$$

and not as:

$$
\boxed{\text{independent observational evidence for the physical GEO-Hubble hypothesis}.}
$$

This distinction is binding.

---

# 38. Final executable conclusion

The External Operator validation establishes that the executable GEO architecture is consistent with the corrected mathematical dependency chain

$$
\eta\rightarrow\{A,B,f_c\},
$$

$$\mu_{\text{eff}} \rightarrow R$$

and

$$
(A,B,\pi/4)\rightarrow(A',B').
$$

For the canonical state,

$$
A'=\frac1{\sqrt2}
$$

and

$$
f_c=\sqrt{\frac35}.
$$

Therefore the independently reconstructed executable ratio is

$$
\boxed{P_{\rm engine}=\frac{f_c}{A'}=\sqrt{\frac65}}
$$

to approximately machine precision.

This is the executable result carried forward by the present repository.
