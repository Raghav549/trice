"""Core state contracts for TRICE.

The data model deliberately stays biology-inspired rather than claiming
one-to-one physiological equivalence.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, Mapping


@dataclass
class OrganismState:
    """Minimal whole-organism state vector.

    Additional subsystem state is carried in ``modules`` so new biological
    mechanisms can be introduced without breaking the core contract.
    """

    time: float = 0.0
    energy: float = 1.0
    temperature: float = 1.0
    neural: float = 0.0
    immune: float = 0.0
    endocrine: float = 0.0
    memory: float = 0.0
    cardiovascular: float = 0.0
    respiratory: float = 0.0
    digestion: float = 0.0
    renal: float = 0.0
    motor: float = 0.0
    sensory: float = 0.0
    stress: float = 0.0
    arousal: float = 0.0
    modules: Dict[str, float] = field(default_factory=dict)

    def vector(self) -> Dict[str, float]:
        """Return a serializable scalar state view."""
        base = {
            "time": self.time,
            "energy": self.energy,
            "temperature": self.temperature,
            "neural": self.neural,
            "immune": self.immune,
            "endocrine": self.endocrine,
            "memory": self.memory,
            "cardiovascular": self.cardiovascular,
            "respiratory": self.respiratory,
            "digestion": self.digestion,
            "renal": self.renal,
            "motor": self.motor,
            "sensory": self.sensory,
            "stress": self.stress,
            "arousal": self.arousal,
        }
        base.update(self.modules)
        return base

    @classmethod
    def from_mapping(cls, values: Mapping[str, float]) -> "OrganismState":
        """Create state from a mapping while preserving unknown module fields."""
        known = {
            "time", "energy", "temperature", "neural", "immune", "endocrine",
            "memory", "cardiovascular", "respiratory", "digestion", "renal",
            "motor", "sensory", "stress", "arousal",
        }
        kwargs = {k: float(v) for k, v in values.items() if k in known}
        modules = {k: float(v) for k, v in values.items() if k not in known}
        kwargs["modules"] = modules
        return cls(**kwargs)
