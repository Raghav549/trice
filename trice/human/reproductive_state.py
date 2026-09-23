"""Reproductive-system state boundary.

This is an explicit computational state surface, not a claim of a complete
biological reproductive simulator.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class ReproductiveState:
    reproductive_maturity: float = 0.0
    gonadal_activity: float = 0.0
    cycle_phase: float = 0.0
    fertility_potential: float = 0.0

    def clamp(self) -> None:
        for name in (
            "reproductive_maturity",
            "gonadal_activity",
            "cycle_phase",
            "fertility_potential",
        ):
            setattr(self, name, max(0.0, min(1.0, float(getattr(self, name)))))
