"""Thin training adapter boundary for optional deep-learning stacks."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable


@dataclass
class TrainingAdapter:
    framework: str = "pytorch"
    strategy: str = "single"

    def validate(self) -> None:
        if self.framework not in {"pytorch", "jax", "tensorflow"}:
            raise ValueError(f"unsupported framework: {self.framework}")
        if self.strategy not in {"single", "fsdp", "deepspeed", "megatron"}:
            raise ValueError(f"unsupported strategy: {self.strategy}")

    def step(self, batch: Any, loss_fn: Callable[[Any], float]) -> float:
        self.validate()
        return float(loss_fn(batch))
