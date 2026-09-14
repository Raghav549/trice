"""Lightweight metrics and event accounting for production simulations."""
from __future__ import annotations

from collections import Counter
from dataclasses import dataclass, field
from time import perf_counter
from typing import Dict


@dataclass
class Telemetry:
    """Collect deterministic simulation metrics without external dependencies."""

    counters: Counter[str] = field(default_factory=Counter)
    gauges: Dict[str, float] = field(default_factory=dict)
    timings_ms: Dict[str, float] = field(default_factory=dict)

    def increment(self, name: str, amount: int = 1) -> None:
        if amount < 0:
            raise ValueError("counter increments must be non-negative")
        self.counters[name] += amount

    def set_gauge(self, name: str, value: float) -> None:
        self.gauges[name] = float(value)

    def time_block(self, name: str):
        return _Timing(self, name)

    def snapshot(self) -> dict:
        return {
            "counters": dict(self.counters),
            "gauges": dict(self.gauges),
            "timings_ms": dict(self.timings_ms),
        }


class _Timing:
    def __init__(self, telemetry: Telemetry, name: str) -> None:
        self.telemetry = telemetry
        self.name = name
        self.started = 0.0

    def __enter__(self):
        self.started = perf_counter()
        return self

    def __exit__(self, exc_type, exc, tb):
        elapsed = (perf_counter() - self.started) * 1000.0
        self.telemetry.timings_ms[self.name] = elapsed
        return False
