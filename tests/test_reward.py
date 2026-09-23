from trice.ai.reward import RewardConfig, compute_reward


def test_reward_includes_task_and_survival_terms():
    value = compute_reward(
        alive=True, energy=0.8, stress=0.2, task_reward=1.0,
        config=RewardConfig(),
    )
    assert value > 1.0


def test_dead_state_gets_survival_penalty():
    assert compute_reward(alive=False, energy=0.0, stress=0.0) < 0.0
