from trice.human.behavior import BehavioralState
from trice.human.drive_model import DriveModel
from trice.human.internal_state import InternalState


def test_drive_model_maps_homeostasis_to_drives():
    drives = DriveModel().update(
        InternalState(glucose=0.1, hydration=0.5, body_energy=0.4),
        BehavioralState(),
    )
    assert drives.hunger > 0
    assert drives.thirst > 0
    assert drives.fatigue > 0
