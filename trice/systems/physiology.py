"""Deterministic organ-level physiological abstractions.

These are executable computational models for simulation, not clinical or
one-to-one replicas of human physiology.
"""
from __future__ import annotations
from dataclasses import dataclass
from math import exp


def clamp(x: float, lo: float = 0.0, hi: float = 1.0) -> float:
    return max(lo, min(hi, float(x)))


@dataclass
class CardiovascularModel:
    heart_rate: float = 0.5
    vascular_tone: float = 0.5
    oxygen_delivery: float = 0.5

    def step(self, demand: float, stress: float, dt: float = 1.0) -> dict[str, float]:
        demand = clamp(demand)
        stress = clamp(stress)
        target_hr = clamp(0.35 + 0.45 * demand + 0.20 * stress)
        self.heart_rate += (target_hr - self.heart_rate) * (1.0 - exp(-dt / 3.0))
        self.oxygen_delivery = clamp(self.heart_rate * (1.0 - 0.25 * self.vascular_tone))
        return {"heart_rate": self.heart_rate, "oxygen_delivery": self.oxygen_delivery}


@dataclass
class RespiratoryModel:
    ventilation: float = 0.5
    oxygenation: float = 0.5
    carbon_dioxide_load: float = 0.2

    def step(self, metabolic_demand: float, dt: float = 1.0) -> dict[str, float]:
        target = clamp(0.25 + 0.70 * clamp(metabolic_demand))
        self.ventilation += (target - self.ventilation) * (1.0 - exp(-dt / 2.0))
        self.carbon_dioxide_load = clamp(self.carbon_dioxide_load + 0.08 * metabolic_demand - 0.12 * self.ventilation * dt)
        self.oxygenation = clamp(0.15 + 0.85 * self.ventilation - 0.20 * self.carbon_dioxide_load)
        return {
            "ventilation": self.ventilation,
            "oxygenation": self.oxygenation,
            "carbon_dioxide_load": self.carbon_dioxide_load,
        }


@dataclass
class RenalModel:
    hydration: float = 0.7
    electrolyte_balance: float = 0.7
    waste_load: float = 0.1

    def step(self, fluid_input: float, metabolic_load: float, dt: float = 1.0) -> dict[str, float]:
        self.hydration = clamp(self.hydration + (0.18 * fluid_input - 0.10 * metabolic_load) * dt)
        self.waste_load = clamp(self.waste_load + 0.06 * metabolic_load * dt - 0.08 * self.hydration * dt)
        self.electrolyte_balance = clamp(1.0 - abs(0.65 - self.hydration) * 0.9 - self.waste_load * 0.15)
        return {
            "hydration": self.hydration,
            "electrolyte_balance": self.electrolyte_balance,
            "waste_load": self.waste_load,
        }


@dataclass
class DigestiveMetabolicModel:
    nutrient_pool: float = 0.5
    glucose: float = 0.5
    energy_flux: float = 0.5

    def step(self, intake: float, activity: float, dt: float = 1.0) -> dict[str, float]:
        intake = clamp(intake)
        activity = clamp(activity)
        self.nutrient_pool = clamp(self.nutrient_pool + 0.22 * intake * dt - 0.08 * dt)
        self.glucose = clamp(self.glucose + 0.18 * intake - 0.10 * activity)
        self.energy_flux = clamp(0.20 + 0.55 * self.nutrient_pool + 0.35 * self.glucose - 0.20 * activity)
        return {
            "nutrient_pool": self.nutrient_pool,
            "glucose": self.glucose,
            "energy_flux": self.energy_flux,
        }


@dataclass
class NeuroEndocrineModel:
    stress: float = 0.2
    arousal: float = 0.3
    hormone_tone: float = 0.4

    def step(self, sensory_load: float, threat: float, dt: float = 1.0) -> dict[str, float]:
        sensory_load = clamp(sensory_load)
        threat = clamp(threat)
        target_stress = clamp(0.15 + 0.65 * threat + 0.20 * sensory_load)
        self.stress += (target_stress - self.stress) * (1.0 - exp(-dt / 4.0))
        self.arousal = clamp(0.20 + 0.55 * sensory_load + 0.35 * self.stress)
        self.hormone_tone = clamp(0.25 + 0.60 * self.stress - 0.20 * (1.0 - self.arousal))
        return {
            "stress": self.stress,
            "arousal": self.arousal,
            "hormone_tone": self.hormone_tone,
        }
