# TRICE Architecture Contract

## Status semantics

- `IMPLEMENTED`: executable code exists and has tests.
- `ABSTRACTED`: executable computational approximation exists, with documented scientific limits.
- `PLANNED`: interface/specification exists but implementation is incomplete.
- `UNMODELED`: identified as required biological coverage but no computational model exists yet.

## Whole-body rule

The registry is authoritative. A component cannot be silently omitted. Every organ, major tissue/system, and important molecular/cellular subsystem must have an entry or a documented reason for exclusion from a particular simulation profile.

## Interface contract

Every subsystem should expose:

- state schema
- inputs
- outputs/events
- update function
- dependencies
- resource costs
- invariants/homeostatic targets
- validation tests
- evidence/reference metadata

## Layers

1. Physical/chemical substrate
2. Molecular/genetic regulation
3. Organelle/cellular physiology
4. Tissue/cell-population dynamics
5. Organs
6. Organ systems
7. Neural/immune/endocrine coupling
8. Brain/cognition/action
9. Whole-organism regulation
10. Adaptation/evolution/reconfiguration

## Required system families

- nervous and sensory
- brain/cognition
- endocrine
- immune/lymphatic
- cardiovascular/hematologic
- respiratory
- digestive/hepatobiliary
- renal/urinary
- musculoskeletal
- integumentary
- reproductive/developmental
- cellular/molecular/genetic
- metabolic/resource

## Scientific integrity

TRICE may implement computational abstractions of biology. It must not claim that an abstraction is an exact human physiological replica. Consciousness, subjective experience, emotion, and complex disease mechanisms require explicit uncertainty labels where appropriate.

## Real implementation rule

No placeholder success paths. If a feature is not implemented, the program must report its actual status. Tests must exercise state transitions and coupling, not just imports.
