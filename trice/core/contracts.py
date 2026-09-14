"""Strict runtime contracts shared by TRICE subsystems."""
from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Mapping


class ModuleStatus(str, Enum):
    ACTIVE = "ACTIVE"
    DEGRADED = "DEGRADED"
    QUARANTINED = "QUARANTINED"
    RECOVERING = "RECOVERING"


@dataclass(frozen=True)
class Signal:
    """A typed inter-system signal."""

    source: str
    target: str
    name: str
    value: float
    time: float
    metadata: Mapping[str, str] = field(default_factory=dict)

    def __post_init__(self) -> None:
        if not self.source or not self.target or not self.name:
            raise ValueError("signal source, target and name are required")


@dataclass
class ModuleHealth:
    """Operational health state for a simulated subsystem."""

    status: ModuleStatus = ModuleStatus.ACTIVE
    score: float = 1.0
    fault_count: int = 0

    def validate(self) -> None:
        if not 0.0 <= self.score <= 1.0:
            raise ValueError("health score must be within [0, 1]")
        if self.fault_count < 0:
            raise ValueError("fault_count cannot be negative")
