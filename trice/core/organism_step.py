"""Validated orchestration boundary for a single organism step."""
from __future__ import annotations

from collections.abc import Mapping

from .body_cycle import FullBodyCycle
from .resource_guard import validate_finite_state


def step_checked(
    cycle: FullBodyCycle,
    dt: float,
    inputs: Mapping[str, float] | None = None,
) -> dict[str, float]:
    """Advance a cycle and reject invalid numeric output immediately."""
    state = cycle.step(dt, inputs)
    validate_finite_state(state)
    return state
