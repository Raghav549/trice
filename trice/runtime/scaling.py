"""Scaling strategy descriptors for distributed training."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ScalingStrategy:
    name: str
    workers: int = 1
    devices_per_worker: int = 1

    @property
    def total_devices(self) -> int:
        return self.workers * self.devices_per_worker

    def validate(self) -> None:
        if self.workers < 1 or self.devices_per_worker < 1:
            raise ValueError("worker and device counts must be >= 1")


CPU_SINGLE = ScalingStrategy("cpu-single")
GPU_SINGLE = ScalingStrategy("gpu-single")
FSDP = ScalingStrategy("fsdp")
DEEPSPEED = ScalingStrategy("deepspeed")
MEGATRON = ScalingStrategy("megatron")
