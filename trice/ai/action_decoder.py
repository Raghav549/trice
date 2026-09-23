"""Decode neural outputs into the validated TRICE action space."""
from __future__ import annotations

from collections.abc import Sequence

from .action_space import Action


def decode(values: Sequence[float]) -> Action:
    if len(values) < 2:
        raise ValueError("at least movement and attention outputs are required")
    return Action(
        movement=max(-1.0, min(1.0, float(values[0]))),
        attention=max(0.0, min(1.0, float(values[1]))),
    )
