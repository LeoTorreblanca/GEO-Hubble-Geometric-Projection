# External Dependencies and Frozen Upstream Sources

## Purpose

This directory documents the external GEO repositories required to reproduce the GEO-Hubble Geometric Projection results.

The present repository does not duplicate or rewrite the upstream source code.

Instead, it records:

- which external repositories are required;
- why they are required;
- how they should be obtained;
- how their exact revisions should be frozen;
- how the GEO External Operator should be installed;
- how its native validation should be executed;
- how this repository should call the external implementation without modifying it.

This design preserves provenance and avoids silently mixing the original framework, executable implementation, and present Hubble derivation into a single untraceable code base.

---

# 1. Required upstream repositories

Two principal upstream repositories are used.

## 1.1 GEO Hidden Geometry Framework

Repository:

https://github.com/LeoTorreblanca/GEO-hidden-geometry-framework

Role:

- historical mathematical framework;
- original GEO development;
- canonical geometric concepts;
- efficiency structure;
- radial/effective law;
- early projection concepts;
- historical Hubble work.

This repository is used primarily for mathematical provenance.

It is not treated as the executable reference implementation for the present numerical tests.

---

## 1.2 GEO External Operator

Repository:

https://github.com/LeoTorreblanca/GEO-External-Operator

Role:

- executable implementation of the GEO architecture;
- Python/C interface;
- canonical partition evaluation;
- radial law;
- effective-state input;
- tangent projection;
- reconstruction;
- spectral outputs;
- native tests.

This repository is the principal executable dependency of the GEO-Hubble Geometric Projection validation scripts.

---

# 2. Recommended external-source layout

For a clean reproduction environment, the following layout is recommended:

`GEO-Hubble-Geometric-Projection/`

with an external-source area conceptually containing:

`external/GEO-hidden-geometry-framework`

and

`external/GEO-External-Operator`

The present repository does not require the upstream source code to be permanently copied into the project tree.

The upstream repositories may instead be:

- cloned separately and referenced through recorded paths;
- included as Git submodules;
- installed from frozen commit hashes;
- archived separately with exact version metadata.

For the first reproducibility release, Git submodules are recommended because they preserve exact commit references.

---

# 3. Why upstream source should remain separate

The mathematical and scientific provenance is clearer if the projects remain distinct.

The dependency chain is:

**Original GEO framework**

↓

**GEO External Operator**

↓

**GEO-Hubble Geometric Projection**

Each layer has a different purpose.

The original framework establishes historical and mathematical provenance.

The External Operator implements the architecture computationally.

The present repository derives and tests the corrected Hubble projection.

Combining the source trees directly would make it harder to determine which result originated where.

---

# 4. Clean clone procedure

A fresh external working area may be created with:

`mkdir -p ~/GEO-Hubble-Upstream`

Then enter it:

`cd ~/GEO-Hubble-Upstream`

Clone the original framework:

`git clone https://github.com/LeoTorreblanca/GEO-hidden-geometry-framework.git`

Clone the External Operator:

`git clone https://github.com/LeoTorreblanca/GEO-External-Operator.git`

The repositories should then exist independently as:

`~/GEO-Hubble-Upstream/GEO-hidden-geometry-framework`

and

`~/GEO-Hubble-Upstream/GEO-External-Operator`

---

# 5. Record exact source revisions immediately

After cloning the original framework:

`cd ~/GEO-Hubble-Upstream/GEO-hidden-geometry-framework`

record:

`git remote -v`

`git branch --show-current`

`git rev-parse HEAD`

`git status --short`

Then repeat for the External Operator:

`cd ~/GEO-Hubble-Upstream/GEO-External-Operator`

`git remote -v`

`git branch --show-current`

`git rev-parse HEAD`

`git status --short`

The commit hashes must be copied into:

`provenance/GEO_ORIGINAL.md`

and

`provenance/EXTERNAL_OPERATOR.md`

before an archival release.

---

# 6. Clean working-tree requirement

The preferred upstream state for a reproducibility release is:

`git status --short`

returning no output.

This means the working tree is clean.

If local modifications exist, they must either:

- be committed and documented;
- be discarded;
- or be explicitly recorded as part of a non-clean reproduction state.

Unrecorded local modifications are not acceptable for a frozen release.

---

# 7. Optional submodule strategy

The present repository may later include the upstream projects as Git submodules.

