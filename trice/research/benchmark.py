"""Small deterministic benchmark harness for TRICE research experiments."""
from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256
import json
from typing import Callable

from ..core.metrics import summarize


@dataclass(frozen=True)
class BenchmarkResult:
    name: str
    steps: int
    digest: str
    metrics: dict[str, float | int | bool]


def run(name: str, organism_factory: Callable[[], object], steps: int = 100, dt: float = 1.0) -> BenchmarkResult:
    if steps < 0:
        raise ValueError("steps must be >= 0")
    organism = organism_factory()
    states = []
    for _ in range(steps):
        states.append(organism.step(dt=dt))
    metrics = summarize(states)
    payload = json.dumps([s.vector() for s in states], sort_keys=True, separators=(",", ":"))
    digest = sha256(payload.encode("utf-8")).hexdigest()
    return BenchmarkResult(
        name=name,
        steps=metrics.steps,
        digest=digest,
        metrics={
            "mean_energy": metrics.mean_energy,
            "final_energy": metrics.final_energy,
            "mean_stress": metrics.mean_stress,
            "finite": metrics.finite,
        },
    )
