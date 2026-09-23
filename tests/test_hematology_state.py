from trice.human.hematology_state import HematologyState


def test_hematology_oxygen_capacity():
    state = HematologyState(red_cells=0.8, hemoglobin_capacity=0.9)
    assert state.oxygen_capacity() == 0.72


def test_hematology_clamps():
    state = HematologyState(red_cells=2, platelets=-1)
    state.clamp()
    assert state.red_cells == 1.0
    assert state.platelets == 0.0
