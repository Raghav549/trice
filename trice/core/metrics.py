"""Metrics for reproducible TRICE experiments."""
from __future__ import annotations

from dataclasses import dataclass
from math import isfinite
from statistics import fmean
from typing import Iterable


@dataclass(frozen=True)
class Metrics:
    steps: int
    mean_energy: float
    final_energy: float
    mean_stress: float
    finite: bool


def summarize(states: Iterable[object]) -> Metrics:
    rows = list(states)
    if not rows:
        return Metrics(0, 0.0, 0.0, 0.0, True)
    energy = [float(s.energy) for s in rows]
    stress = [float(getattr(s, "stress", 0.0)) for s in rows]
    finite = all(isfinite(v) for v in (*energy, *stress))
    return Metrics(
        steps=len(rows),
        mean_energy=fmean(energy),
        final_energy=energy[-1],
        mean_stress=fmean(stress),
        finite=finite,
    )
