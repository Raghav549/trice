"""Immune-inspired surveillance and recovery subsystem."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, Mapping

from ..core.module import ModuleContext, StatefulModule
from ..core.types import OrganismState


@dataclass
class Detector:
    pattern: str
    threshold: float = 0.5
    strength: float = 1.0


class ImmuneModule(StatefulModule):
    name = "immune"

    def __init__(self) -> None:
        super().__init__()
        self.detectors: Dict[str, Detector] = {}
        self.memory: Dict[str, float] = {}
        self.surveillance = 0.0
        self.recovery = 0.0

    def register_detector(self, name: str, threshold: float = 0.5) -> None:
        self.detectors[name] = Detector(name, threshold)

    def observe(self, anomaly_score: float, key: str = "default") -> None:
        anomaly_score = min(1.0, max(0.0, float(anomaly_score)))
        self.surveillance = anomaly_score
        self.memory[key] = max(self.memory.get(key, 0.0), anomaly_score)

    def step(self, state: OrganismState, context: ModuleContext, dt: float = 1.0) -> Mapping[str, float]:
        anomaly = float(context.signals.get("anomaly", 0.0))
        damage = float(context.signals.get("damage", anomaly))
        self.observe(anomaly)
        self.recovery = max(0.0, min(1.0, self.recovery + (damage - self.recovery) * 0.15 * max(dt, 0.0)))
        return {
            "immune": self.surveillance,
            "stress": min(1.0, state.stress + 0.1 * self.surveillance),
        }
