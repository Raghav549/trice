"""Explicit sensory-organ state surfaces."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class SensoryOrgans:
    vision: float = 0.0
    hearing: float = 0.0
    touch: float = 0.0
    smell: float = 0.0
    taste: float = 0.0
    vestibular: float = 0.0

    def ingest(self, inputs: dict[str, float] | None = None) -> dict[str, float]:
        source = inputs or {}
        for name in ("vision", "hearing", "touch", "smell", "taste", "vestibular"):
            setattr(self, name, max(-1.0, min(1.0, float(source.get(name, 0.0)))))
        return {
            "vision": self.vision,
            "hearing": self.hearing,
            "touch": self.touch,
            "smell": self.smell,
            "taste": self.taste,
            "vestibular": self.vestibular,
        }
