# Upstream GEO References

This directory records the public upstream GEO repositories used by the
GEO-Hubble Geometric Projection reproducibility project.

The upstream projects are referenced rather than vendored so that the
provenance of the mathematical framework and of the executable operator
remains explicit.

## 1. GEO Hidden Geometry Framework

Repository:

https://github.com/LeoTorreblanca/GEO-hidden-geometry-framework

Reference commit used in this audit:

7606fef854aeb3fbe6082a78f7794209eab850da

Role in this project:

- source framework for the canonical GEO architecture;
- canonical partition and coupling relations;
- geometric projection concepts;
- radial-law provenance;
- historical development of the GEO-Hubble interpretation.

The corrected general radial relation used by this repository is

R^3 = mu_eff

or equivalently

R = mu_eff^(1/3).

The parameter mu_eff is kept distinct from the canonical partition
parameter eta.

## 2. GEO External Operator

Repository:

https://github.com/LeoTorreblanca/GEO-External-Operator

Reference commit used in this audit:

003402ef5edff2fe6efa020c368de8064e711732

Reference API version:

1

Role in this project:

- independent executable realization of the GEO operator;
- verification of the canonical partition;
- verification of the membrane projection;
- verification of forward and inverse reconstruction;
- verification of radial-law behavior;
- numerical comparison with the analytic derivations in this repository.

## 3. Provenance boundary

This repository does not modify either upstream project.

The upstream repositories provide the GEO framework and the executable
operator used as references.

This repository provides a focused reconstruction and audit of the
GEO-Hubble geometric-projection argument.

In particular, it distinguishes between:

1. inherited GEO definitions and relations;
2. corrected interpretation of the general radial law;
3. analytic consequences derived from the canonical projection geometry;
4. executable numerical verification;
5. the physical GEO-Hubble application hypothesis.

## 4. Closed-form projection result

For the canonical conservative GEO state,

A + B = 1,

eta = 3/5,

f_c = sqrt(eta),

and for the exact 45-degree membrane,

theta_M = pi/4.

The projected observable coordinate is

A' = A cos(theta_M) + B sin(theta_M).

Because

cos(pi/4) = sin(pi/4) = 1/sqrt(2),

the conservation relation gives

A' = 1/sqrt(2).

Therefore the geometric projection ratio used in this reconstruction is

P_GEO = f_c / A'

and hence

P_GEO = sqrt(3/5) / (1/sqrt(2))
      = sqrt(6/5).

This closed form is an algebraic consequence of the stated canonical
relations. It is not introduced as an independently fitted constant.

## 5. Hubble application boundary

The further identification

H_projected / H_base = P_GEO

is the GEO-Hubble physical application hypothesis examined by this
repository.

The software tests establish the internal mathematical and computational
closure of the stated transformation. They do not, by themselves,
establish that the physical Universe must realize this mapping.
