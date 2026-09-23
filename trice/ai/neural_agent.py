"""Closed-loop neural agent over the whole-human state surface."""
from __future__ import annotations

from dataclasses import dataclass, field

from .action_decoder import decode
from .neural_policy import TorchNeuralPolicy
from .observation_encoder import encode
from trice.human.whole_human import WholeHuman


@dataclass
class NeuralAgent:
    human: WholeHuman = field(default_factory=WholeHuman)
    policy: TorchNeuralPolicy | None = None

    def __post_init__(self) -> None:
        if self.policy is None:
            try:
                self.policy = TorchNeuralPolicy()
            except RuntimeError:
                self.policy = None

    def step(self, dt: float, inputs: dict[str, float] | None = None) -> dict[str, float]:
        state = self.human.step(dt, inputs or {})
        observation = encode(state)
        if self.policy is None:
            return {"movement": 0.0, "attention": state.get("attention", 0.0)}
        action = decode(self.policy.predict(observation))
        return action.as_dict()
