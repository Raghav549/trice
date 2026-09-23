"""Energy-budget validation helpers."""
from __future__ import annotations

from .energy import EnergyBudget


def validate_energy_budget(budget: EnergyBudget) -> None:
    if budget.capacity < 0:
        raise ValueError("energy capacity cannot be negative")
    if budget.level < 0 or budget.level > budget.capacity:
        raise ValueError("energy level must remain within [0, capacity]")
    if budget.basal_rate < 0:
        raise ValueError("basal_rate cannot be negative")
