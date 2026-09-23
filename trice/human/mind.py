"""High-level mind state, kept separate from claims about subjective consciousness."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class MindState:
    attention: float = 0.0
    working_memory: float = 0.0
    arousal: float = 0.5
    valence: float = 0.0
    goal_pressure: float = 0.0
    self_model: float = 0.0

    def clamp(self) -> None:
        for name in ("attention", "working_memory", "arousal", "goal_pressure", "self_model"):
            setattr(self, name, max(0.0, min(1.0, float(getattr(self, name)))))
        self.valence = max(-1.0, min(1.0, float(self.valence)))
