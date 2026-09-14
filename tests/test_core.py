from trice.core import EnergyBudget, HomeostasisEngine, OrganismState


def test_energy_budget_never_goes_below_zero():
    budget = EnergyBudget(capacity=1.0, level=0.1)
    budget.consume(10.0)
    assert budget.level == 0.0


def test_homeostasis_moves_state_toward_target():
    state = OrganismState(energy=0.0, temperature=2.0, stress=1.0)
    state = HomeostasisEngine().regulate(state, dt=1.0)
    assert state.energy > 0.0
    assert state.temperature < 2.0
    assert state.stress <= 1.0
