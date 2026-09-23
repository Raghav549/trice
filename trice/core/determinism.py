"""Determinism checks for simulation inputs and outputs."""
from __future__ import annotations

from collections.abc import Mapping


def canonical_inputs(inputs: Mapping[str, float] | None) -> dict[str, float]:
    """Normalize input ordering and numeric types for reproducible runs."""
    return {key: float(inputs[key]) for key in sorted(inputs or {})}


def states_equal(left: Mapping[str, float], right: Mapping[str, float], tol: float = 1e-12) -> bool:
    if tol < 0:
        raise ValueError("tol cannot be negative")
    if set(left) != set(right):
        return False
    return all(abs(float(left[key]) - float(right[key])) <= tol for key in left)
