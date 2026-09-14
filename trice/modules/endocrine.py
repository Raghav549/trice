"""Slow-timescale global modulation inspired by endocrine regulation."""
from __future__ import annotations

from typing import Mapping

from ..core.module import ModuleContext, StatefulModule
from ..core.types import OrganismState


class EndocrineModule(StatefulModule):
    name = "endocrine"

    def __init__(self) -> None:
        super().__init__()
        self.hormones = {
            "cortisol": 0.0,
            "adrenaline": 0.0,
            "melatonin": 0.0,
            "growth": 0.5,
        }

    def step(self, state: OrganismState, context: ModuleContext, dt: float = 1.0) -> Mapping[str, float]:
        stress = max(0.0, min(1.0, state.stress))
        arousal = max(0.0, min(1.0, state.arousal))
        self.hormones["cortisol"] += (stress - self.hormones["cortisol"]) * 0.12 * max(dt, 0.0)
        self.hormones["adrenaline"] += (arousal - self.hormones["adrenaline"]) * 0.18 * max(dt, 0.0)
        self.hormones["melatonin"] += (float(context.environment.get("darkness", 0.0)) - self.hormones["melatonin"]) * 0.08 * max(dt, 0.0)
        return {
            "endocrine": sum(self.hormones.values()) / len(self.hormones),
            "stress": min(1.0, stress + 0.03 * self.hormones["cortisol"]),
        }
