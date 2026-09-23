"""Framework-neutral training orchestration boundary."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Sequence


@dataclass
class TrainingConfig:
    epochs: int = 1
    learning_rate: float = 1e-3
    batch_size: int = 32

    def validate(self) -> None:
        if self.epochs < 1:
            raise ValueError("epochs must be >= 1")
        if self.learning_rate <= 0:
            raise ValueError("learning_rate must be positive")
        if self.batch_size < 1:
            raise ValueError("batch_size must be >= 1")


def train_loop(
    batches: Sequence[object],
    step_fn: Callable[[object], float],
    config: TrainingConfig | None = None,
) -> list[float]:
    cfg = config or TrainingConfig()
    cfg.validate()
    losses: list[float] = []
    for _ in range(cfg.epochs):
        for batch in batches:
            losses.append(float(step_fn(batch)))
    return losses
