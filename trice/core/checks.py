"""Reusable simulation invariant checks."""
from __future__ import annotations

from collections.abc import Mapping


def require_keys(state: Mapping[str, float], keys: tuple[str, ...]) -> None:
    missing = [key for key in keys if key not in state]
    if missing:
        raise KeyError("missing state keys: " + ", ".join(missing))


def require_range(value: float, minimum: float, maximum: float, name: str) -> None:
    numeric = float(value)
    if numeric < minimum or numeric > maximum:
        raise ValueError(f"{name} must be within [{minimum}, {maximum}]")
