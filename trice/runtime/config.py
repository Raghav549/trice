"""Central runtime configuration for the multi-backend AI stack."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class RuntimeConfig:
    backend: str = "cpu"
    framework: str = "pytorch"
    distributed_backend: str = "local"
    tracker: str = "none"
    precision: str = "fp32"

    def validate(self) -> None:
        if self.backend not in {"cpu", "torch"}:
            raise ValueError(f"unknown backend: {self.backend}")
        if self.framework not in {"pytorch", "jax", "tensorflow"}:
            raise ValueError(f"unknown framework: {self.framework}")
        if self.distributed_backend not in {"local", "ray", "dask", "spark"}:
            raise ValueError(f"unknown distributed backend: {self.distributed_backend}")
        if self.tracker not in {"none", "wandb", "mlflow"}:
            raise ValueError(f"unknown tracker: {self.tracker}")
        if self.precision not in {"fp32", "fp16", "bf16"}:
            raise ValueError(f"unknown precision: {self.precision}")
