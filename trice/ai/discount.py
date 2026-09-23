"""Return and discounted-return utilities."""
from __future__ import annotations

from collections.abc import Sequence


def discounted_returns(rewards: Sequence[float], gamma: float = 0.99) -> list[float]:
    if not 0.0 <= gamma <= 1.0:
        raise ValueError("gamma must be within [0, 1]")
    result = [0.0] * len(rewards)
    running = 0.0
    for index in range(len(rewards) - 1, -1, -1):
        running = float(rewards[index]) + gamma * running
        result[index] = running
    return result
