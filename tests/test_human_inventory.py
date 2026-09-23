from trice.human.anatomy_layers import BiologicalLayer
from trice.human.inventory import COMPONENTS, inventory_by_layer


def test_human_inventory_spans_all_layers():
    assert {component.layer for component in COMPONENTS} == set(BiologicalLayer)
    assert inventory_by_layer(BiologicalLayer.ORGAN)
