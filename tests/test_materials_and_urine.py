from trice.physiology.body_materials import MaterialPools
from trice.physiology.urinary_flow import UrinaryFlowModel

def test_material_pools_track_nutrients():
    p=MaterialPools()
    s=p.ingest(proteins=3,fats=2,omega3=1,vitamins=1,water=4)
    assert s["proteins"]==3
    assert s["omega3"]==1
    assert s["water"]==4

def test_urinary_flow_can_form_and_void():
    m=UrinaryFlowModel()
    m.step(renal_filtration=1,hydration=.7,waste_load=.6)
    s=m.step(renal_filtration=1,hydration=.7,waste_load=.6,void=1)
    assert s["bladder_volume"]==0
