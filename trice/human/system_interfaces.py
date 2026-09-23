"""Canonical subsystem interface used by whole-human orchestration."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol


class HumanSubsystem(Protocol):
    name: str

    def step(self, dt: float, inputs: dict[str, float]) -> dict[str, float]:
        ...


@dataclass(frozen=True)
class SubsystemSpec:
    name: str
    domain: str
    inputs: tuple[str, ...] = ()
    outputs: tuple[str, ...] = ()
    status: str = "ABSTRACTED"
