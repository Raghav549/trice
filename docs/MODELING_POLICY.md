# TRICE Modeling Policy

## Three levels of fidelity

### Level A — mechanistic
Use when published equations or experimentally supported mechanisms are sufficiently specified for the intended simulation scale.

### Level B — validated abstraction
Use a reduced-order model that preserves the behavior needed by a stated experiment and document the omitted mechanisms.

### Level C — conceptual abstraction
Use symbolic/state variables when science does not yet support a mechanistic implementation at the chosen scale. These variables must never be described as proof of a biological process.

## Rule for every component

Each biological component must declare:

- biological scope;
- computational role;
- fidelity level;
- state variables;
- inputs and outputs;
- coupling dependencies;
- validation evidence;
- known limitations;
- test coverage.

## Brain and consciousness

TRICE may simulate neural dynamics, memory, valuation, attention, stress, sleep/wake state, and other measurable or computational correlates. It must not claim that a simulation has subjective consciousness, feelings, self-awareness, or human identity merely because its outputs appear human-like.

## Parameters

A parameter is either:

- empirically sourced;
- derived from an explicitly documented experiment;
- estimated for computational stability; or
- a free research parameter.

Only the first two may be described as biological measurements, and their source must be recorded.
