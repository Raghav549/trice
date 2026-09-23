"""Hormonal regulation state surface."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class EndocrineState:
    insulin: float = 0.5
    glucagon: float = 0.5
    cortisol: float = 0.0
    thyroid_signal: float = 0.5
    adrenaline: float = 0.0
    melatonin: float = 0.0

    def clamp(self) -> None:
        for name in ("insulin", "glucagon", "cortisol", "thyroid_signal", "adrenaline", "melatonin"):
            setattr(self, name, max(0.0, min(1.0, float(getattr(self, name)))))