From the root of this repository, the conceptual commands are:

`git submodule add https://github.com/LeoTorreblanca/GEO-hidden-geometry-framework.git external/GEO-hidden-geometry-framework`

and

`git submodule add https://github.com/LeoTorreblanca/GEO-External-Operator.git external/GEO-External-Operator`

After this, exact commits can be frozen by committing the submodule pointers.

This strategy is recommended for a public reproducibility release.

---

# 8. External Operator virtual environment

The GEO External Operator should be installed in a dedicated Python environment.

Example:

`cd ~/GEO-Hubble-Upstream/GEO-External-Operator`

Create the virtual environment:

`python3 -m venv .venv`

Activate it:

`source .venv/bin/activate`

Upgrade packaging tools:

`python -m pip install --upgrade pip setuptools wheel`

Install the package and test dependencies:

`pip install -e ".[test]"`

The installation must complete without modifying the scientific formulas for the purpose of obtaining the desired Hubble result.

---

# 9. External Operator import test

After installation, verify the public API:

`python -c "import geo_external_operator; print(geo_external_operator.__file__)"`

The import should resolve to the installed External Operator package.

A more complete check may inspect:

- `compute`
- `api_version`

The public API used by this repository is based on the executable call:

\[
\mathrm{compute}
(
\eta,
L,
\mu_{\rm eff}
).
\]

---

# 10. API-version check

The API version should be recorded before the validation chain begins.

Example Python check:

`from geo_external_operator import api_version`

Then:

`print(api_version())`

The validated test environment used API version:

\[
1.
\]

The archival release must record the value returned by its own frozen environment.

---

# 11. Native test suite

Before using the External Operator as a validation dependency, run its own native tests.

Command:

`pytest -vv`

The native suite should pass before this repository's higher-level GEO-Hubble tests are considered meaningful.

The previously observed clean test execution included successful checks for:

- API behavior;
- independence between `mu_eff` and `eta`;
- canonical radial law;
- projection norm closure;
- reconstruction closure.

A frozen release should preserve the full test output.

---

# 12. Why native tests run first

This repository should not diagnose its own Hubble derivation using an upstream executable that is already failing its own consistency tests.

The validation order must therefore be:

1. install External Operator;
2. run native External Operator tests;
3. confirm native tests pass;
4. run GEO-Hubble project tests.

This ordering isolates upstream failures from errors in the present repository.

---

# 13. Core API contract used here

The principal External Operator function accepts the following conceptual inputs:

\[
\eta,
\]

\[
L,
\]

\[
\mu_{\rm eff}.
\]

The architecture used in the present demonstration sets

\[
\eta=0.6
\]

and

\[
L=0
\]

while permitting

\[
\mu_{\rm eff}
\]

to vary independently.

The resulting radial response must satisfy

\[
R=\mu_{\rm eff}^{1/3}.
\]

---

# 14. Important input distinction

The External Operator API demonstrates an important architectural distinction:

\[
\boxed{
\eta
\text{ and }
\mu_{\rm eff}
\text{ are separate inputs.}
}
\]

Therefore the executable implementation does not require the universal identity

\[
\mu_{\rm eff}=\eta.
\]

This is one reason the External Operator is useful for the corrected GEO-Hubble demonstration.

---

# 15. Fields used by this repository

The principal output fields used in the present validation are:

`eta`

`mu_eff`

`R`

`Phi`

`alpha`

`projected_observable`

`projected_complementary`

`reconstructed_observable`

`reconstructed_complementary`

`projection_norm_error`

`reconstruction_observable_error`

`reconstruction_complementary_error`

Other fields may be retained for broader GEO studies but are not required for the minimal Hubble projection proof.

---

# 16. Radial-law validation

For each supplied

\[
\mu_{\rm eff},
\]

the engine must return

\[
R
\]

such that

\[
\boxed{
R^3=\mu_{\rm eff}.
}
\]

The present project verifies this independently using direct numerical evaluation.

This test ensures that the radial law is not silently replaced with

\[
R=\eta^{1/3}.
\]

---

# 17. Projection validation

The engine output

`projected_observable`

is compared against the analytic result

\[
A'
=
A\cos\theta+B\sin\theta.
\]

For the canonical state,

\[
A=0.6,
\]

\[
B=0.4,
\]

and

