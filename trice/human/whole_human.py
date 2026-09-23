"""Public facade for the integrated high-level human abstraction."""
from __future__ import annotations

from dataclasses import dataclass, field

from .human_model import HumanModel
from .validation import validate_human_output
from .whole_body_step import WholeBodyState


@dataclass
class WholeHuman:
    """Combine the existing computational body with the expanded human layer."""

    model: HumanModel = field(default_factory=HumanModel)
    physiology: WholeBodyState = field(default_factory=WholeBodyState)

    def step(self, dt: float, inputs: dict[str, float] | None = None) -> dict[str, float]:
        primary = self.model.step(dt, inputs)
        secondary = self.physiology.step(dt, inputs)
        combined = {**primary, **secondary}
        validate_human_output(combined)
        return combined
