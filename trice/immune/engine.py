"""Adaptive immune-surveillance abstraction."""
from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class ImmuneEngine:
    baseline: float = 0.5
    inflammation: float = 0.0
    memory: dict[str, float] = field(default_factory=dict)

    def observe(self, antigen: str, novelty: float) -> float:
        novelty = max(0.0, min(1.0, float(novelty)))
        prior = self.memory.get(str(antigen), 0.0)
        response = max(novelty, 1.0 - prior)
        self.memory[str(antigen)] = min(1.0, prior + 0.1 * response)
        self.inflammation = min(1.0, self.inflammation + 0.25 * response)
        return response

    def step(self, dt: float, stress: float = 0.0, damage: float = 0.0) -> dict[str, float]:
        dt = max(0.0, float(dt))
        stress = max(0.0, min(1.0, float(stress)))
        damage = max(0.0, min(1.0, float(damage)))
        drive = damage * 0.7 + stress * 0.1
        self.inflammation += (drive - self.inflammation * 0.6) * dt
        self.inflammation = max(0.0, min(1.0, self.inflammation))
        surveillance = max(0.0, min(1.0, self.baseline + 0.4 * self.inflammation))
        return {
            "immune_surveillance": surveillance,
            "immune_inflammation": self.inflammation,
            "immune_memory_size": float(len(self.memory)),
        }
