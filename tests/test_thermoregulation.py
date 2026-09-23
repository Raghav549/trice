from trice.physiology.thermoregulation import ThermoregulationModel
def test_temperature_control():
    s=ThermoregulationModel().step(ambient=.85,activity=.7,hydration=.8)
    assert 0<=s["core_temperature"]<=1
