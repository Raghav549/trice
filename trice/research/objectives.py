"""Objective functions for multi-criteria computational organism experiments."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence


@dataclass(frozen=True)
class Objective:
    name: str
    weight: float = 1.0
    maximize: bool = True

    def __post_init__(self) -> None:
        if not self.name:
            raise ValueError("objective name is required")
        if self.weight < 0:
            raise ValueError("objective weight must be non-negative")

    def contribution(self, value: float) -> float:
        signed = float(value) if self.maximize else -float(value)
        return self.weight * signed


def multi_objective_score(values: Sequence[float], objectives: Sequence[Objective]) -> float:
    if len(values) != len(objectives):
        raise ValueError("values and objectives must have equal length")
    total_weight = sum(o.weight for o in objectives)
    if total_weight == 0:
        raise ValueError("at least one objective must have positive weight")
    return sum(o.contribution(v) for v, o in zip(values, objectives)) / total_weight
