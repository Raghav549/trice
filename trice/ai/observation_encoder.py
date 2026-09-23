"""Stable numeric encoder for the human state observation surface."""
from __future__ import annotations

from collections.abc import Mapping

from trice.core.observations import DEFAULT_KEYS


def encode(observation: Mapping[str, float]) -> list[float]:
    return [float(observation.get(key, 0.0)) for key in DEFAULT_KEYS]
