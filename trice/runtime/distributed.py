"""Distributed execution boundary without hard dependency on a cluster runtime."""
from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass
from typing import Callable, TypeVar

T = TypeVar("T")
R = TypeVar("R")


@dataclass(frozen=True)
class DistributedPlan:
    workers: int = 1
    backend: str = "local"

    def validate(self) -> None:
        if self.workers < 1:
            raise ValueError("workers must be >= 1")


def map_batches(
    batches: Sequence[T],
    fn: Callable[[T], R],
    plan: DistributedPlan | None = None,
) -> list[R]:
    cfg = plan or DistributedPlan()
    cfg.validate()
    # The local implementation is the reference semantics. Ray/Dask/Spark
    # adapters can replace this function without changing callers.
    return [fn(batch) for batch in batches]
