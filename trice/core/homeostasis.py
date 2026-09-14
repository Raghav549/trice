"""Homeostatic regulation primitives."""
from __future__ import annotations

from dataclasses import dataclass

from .types import OrganismState


@dataclass(frozen=True)
class HomeostaticTarget:
    """Target range for a regulated scalar variable."""

    minimum: float
    maximum: float
    recovery_rate: float = 0.1

    @property
    def midpoint(self) -> float:
        return (self.minimum + self.maximum) / 2.0

    def error(self, value: float) -> float:
        if value < self.minimum:
            return self.minimum - value
        if value > self.maximum:
            return self.maximum - value
        return self.midpoint - value


@dataclass
class HomeostasisEngine:
    """Simple bounded regulator used by the initial TRICE simulation."""

    energy: HomeostaticTarget = HomeostaticTarget(0.2, 1.0, 0.08)
    temperature: HomeostaticTarget = HomeostaticTarget(0.95, 1.05, 0.05)
    stress: HomeostaticTarget = HomeostaticTarget(0.0, 0.6, 0.08)

    def regulate(self, state: OrganismState, dt: float = 1.0) -> OrganismState:
        """Move regulated state variables toward safe target regions."""
        state.energy = self._move(state.energy, self.energy, dt)
        state.temperature = self._move(state.temperature, self.temperature, dt)
        state.stress = max(0.0, min(1.0, self._move(state.stress, self.stress, dt)))
        return state

    @staticmethod
    def _move(value: float, target: HomeostaticTarget, dt: float) -> float:
        delta = target.error(value) * target.recovery_rate * max(0.0, dt)
        return value + delta
