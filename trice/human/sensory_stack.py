"""Unified sensory channel normalization."""
from __future__ import annotations

CHANNELS = ("vision", "hearing", "touch", "smell", "taste", "balance", "pain", "temperature")


def normalize_senses(inputs: dict[str, float] | None = None) -> dict[str, float]:
    source = inputs or {}
    return {
        channel: max(-1.0, min(1.0, float(source.get(channel, 0.0))))
        for channel in CHANNELS
    }
