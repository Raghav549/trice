from trice.physiology.cell_cycle import CellCycleModel
def test_cellular_state():
    s=CellCycleModel().step(oxygen=.8,nutrients=.8,damage=.2)
    assert 0<=s["dna_integrity"]<=1
