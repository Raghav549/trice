"""Closed-loop agent combining TRICE body state with a policy."""
from __future__ import annotations

from dataclasses import dataclass, field

from trice.body import ComputationalBody
from .loop import AgentLoop


@dataclass
class BodyAgent:
    """Observe the body, choose an action, then feed the action back to it."""

    body: ComputationalBody = field(default_factory=ComputationalBody)
    loop: AgentLoop = field(default_factory=AgentLoop)

    def step(self, dt: float, external: dict[str, float] | None = None) -> dict[str, float]:
        external = dict(external or {})
        current = self.body.step(dt, external)
        observations = {
            "energy": current.get("body_energy", current.get("energy", 0.5)),
            "stress": external.get("stress", 0.0),
            "reward": external.get("reward", 0.0),
        }
        action = self.loop.step(observations)
        next_inputs = dict(external)
        next_inputs.update({"movement": action.get("movement", 0.0)})
        next_inputs["_agent_attention"] = action.get("attention", 0.0)
        self.body.step(dt, next_inputs)
        return dict(action)
