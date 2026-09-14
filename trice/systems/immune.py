"""Executable immune-surveillance abstractions for simulation."""
from __future__ import annotations
from dataclasses import dataclass, field
from math import exp


def clip(x: float) -> float:
    return max(0.0, min(1.0, float(x)))


@dataclass
class ImmuneMemory:
    patterns: dict[str, float] = field(default_factory=dict)

    def observe(self, antigen: str, confidence: float, learning_rate: float = 0.08) -> None:
        confidence = clip(confidence)
        old = self.patterns.get(antigen, 0.0)
        self.patterns[antigen] = clip(old + learning_rate * (confidence - old))

    def score(self, antigen: str) -> float:
        return self.patterns.get(antigen, 0.0)


@dataclass
class ImmuneSystem:
    surveillance: float = 0.5
    inflammation: float = 0.0
    recovery: float = 0.5
    memory: ImmuneMemory = field(default_factory=ImmuneMemory)

    def step(self, anomaly: float, damage: float, dt: float = 1.0) -> dict[str, float]:
        anomaly = clip(anomaly)
        damage = clip(damage)
        self.surveillance += (clip(0.35 + 0.65 * anomaly) - self.surveillance) * (1.0 - exp(-dt / 3.0))
        self.inflammation = clip(self.inflammation + 0.18 * anomaly + 0.08 * damage - 0.12 * self.recovery * dt)
        self.recovery = clip(self.recovery + 0.05 * (1.0 - self.inflammation) * dt - 0.04 * damage * dt)
        return {
            "immune_surveillance": self.surveillance,
            "inflammation": self.inflammation,
            "immune_recovery": self.recovery,
        }

    def learn(self, antigen: str, confidence: float) -> None:
        self.memory.observe(antigen, confidence)
