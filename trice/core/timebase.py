"""Deterministic simulation timebase."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Timebase:
    time: float = 0.0
    steps: int = 0

    def advance(self, dt: float) -> float:
        if dt <= 0:
            raise ValueError("dt must be positive")
        self.time += float(dt)
        self.steps += 1
        return self.time
