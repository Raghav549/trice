# TRICE Production Readiness Standard

TRICE aims for production-grade software engineering while remaining scientifically honest about biological fidelity.

## Release gates

A release candidate must satisfy all of these:

1. `python -m pytest -q` passes.
2. `python -m compileall -q trice` passes.
3. Coverage registry validation passes.
4. No component marked `IMPLEMENTED` lacks a test.
5. Deterministic benchmark digests are reproducible for fixed seed/configuration.
6. Public APIs have type annotations and documented contracts.
7. Checkpoints can be created and restored without silent state loss.
8. Invalid numerical state is detected and reported rather than propagated.
9. Research parameters are separated from measured human physiological constants.
10. Claims of biological equivalence are prohibited unless supported by explicit evidence.

## Operational principle

TRICE is a computational organism simulator/research platform. Production-ready means reliable, reproducible, observable, testable software. It does **not** mean that current code reproduces every mechanism of a living human or solves consciousness.

## Scientific fidelity ladder

`UNMODELED -> PLANNED -> ABSTRACTED -> CALIBRATED -> VALIDATED`

A component must never jump directly from `UNMODELED` to `VALIDATED` without documented evidence and tests.
