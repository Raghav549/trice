"""Minimal experiment descriptor for reproducible simulation runs."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping


@dataclass(frozen=True)
class Experiment:
    name: str
    seed: int = 0
    parameters: Mapping[str, float] | None = None

    def normalized_parameters(self) -> dict[str, float]:
        return {
            key: float((self.parameters or {})[key])
            for key in sorted(self.parameters or {})
        }
