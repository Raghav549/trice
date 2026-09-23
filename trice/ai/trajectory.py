"""Trajectory storage for learning and evaluation."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class Transition:
    observation: dict[str, float]
    action: dict[str, float]
    reward: float
    next_observation: dict[str, float]
    done: bool = False


@dataclass
class Trajectory:
    transitions: list[Transition] = field(default_factory=list)

    def append(
        self,
        observation: dict[str, float],
        action: dict[str, float],
        reward: float,
        next_observation: dict[str, float],
        done: bool = False,
    ) -> None:
        self.transitions.append(
            Transition(
                dict(observation),
                dict(action),
                float(reward),
                dict(next_observation),
                bool(done),
            )
        )

    def rewards(self) -> list[float]:
        return [transition.reward for transition in self.transitions]

    def __len__(self) -> int:
        return len(self.transitions)
