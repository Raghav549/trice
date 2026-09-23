from trice.human.renal_state import RenalState


def test_renal_state_produces_urine_and_filtration():
    state = RenalState()
    result = state.step(1.0, hydration=0.8, solute_load=0.2)
    assert result["renal_filtration"] > 0
    assert result["urine_volume"] > 0
