"""Computational olfactory-perception state surface."""
from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class OlfactorySystem:
    receptor_gain: float = 1.0
    molecules: dict[str, float] = field(default_factory=dict)
    salience: float = 0.0

    def ingest(self, molecules: dict[str, float] | None = None) -> dict[str, float]:
        source = molecules or {}
        self.molecules = {
            str(name): max(0.0, min(1.0, float(value)))
            for name, value in source.items()
        }
        self.salience = max(
            0.0,
            min(1.0, sum(self.molecules.values()) / max(1, len(self.molecules))),
        )
        return {
            "olfactory_receptor_gain": self.receptor_gain,
            "olfactory_salience": self.salience,
        }
