"""Framework-neutral distributed learning protocol.

Concrete deployments may map this protocol to Ray, Dask, Spark, FSDP or
DeepSpeed, while TRICE retains deterministic reference semantics here.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Sequence, TypeVar

T = TypeVar("T")
R = TypeVar("R")


@dataclass(frozen=True)
class WorkerSpec:
    worker_id: int
    device: str = "cpu"


def shard(items: Sequence[T], workers: int) -> list[list[T]]:
    if workers < 1:
        raise ValueError("workers must be >= 1")
    return [list(items[i::workers]) for i in range(workers)]


def distributed_map(
    items: Sequence[T],
    fn: Callable[[T], R],
    workers: int = 1,
) -> list[R]:
    return [fn(item) for item in items]
