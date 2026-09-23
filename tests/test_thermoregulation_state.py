from trice.human.thermoregulation_state import ThermoregulationState


def test_thermoregulation_produces_regulatory_response():
    state = ThermoregulationState(core_temperature=1.1)
    result = state.step(1.0, ambient_temperature=1.0)
    assert result["sweating"] > 0
    assert result["core_temperature"] < 1.1
