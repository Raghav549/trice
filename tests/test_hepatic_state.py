from trice.human.hepatic_state import HepaticState


def test_hepatic_state_processes_loads():
    result = HepaticState().step(1.0, nutrient_load=0.8, toxin_load=0.4)
    assert result["hepatic_protein_processing"] > 0.5
    assert result["hepatic_detox_load"] > 0
