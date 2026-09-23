from trice.physiology.intake import IntakeModel


def test_intake_routes_food_water_and_air():
    model = IntakeModel()
    state = model.step(food=2.0, water=1.0, air=3.0, dt=1.0)
    assert state["food_intake"] > 0
    assert state["water_intake"] > 0
    assert state["air_intake"] > 0
    assert state["swallowed"] <= state["food_intake"]
