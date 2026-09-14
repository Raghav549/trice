"""Explicit dependency graph for whole-organism coupling.

The graph is computational: edges describe information/state coupling in the
simulator and do not claim anatomical identity or physiological equivalence.
"""
from __future__ import annotations

from dataclasses import dataclass
from math import isfinite
from typing import Iterable


@dataclass(frozen=True)
class Coupling:
    source: str
    target: str
    channel: str
    weight: float = 1.0

    def __post_init__(self) -> None:
        if not self.source.strip() or not self.target.strip() or not self.channel.strip():
            raise ValueError("coupling source, target, and channel must be non-empty")
        if not isfinite(float(self.weight)):
            raise ValueError("coupling weight must be finite")


DEFAULT_COUPLINGS: tuple[Coupling, ...] = (
    Coupling("sensory", "neural", "afferent", 1.0),
    Coupling("neural", "motor", "motor_command", 1.0),
    Coupling("neural", "endocrine", "autonomic_modulation", 0.6),
    Coupling("endocrine", "metabolism", "hormonal_modulation", 0.8),
    Coupling("immune", "endocrine", "inflammatory_signal", 0.5),
    Coupling("immune", "neural", "neuromodulatory_signal", 0.3),
    Coupling("cardiovascular", "respiratory", "gas_transport_feedback", 0.7),
    Coupling("respiratory", "cardiovascular", "oxygenation_feedback", 0.8),
    Coupling("digestion", "metabolism", "nutrient_flux", 1.0),
    Coupling("metabolism", "renal", "solute_load", 0.5),
    Coupling("renal", "endocrine", "fluid_electrolyte_feedback", 0.7),
    Coupling("metabolism", "neural", "energy_availability", 0.6),
    Coupling("neural", "memory", "encoding_context", 0.9),
    Coupling("memory", "neural", "retrieval_context", 0.9),
    Coupling("stress", "immune", "stress_modulation", 0.4),
    Coupling("stress", "memory", "salience", 0.5),
    Coupling("energy", "all", "resource_budget", 1.0),
    Coupling("sleep", "memory", "consolidation_window", 0.8),
    Coupling("sleep", "immune", "recovery_window", 0.7),
)


class OrganismGraph:
    """Validated immutable coupling topology for a TRICE organism."""

    def __init__(self, couplings: Iterable[Coupling] = DEFAULT_COUPLINGS) -> None:
        self._couplings = tuple(couplings)
        keys = [(c.source, c.target, c.channel) for c in self._couplings]
        if len(keys) != len(set(keys)):
            raise ValueError("duplicate organism coupling")

    def neighbors(self, source: str) -> tuple[str, ...]:
        return tuple(c.target for c in self._couplings if c.source == source)

    def incoming(self, target: str) -> tuple[Coupling, ...]:
        return tuple(c for c in self._couplings if c.target == target)

    def channels(self) -> tuple[Coupling, ...]:
        return self._couplings
