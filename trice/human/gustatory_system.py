"""Computational taste-perception state surface."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class GustatorySystem:
    sweet: float = 0.0
    salty: float = 0.0
    sour: float = 0.0
    bitter: float = 0.0
    umami: float = 0.0

    def ingest(self, values: dict[str, float] | None = None) -> dict[str, float]:
        source = values or {}
        for name in ("sweet", "salty", "sour", "bitter", "umami"):
            setattr(self, name, max(0.0, min(1.0, float(source.get(name, 0.0)))))
        return {
            "taste_sweet": self.sweet,
            "taste_salty": self.salty,
            "taste_sour": self.sour,
            "taste_bitter": self.bitter,
            "taste_umami": self.umami,
        }
