from trice.human.pancreatic_state import PancreaticState


def test_pancreatic_state_tracks_glucose_and_food():
    result = PancreaticState().step(0.1, glucose=0.9, food=0.8)
    assert result["pancreatic_insulin"] > 0.5
    assert result["digestive_enzyme_output"] > 0.5
