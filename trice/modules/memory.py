"""Adaptive memory primitives."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List

from ..core.module import ModuleContext, StatefulModule
from ..core.types import OrganismState


@dataclass
class MemoryTrace:
    value: float
    salience: float
    age: float = 0.0
    context: str = ""


class MemoryModule(StatefulModule):
    name = "memory"

    def __init__(self, capacity: int = 256, decay: float = 0.002) -> None:
        super().__init__()
        self.capacity = max(1, capacity)
        self.decay = min(1.0, max(0.0, decay))
        self.traces: List[MemoryTrace] = []

    def encode(self, value: float, salience: float = 0.5, context: str = "") -> None:
        trace = MemoryTrace(float(value), max(0.0, min(1.0, salience)), 0.0, context)
        self.traces.append(trace)
        if len(self.traces) > self.capacity:
            self.traces.sort(key=lambda t: (t.salience, -t.age))
            self.traces = self.traces[-self.capacity :]

    def recall(self, context: str = "") -> float:
        candidates = [t for t in self.traces if not context or t.context == context]
        if not candidates:
            return 0.0
        total = sum(max(0.0, t.salience) for t in candidates)
        if total <= 0:
            return sum(t.value for t in candidates) / len(candidates)
        return sum(t.value * t.salience for t in candidates) / total

    def step(self, state: OrganismState, context: ModuleContext, dt: float = 1.0) -> Dict[str, float]:
        dt = max(0.0, dt)
        for trace in self.traces:
            trace.age += dt
            trace.salience = max(0.0, trace.salience * (1.0 - self.decay * dt))
        recalled = self.recall(str(context.environment.get("context", "")))
        return {"memory": recalled}
