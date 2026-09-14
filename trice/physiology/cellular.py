"""Cellular energy, membrane and organelle state abstraction."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class CellularModel:
    membrane_potential: float = 0.0
    atp: float = 1.0
    calcium: float = 1.0
    oxidative_stress: float = 0.0
    protein_synthesis: float = 1.0
    dna_damage: float = 0.0

    def step(self, dt: float, workload: float = 0.2, damage_input: float = 0.0) -> dict[str, float]:
        dt = max(0.0, float(dt))
        workload = max(0.0, min(1.0, float(workload)))
        damage_input = max(0.0, min(1.0, float(damage_input)))
        self.atp += (1.0 - workload - self.atp) * min(1.0, dt * 0.25)
        self.oxidative_stress += (workload * 0.2 - self.oxidative_stress * 0.12) * dt
        self.dna_damage += (damage_input + self.oxidative_stress * 0.03 - self.dna_damage * 0.08) * dt
        self.calcium += (1.0 - self.calcium) * min(1.0, dt * 0.3) + 0.01 * workload * dt
        self.membrane_potential += (-self.membrane_potential - 0.02 * workload) * min(1.0, dt)
        self.protein_synthesis = max(0.0, 1.0 - 0.5 * self.dna_damage - 0.2 * self.oxidative_stress)
        self.atp = max(0.0, min(1.5, self.atp))
        self.calcium = max(0.0, min(2.0, self.calcium))
        self.oxidative_stress = max(0.0, min(2.0, self.oxidative_stress))
        self.dna_damage = max(0.0, min(2.0, self.dna_damage))
        return {
            "membrane_potential": self.membrane_potential,
            "atp": self.atp,
            "cellular_calcium": self.calcium,
            "oxidative_stress": self.oxidative_stress,
            "protein_synthesis": self.protein_synthesis,
            "dna_damage": self.dna_damage,
        }
