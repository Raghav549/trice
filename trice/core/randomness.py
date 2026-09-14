"""Deterministic randomness primitives for reproducible TRICE experiments."""
from __future__ import annotations

import random
from dataclasses import dataclass
from typing import Sequence, TypeVar

T = TypeVar("T")


@dataclass
class DeterministicRNG:
    """Small reproducible RNG wrapper used by simulation and evolution code."""

    seed: int = 0

    def __post_init__(self) -> None:
        self._rng = random.Random(self.seed)

    def random(self) -> float:
        return self._rng.random()

    def uniform(self, a: float, b: float) -> float:
        return self._rng.uniform(a, b)

    def randint(self, a: int, b: int) -> int:
        return self._rng.randint(a, b)

    def choice(self, values: Sequence[T]) -> T:
        if not values:
            raise IndexError("cannot choose from an empty sequence")
        return self._rng.choice(values)

    def fork(self, salt: int) -> "DeterministicRNG":
        """Create a deterministic child stream without mutating the parent."""
        mixed = (self.seed * 1_000_003 + int(salt) * 97_003) & 0xFFFFFFFF
        return DeterministicRNG(mixed)
