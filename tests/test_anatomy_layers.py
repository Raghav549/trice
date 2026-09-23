from trice.human.anatomy_layers import AnatomyPart, BiologicalLayer, CORE_HUMAN_LAYERS


def test_anatomy_part_carries_explicit_layer():
    part = AnatomyPart("heart", BiologicalLayer.ORGAN)
    assert part.layer is BiologicalLayer.ORGAN
    assert not part.modeled
    assert len(CORE_HUMAN_LAYERS) == 6
