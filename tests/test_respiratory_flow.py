from trice.physiology.respiratory_flow import RespiratoryFlowModel

def test_air_path():
    s=RespiratoryFlowModel().step(air=2,metabolic_demand=.6)
    assert s["oxygenation"]>=0
