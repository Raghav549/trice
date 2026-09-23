from trice.ai.trajectory import Trajectory


def test_trajectory_stores_transitions():
    trajectory = Trajectory()
    trajectory.append({"energy": 1.0}, {"movement": 0.2}, 0.5, {"energy": 0.9})
    assert len(trajectory) == 1
    assert trajectory.rewards() == [0.5]
