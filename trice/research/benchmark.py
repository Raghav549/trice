"""Deterministic, fail-fast benchmark harness for TRICE experiments."""
from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256
import json
from math import isfinite
from typing import Callable

from ..core.metrics import summarize


@dataclass(frozen=True)
class BenchmarkResult:
    name: str
    steps: int
    digest: str
    metrics: dict[str, float | int | bool]


def run(
    name: str,
    organism_factory: Callable[[], object],
    steps: int = 100,
    dt: float = 1.0,
) -> BenchmarkResult:
    """Run a deterministic organism benchmark and return a content digest."""
    if not name.strip():
        raise ValueError("name must be non-empty")
    if steps < 0:
        raise ValueError("steps must be >= 0")
    dt = float(dt)
    if not isfinite(dt) or dt <= 0.0:
        raise ValueError("dt must be finite and > 0")

    organism = organism_factory()
    states = [organism.step(dt=dt) for _ in range(steps)]
    metrics = summarize(states)
    if not metrics.finite:
        raise FloatingPointError("benchmark produced non-finite metrics")

    vectors = [s.vector() for s in states]
    payload = json.dumps(vectors, sort_keys=True, separators=(",", ":"))
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
