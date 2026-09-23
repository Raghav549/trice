from trice.human.proprioception import Proprioception


def test_proprioception_tracks_joints():
    result = Proprioception().ingest({"knee": 0.4, "elbow": -0.2})
    assert result["proprioception_confidence"] == 1.0
    assert result["proprioception_joint_count"] == 2.0