\[
\theta=\frac{\pi}{4},
\]

the expected result is

\[
\boxed{
A'
=
\frac1{\sqrt2}.
}
\]

The External Operator should reproduce this value to floating-point precision.

---

# 18. Complementary projection validation

The engine output

`projected_complementary`

is compared against

\[
B'
=
-A\sin\theta+B\cos\theta.
\]

For the canonical state,

\[
\boxed{
B'
=
-\frac{0.2}{\sqrt2}.
}
\]

This provides a second independent coordinate check.

---

# 19. Reconstruction validation

The projected coordinates should reconstruct the original conservative state.

The expected outputs are

\[
A_{\rm rec}\approx0.6
\]

and

\[
B_{\rm rec}\approx0.4.
\]

The reconstruction errors should remain at floating-point precision.

---

# 20. Projection-factor calculation

The present repository does not ask the External Operator to return a hard-coded Hubble factor.

Instead, it reconstructs

\[
f_c=\sqrt{\eta}
\]

and obtains

\[
A'
\]

from the engine.

It then calculates

\[
\boxed{
P_{\rm GEO}
=
\frac{f_c}{A'}.
}
\]

This design is intentional.

The factor must emerge from independent quantities rather than being stored as a target constant.

---

# 21. Closed-form audit

After reconstructing the factor numerically, the result is compared with the analytic identity

\[
\boxed{
P_{\rm GEO}
=
\sqrt{\frac65}.
}
\]

The analytic expression is used as a validation target only after the engine factor has been reconstructed.

The engine calculation itself must not simply return the analytic target by assignment.

---

# 22. Hubble calculation

Only after the projection factor has passed validation may a baseline Hubble value be supplied.

The present reference baseline is

\[
H_{\rm base}=67.4.
\]

The numerical prediction is then

\[
H_{\rm pred}
=
P_{\rm GEO}H_{\rm base}.
\]

The current reference output is

\[
73.833000751696.
\]

The local Hubble measurement is not used to construct this value.

---

# 23. No upstream source modification for the Hubble result

The GEO External Operator must not be modified so that its projection output yields the desired Hubble value.

In particular, the following are prohibited for the canonical reproduction:

- altering \(\eta\) to match local \(H_0\);
- altering \(\theta\) to match local \(H_0\);
- altering projection coefficients;
- changing `projected_observable` manually;
- assigning a Hubble-specific `mu_eff` solely to reproduce a target;
- replacing the radial law with a fitted relation.

---

# 24. Historical compatibility code

The External Operator may contain adapters designed to preserve historical GEO applications.

Such compatibility code must be distinguished from the core engine.

If an adapter imposes

\[
\mu_H:=\eta,
\]

that behavior must not be interpreted as a universal statement of the core GEO architecture.

The corrected Hubble demonstration does not depend on such an adapter.

---

# 25. Why the core engine is used directly

The current project calls the core operator because the scientific question is:

> Does the canonical geometry itself produce the fixed projection structure after the radial notation issue is removed?

Using the core operator directly avoids importing historical application assumptions into the test.

---

# 26. Reproducibility environment record

Before public release, generate an environment record.

Recommended commands:

`python --version`

`pip --version`

`pip freeze`

`cmake --version`

`gcc --version`

or the compiler actually used.

Also record:

`uname -a`

This information should be saved into a results or provenance log.

---

# 27. Recommended environment file

A frozen environment summary may be stored as:

`results/environment.txt`

It should include:

- operating system;
- Python version;
- pip version;
- compiler version;
- CMake version;
- NumPy version;
- SciPy version;
- pytest version;
- External Operator commit;
- External Operator API version;
- present repository commit.

---

# 28. Required native test log

The full External Operator test output should be preserved as:

`results/external_operator_pytest.txt`

This allows reviewers to verify that the dependency passed its own validation independently of the Hubble scripts.

---

# 29. Required core audit log

A direct API audit should be preserved as:

`results/external_operator_api_audit.txt`

It should record at minimum:

- API version;
- result fields;
- canonical projection output;
- radial response;
- reconstruction output;
- norm error.

---

# 30. Required radial/projection-independence audit

The radial/projection-independence audit is preserved in:

`results/03_radial_projection_console.log`

and

`results/03_radial_projection_independence.txt`

The console log preserves the complete execution trace.

The TXT file preserves the concise human-readable audit result.

Together these files document the variation of the effective radial state
while the canonical GEO architecture remains fixed. They are used to verify
that the radial response changes with \(\mu_{m eff}\) while the canonical
projection factor remains unchanged in the tested implementation.

---

# 31. Required projection comparison log

The analytic-versus-engine comparison should be preserved as:

`results/02_projection_check.txt`

It should report:

\[
A'_{\rm analytic},
\]

\[
A'_{\rm engine},
\]

\[
B'_{\rm analytic},
\]

\[
B'_{\rm engine},
\]

and their differences.

---

# 32. Version-freezing procedure

Immediately before archival release:

1. update both upstream repositories;
2. choose the exact revisions to freeze;
3. record the commit hashes;
4. verify clean working trees;
5. rerun installation from a clean environment;
6. rerun native tests;
7. rerun the complete GEO-Hubble validation;
8. commit the resulting provenance metadata;
9. tag the project release.

The frozen release must not point to moving branch names alone.

A commit hash is required.

---

# 33. Reproduction from submodules

If submodules are used, a reviewer should be able to obtain the exact project with:

`git clone --recurse-submodules <repository-url>`

If the repository was already cloned without submodules:

`git submodule update --init --recursive`

The submodule commit pointers then serve as part of the frozen provenance.

---

# 34. Reproduction without submodules

If submodules are not used, the exact required commits must be written explicitly into:

`provenance/GEO_ORIGINAL.md`

and

`provenance/EXTERNAL_OPERATOR.md`

The reproduction instructions must then tell the reviewer to checkout those commits manually.

Example concept:

`git checkout <frozen-commit>`

No branch tip should be assumed to remain unchanged over time.

---

# 35. Separation from GEO External Operator v2

The user's broader GEO software ecosystem may contain additional versions such as a more complete External Operator v2.

The present repository should not silently switch implementations during a frozen reproduction.

The first release should identify exactly which operator implementation was used.

If a v2 cross-check is later added, it should be documented as an independent validation layer rather than replacing the v1 result without provenance.

---

# 36. Why a second implementation can be useful

A future cross-check using a second implementation may test whether

\[
A'=\frac1{\sqrt2}
\]

and

\[
P_{\rm GEO}=\sqrt{\frac65}
\]

are reproduced by independently organized code paths.

Such a test could strengthen implementation-level confidence.

However, agreement between two implementations would still be a mathematical/software validation, not direct observational evidence.

---

# 37. Security and scientific integrity rule

External source code must be obtained from the recorded upstream repository.

Unknown third-party forks should not be substituted silently.

If a fork or local patch is used, its provenance and differences must be documented explicitly.

---

# 38. Final dependency principle

The external-source policy is:

\[
\boxed{
\text{reference, freeze, verify, do not silently merge}.
}
\]

The original GEO framework remains the mathematical provenance source.

The GEO External Operator remains the executable implementation.

The GEO-Hubble Geometric Projection repository remains the derivation and reproducibility layer.

Keeping these roles separate is part of the scientific audit trail.

---

# 39. Final reproduction chain

A clean independent reproduction should follow:

**Clone GEO-Hubble Geometric Projection**

↓

**Obtain frozen GEO original source**

↓

**Obtain frozen GEO External Operator**

↓

**Create clean Python environment**

↓

**Install External Operator**

↓

**Run External Operator native tests**

↓

**Run GEO-Hubble analytic tests**

↓

**Run projection comparison**

↓

**Run radial independence sweep**

↓

**Reconstruct projection factor**

↓

**Apply supplied baseline Hubble value**

↓

**Generate final reproducibility summary**

No observational Hubble target is used before the final comparison stage.

---

# 40. Status

Current external-dependency status:

- Upstream GEO original repository identified — COMPLETE
- Upstream GEO External Operator identified — COMPLETE
- Isolated External Operator clone created — COMPLETE
- Python environment created — COMPLETE
- External Operator installed — COMPLETE
- Public API tested — COMPLETE
- API version checked — COMPLETE
- Native tests executed — COMPLETE
- Radial law tested — COMPLETE
- Projection tested — COMPLETE
- Reconstruction tested — COMPLETE
- Projection factor reconstructed — COMPLETE
- Frozen upstream commit hashes — PENDING
- Frozen environment log — PENDING
- Public release submodule strategy — PENDING

The pending items must be completed before archival release.
