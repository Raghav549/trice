"""Framework-neutral train/infer interface."""
from __future__ import annotations

from typing import Protocol, Sequence


class ModelInterface(Protocol):
    def predict(self, observation: Sequence[float]) -> Sequence[float]:
        ...

    def update(self, observation: Sequence[float], target: Sequence[float]) -> float:
        ...
