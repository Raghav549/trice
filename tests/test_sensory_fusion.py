from trice.human.sensory_fusion import fuse, salience


def test_sensory_fusion():
    assert salience({"vision": 1, "hearing": 0}) == 0.5
    assert fuse({"vision": 1}, 0.0) > 0.0
