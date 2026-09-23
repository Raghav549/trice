"""Numerical safety guards for long-running simulations."""
from __future__ import annotations

import math
from collections.abc import Mapping


def validate_finite_state(state: Mapping[str, float]) -> None:
    """Raise when a state contains NaN/inf or non-numeric values."""
    for name, value in state.items():
        try:
            numeric = float(value)
        except (TypeError, ValueError) as exc:
            raise ValueError(f"state '{name}' is not numeric") from exc
        if not math.isfinite(numeric):
            raise ValueError(f"state '{name}' is not finite")


def clamp01(value: float) -> float:
    return max(0.0, min(1.0, float(value)))
