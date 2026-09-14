"""Multi-modal sensory transduction abstraction."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class SensoryModel:
    vision: float = 0.0
    hearing: float = 0.0
    touch: float = 0.0
    pain: float = 0.0
    temperature: float = 0.0
    smell: float = 0.0
    taste: float = 0.0
    vestibular: float = 0.0

    def ingest(self, signals: dict[str, float]) -> dict[str, float]:
        channels = ("vision", "hearing", "touch", "pain", "temperature", "smell", "taste", "vestibular")
        for name in channels:
            if name in signals:
                value = float(signals[name])
                setattr(self, name, max(-1.0, min(1.0, value)))
        return {name: float(getattr(self, name)) for name in channels}

    def step(self, dt: float, decay: float = 1.0) -> dict[str, float]:
        factor = max(0.0, min(1.0, float(dt) * max(0.0, float(decay))))
        state = self.ingest({})
        for name, value in state.items():
            setattr(self, name, value * max(0.0, 1.0 - factor))
        return self.ingest({})
