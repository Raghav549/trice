"""Canonical observation extraction from integrated body state."""
from __future__ import annotations

from collections.abc import Mapping


DEFAULT_KEYS = (
    "body_energy",
    "glucose",
    "heart_rate",
    "oxygen",
    "temperature",
    "stress",
    "attention",
    "pain",
    "arousal",
)


def observe(state: Mapping[str, float]) -> dict[str, float]:
    """Return a stable agent-facing observation schema with safe defaults."""
    result: dict[str, float] = {}
    for key in DEFAULT_KEYS:
        value = state.get(key, 0.0)
        result[key] = float(value)
    return result
