"""Multi-scale cellular and molecular state abstractions."""
from __future__ import annotations
from dataclasses import dataclass
from math import exp


def clip(x: float) -> float:
    return max(0.0, min(1.0, float(x)))


@dataclass
class MolecularState:
    dna_integrity: float = 1.0
    protein_pool: float = 0.5
    metabolite_pool: float = 0.5
    repair_activity: float = 0.4

    def step(self, stress: float, energy: float, dt: float = 1.0) -> dict[str, float]:
        stress = clip(stress)
        energy = clip(energy)
        damage = 0.025 * stress * dt
        repair = 0.035 * self.repair_activity * energy * dt
        self.dna_integrity = clip(self.dna_integrity - damage + repair)
        self.protein_pool = clip(self.protein_pool + 0.06 * energy * dt - 0.04 * stress * dt)
        self.metabolite_pool = clip(self.metabolite_pool + 0.05 * energy * dt - 0.035 * stress * dt)
        self.repair_activity = clip(self.repair_activity + 0.04 * stress - 0.02 * energy)
        return self.__dict__.copy()


@dataclass
class CellState:
    membrane_potential: float = 0.5
    mitochondrial_energy: float = 0.6
    protein_synthesis: float = 0.5
    waste_load: float = 0.1
    viability: float = 1.0

    def step(self, demand: float, stress: float, dt: float = 1.0) -> dict[str, float]:
        demand = clip(demand)
        stress = clip(stress)
        self.mitochondrial_energy = clip(self.mitochondrial_energy + 0.05 * (1.0 - demand) - 0.06 * demand - 0.025 * stress)
        self.protein_synthesis = clip(self.protein_synthesis + 0.04 * self.mitochondrial_energy - 0.035 * stress)
        self.waste_load = clip(self.waste_load + 0.045 * demand - 0.03 * self.mitochondrial_energy)
        self.membrane_potential = clip(0.55 + 0.25 * self.mitochondrial_energy - 0.20 * stress)
        self.viability = clip(self.viability + 0.03 * self.mitochondrial_energy - 0.06 * self.waste_load - 0.05 * stress)
        return self.__dict__.copy()
