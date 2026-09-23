from trice.human.oral_airway import OralAirwayState


def test_oral_airway_responds_to_food_and_obstruction():
    result = OralAirwayState().step(0.1, food=0.8, obstruction=0.2)
    assert result["salivary_flow"] > 0.5
    assert result["airway_patency"] == 0.8
