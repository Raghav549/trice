"""Reward shaping primitives kept separate from biological state."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class RewardConfig:
    survival_weight: float = 1.0
    energy_weight: float = 0.25
    stress_penalty: float = 0.25
    task_weight: float = 1.0


def compute_reward(
    *,
    alive: bool,
    energy: float,
    stress: float,
    task_reward: float = 0.0,
    config: RewardConfig | None = None,
) -> float:
    cfg = config or RewardConfig()
    reward = cfg.task_weight * float(task_reward)
    reward += cfg.survival_weight if alive else -cfg.survival_weight
    reward += cfg.energy_weight * float(energy)
    reward -= cfg.stress_penalty * max(0.0, float(stress))
    return reward
