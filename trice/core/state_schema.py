"""Schema helpers for stable simulation state surfaces."""
from __future__ import annotations

from dataclasses import dataclass
from collections.abc import Mapping


@dataclass(frozen=True)
class StateField:
    name: str
    minimum: float | None = None
    maximum: float | None = None

    def validate(self, value: float) -> None:
        numeric = float(value)
        if self.minimum is not None and numeric < self.minimum:
            raise ValueError(f"{self.name} below minimum")
        if self.maximum is not None and numeric > self.maximum:
            raise ValueError(f"{self.name} above maximum")


@dataclass(frozen=True)
class StateSchema:
    fields: tuple[StateField, ...]

    def validate(self, state: Mapping[str, float]) -> None:
        for field in self.fields:
            if field.name in state:
                field.validate(state[field.name])

    @property
    def names(self) -> tuple[str, ...]:
        return tuple(field.name for field in self.fields)
