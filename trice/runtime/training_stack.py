"""Scalable-training capability registry."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class TrainingStack:
    framework: str = "pytorch"
    parallelism: str = "single"
    engine: str = "native"
    precision: str = "fp32"

    def validate(self) -> None:
        allowed_frameworks = {"pytorch", "jax", "tensorflow"}
        allowed_parallelism = {"single", "fsdp", "deepspeed", "megatron"}
        if self.framework not in allowed_frameworks:
            raise ValueError(f"unsupported framework: {self.framework}")
        if self.parallelism not in allowed_parallelism:
            raise ValueError(f"unsupported parallelism: {self.parallelism}")
        if not self.engine:
            raise ValueError("engine cannot be empty")
        if not self.precision:
            raise ValueError("precision cannot be empty")
