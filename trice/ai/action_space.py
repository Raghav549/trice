"""Validated action representation for the body-agent boundary."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Action:
    movement: float = 0.0
    attention: float = 0.0

    def __post_init__(self) -> None:
        if not -1.0 <= self.movement <= 1.0:
            raise ValueError("movement must be within [-1, 1]")
        if not 0.0 <= self.attention <= 1.0:
            raise ValueError("attention must be within [0, 1]")

    def as_dict(self) -> dict[str, float]:
        return {"movement": self.movement, "attention": self.attention}
