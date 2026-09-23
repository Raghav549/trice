from trice.core.energy import EnergyBudget
from trice.core.energy_guard import validate_energy_budget


def test_energy_budget_validation():
    budget = EnergyBudget(capacity=2.0, level=1.0)
    validate_energy_budget(budget)
    budget.level = 2.0
    validate_energy_budget(budget)
