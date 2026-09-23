"""Public whole-human organism facade."""
from __future__ import annotations

from dataclasses import dataclass, field

from .human_model import HumanModel


@dataclass
class HumanOrganism:
    """Facade for stepping and observing the integrated human model."""

    model: HumanModel = field(default_factory=HumanModel)

    def step(self, dt: float, inputs: dict[str, float] | None = None) -> dict[str, float]:
        return self.model.step(dt, inputs)

    @property
    def time(self) -> float:
        return self.model.time
