# TRICE Production-Readiness Contract

TRICE is a scientific simulation framework. "Production-ready" means reproducible, observable, testable, versioned, recoverable, and explicit about model limitations. It does **not** mean biological equivalence to a human being.

## Release gates

A release candidate must satisfy:

1. `python -m pytest -q` passes.
2. Coverage registry validation passes and every tracked biological component has a declared status.
3. No component marked `IMPLEMENTED` lacks automated tests.
4. Simulation runs are deterministic when a seed is supplied.
5. Checkpoints can be serialized and restored without changing the deterministic trajectory.
6. Research outputs include provenance metadata and model/configuration versions.
7. Invalid state values are rejected early by validation contracts.
8. Failures are observable through structured telemetry rather than silent fallbacks.
9. Scientific approximations are labeled and are not presented as measured human physiology.
10. No production path depends on fake success responses, placeholder buttons, or untested external services.

## Operational principles

- Prefer small deterministic components over opaque global state.
- Keep simulation, research experiments, and presentation/API layers separate.
- Treat configuration and random seeds as first-class experiment inputs.
- Store checkpoints and experiment metadata together.
- Make model assumptions explicit and reviewable.
- Never silently substitute a different biological mechanism for a requested one.

## Scope boundary

TRICE remains a computational research simulator. Any future wet-lab implementation, genetic engineering, pathogen work, or work with living tissues requires separate biosafety, ethics, institutional, and regulatory review.
