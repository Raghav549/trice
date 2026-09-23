"""Declarative coupling map for cross-system signals."""
from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class Coupling:
    source: str
    signal: str
    target: str
    gain: float = 1.0


@dataclass
class CouplingGraph:
    couplings: list[Coupling] = field(default_factory=list)

    def add(self, source: str, signal: str, target: str, gain: float = 1.0) -> None:
        if not source or not signal or not target:
            raise ValueError("source, signal and target are required")
        self.couplings.append(Coupling(source, signal, target, float(gain)))

    def targets_for(self, source: str, signal: str) -> tuple[Coupling, ...]:
        return tuple(c for c in self.couplings if c.source == source and c.signal == signal)

    def validate(self) -> None:
        for c in self.couplings:
            if not c.source or not c.signal or not c.target:
                raise ValueError("invalid coupling")
