from trice.human.fluid_balance import FluidBalance


def test_fluid_balance_remains_bounded():
    state = FluidBalance()
    result = state.step(1.0, water_intake=1.0, loss=0.2)
    assert 0.0 <= result["water"] <= 1.0
    assert 0.0 <= result["sodium"] <= 1.0
    assert 0.0 <= result["potassium"] <= 1.0
