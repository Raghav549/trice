from trice.physiology.cardiovascular import CardiovascularModel
from trice.physiology.cellular import CellularModel
from trice.physiology.digestion import DigestionModel
from trice.physiology.metabolism import MetabolismModel
from trice.physiology.motor import MotorModel
from trice.physiology.renal import RenalModel
from trice.physiology.respiratory import RespiratoryModel
from trice.physiology.sensory import SensoryModel


def test_models_produce_finite_state() -> None:
    models = [
        CardiovascularModel(), CellularModel(), DigestionModel(), MetabolismModel(),
        MotorModel(), RenalModel(), RespiratoryModel(), SensoryModel(),
    ]
    outputs = [
        models[0].step(0.1), models[1].step(0.1), models[2].step(0.1),
        models[3].step(0.1), models[4].step(0.1), models[5].step(0.1),
        models[6].step(0.1), models[7].step(0.1),
    ]
    for state in outputs:
        assert state
        assert all(isinstance(value, (int, float)) for value in state.values())


def test_sensory_channels_are_bounded() -> None:
    model = SensoryModel()
    state = model.ingest({"vision": 5, "pain": -5})
    assert state["vision"] == 1.0
    assert state["pain"] == -1.0
