"""Safety and numerical validation utilities for the simulator."""
from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Iterable, Mapping


class StateValidationError(ValueError):
    """Raised when a simulated physiological state is invalid."""


def finite(value: float, name: str) -> float:
    value = float(value)
    if not math.isfinite(value):
        raise StateValidationError(f"{name} must be finite, got {value!r}")
    return value


def bounded(value: float, name: str, low: float, high: float) -> float:
    value = finite(value, name)
    if not low <= value <= high:
        raise StateValidationError(f"{name}={value} outside [{low}, {high}]")
    return value


def validate_vector(values: Mapping[str, float], required: Iterable[str] = ()) -> None:
    missing = [key for key in required if key not in values]
    if missing:
        raise StateValidationError(f"missing required state fields: {missing}")
    for key, value in values.items():
        finite(value, key)


@dataclass(frozen=True)
class HealthReport:
    """Numerical health report for one simulation step."""

    finite: bool
    bounded_energy: bool
    state_count: int
    errors: tuple[str, ...] = ()

    @property
    def ok(self) -> bool:
        return self.finite and self.bounded_energy and not self.errors
