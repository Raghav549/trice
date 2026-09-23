from trice.ai.environment import Environment

def test_environment_observation_action():
    e=Environment({"energy":.5})
    s=e.apply({"movement":.2})
    assert s["movement"]==.2
