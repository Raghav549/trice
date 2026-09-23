"""Whole-human state validation helpers."""
from __future__ import annotations

from collections.abc import Mapping

from trice.core.resource_guard import validate_finite_state


def validate_human_output(state: Mapping[str, float]) -> None:
    validate_finite_state(state)
    bounded = (
        "vision", "hearing", "touch", "smell", "taste", "vestibular",
        "sensory_gain", "signal_fidelity", "reflex_readiness",
        "blood_oxygen_capacity", "innate_activity", "adaptive_activity",
        "inflammation", "fluid_accumulation", "water", "sodium", "potassium",
        "renal_filtration", "balance", "posture", "sleep_pressure",
        "alertness", "sweating", "shivering",
    )
    for key in bounded:
        if key in state and not 0.0 <= float(state[key]) <= 1.0:
            raise ValueError(f"{key} must be within [0, 1]")
