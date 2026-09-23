"""Top-level whole-human computational orchestrator."""
from __future__ import annotations

from dataclasses import dataclass, field

from trice.body import ComputationalBody
from trice.core.resource_guard import validate_finite_state

from .body_state import HumanState
from .physiology_bridge import export_human_state, ingest_body_state


@dataclass
class HumanModel:
    """Compose the existing body simulator with the human-state architecture."""

    body: ComputationalBody = field(default_factory=ComputationalBody)
    state: HumanState = field(default_factory=HumanState)
    time: float = 0.0

    def step(self, dt: float, inputs: dict[str, float] | None = None) -> dict[str, float]:
        if dt <= 0:
            raise ValueError("dt must be positive")
        body_state = self.body.step(dt, inputs or {})
        validate_finite_state(body_state)
        ingest_body_state(self.state, body_state)
        self.state.lifecycle.step(dt / 31_536_000.0)
        self.state.validate()
        self.time += dt
        result = export_human_state(self.state)
        result["time"] = self.time
        return result
