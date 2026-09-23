"""Multi-sensory integration into an attention signal."""
from __future__ import annotations

from collections.abc import Mapping


def salience(channels: Mapping[str, float]) -> float:
    values = [abs(float(value)) for value in channels.values()]
    if not values:
        return 0.0
    return max(0.0, min(1.0, sum(values) / len(values)))


def fuse(channels: Mapping[str, float], previous_attention: float = 0.0) -> float:
    current = salience(channels)
    previous = max(0.0, min(1.0, float(previous_attention)))
    return 0.7 * current + 0.3 * previous
