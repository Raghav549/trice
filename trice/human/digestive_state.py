"""Digestive and nutrient-processing state surface."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class DigestiveState:
    stomach_content: float = 0.0
    intestinal_content: float = 0.0
    absorbed_glucose: float = 0.0
    absorbed_amino_acids: float = 0.0
    absorbed_lipids: float = 0.0
    waste: float = 0.0

    def step(self, dt: float, food: float = 0.0) -> dict[str, float]:
        if dt <= 0:
            raise ValueError("dt must be positive")
        food = max(0.0, float(food))
        self.stomach_content = max(0.0, self.stomach_content + food)
        moved = min(self.stomach_content, 0.35 * dt)
        self.stomach_content -= moved
        self.intestinal_content += moved
        absorbed = min(self.intestinal_content, 0.30 * dt)
        self.intestinal_content -= absorbed
        self.absorbed_glucose = min(1.0, self.absorbed_glucose + absorbed * 0.5)
        self.absorbed_amino_acids = min(1.0, self.absorbed_amino_acids + absorbed * 0.3)
        self.absorbed_lipids = min(1.0, self.absorbed_lipids + absorbed * 0.2)
        self.waste = max(0.0, self.waste + max(0.0, moved - absorbed) - 0.05 * dt)
        return {
            "stomach_content": self.stomach_content,
            "intestinal_content": self.intestinal_content,
            "absorbed_glucose": self.absorbed_glucose,
            "absorbed_amino_acids": self.absorbed_amino_acids,
            "absorbed_lipids": self.absorbed_lipids,
            "digestive_waste": self.waste,
        }
