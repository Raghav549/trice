from trice.human.body_state import HumanState
from trice.human.physiology_bridge import export_human_state, ingest_body_state


def test_physiology_bridge_round_trip_surface():
    human = HumanState()
    ingest_body_state(
        human,
        {"body_energy": 0.8, "glucose": 0.6, "oxygen": 0.9, "temperature": 1.01, "stress": 0.2, "attention": 0.7, "arousal": 0.5},
    )
    exported = export_human_state(human)
    assert exported["body_energy"] == 0.8
    assert exported["stress"] == 0.2
