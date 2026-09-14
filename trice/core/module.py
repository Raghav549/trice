"""Extensible subsystem contract for TRICE."""
from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Dict, Mapping

from .types import OrganismState


@dataclass
class ModuleContext:
    """Shared context available to computational body modules."""

    environment: Dict[str, float] = field(default_factory=dict)
    signals: Dict[str, float] = field(default_factory=dict)


class BodyModule(ABC):
    """Base interface for every simulated body subsystem."""

    name: str = "unnamed"

    @abstractmethod
    def step(self, state: OrganismState, context: ModuleContext, dt: float = 1.0) -> Mapping[str, float]:
        """Advance the module and return state updates."""
        raise NotImplementedError


class StatefulModule(BodyModule):
    """Convenience implementation for scalar internal module state."""

    def __init__(self) -> None:
        self.internal: Dict[str, float] = {}

    def update(self, **values: float) -> None:
        self.internal.update({key: float(value) for key, value in values.items()})
