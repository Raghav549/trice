"""Deterministic state-flow container for whole-human integration."""
from __future__ import annotations

from dataclasses import dataclass, field

from .body_state import HumanState


@dataclass
class StateFlow:
    """Carry environmental, internal, behavioral and mind state together."""

    human: HumanState = field(default_factory=HumanState)

    def snapshot(self) -> dict[str, float]:
        return {
            "age_years": self.human.lifecycle.age_years,
            "alive": 1.0 if self.human.lifecycle.alive else 0.0,
            "energy": self.human.internal.body_energy,
            "hydration": self.human.internal.hydration,
            "oxygen": self.human.internal.oxygen,
            "glucose": self.human.internal.glucose,
            "pain": self.human.internal.pain,
            "hunger": self.human.behavior.hunger,
            "thirst": self.human.behavior.thirst,
            "fatigue": self.human.behavior.fatigue,
            "attention": self.human.mind.attention,
            "arousal": self.human.mind.arousal,
            "valence": self.human.mind.valence,
        }
