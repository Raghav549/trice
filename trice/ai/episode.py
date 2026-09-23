"""Episode lifecycle and return accounting for TRICE agents."""
from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Episode:
    """Collect rewards and terminal state for one environment rollout."""

    rewards: list[float] = field(default_factory=list)
    done: bool = False
    info: dict[str, float] = field(default_factory=dict)

    def add(self, reward: float) -> None:
        if self.done:
            raise RuntimeError("cannot add reward after episode is done")
        self.rewards.append(float(reward))

    def finish(self, **info: float) -> None:
        self.done = True
        self.info = {str(k): float(v) for k, v in info.items()}

    @property
    def return_sum(self) -> float:
        return sum(self.rewards)

    def reset(self) -> None:
        self.rewards.clear()
        self.done = False
        self.info.clear()
