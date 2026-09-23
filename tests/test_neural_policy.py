import pytest

from trice.ai.neural_policy import NeuralPolicyConfig, TorchNeuralPolicy


def test_neural_policy_config():
    NeuralPolicyConfig().validate()


def test_torch_neural_policy_is_optional():
    try:
        policy = TorchNeuralPolicy()
    except RuntimeError:
        pytest.skip("torch not installed")
    result = policy.predict([0.0] * 9)
    assert len(result) == 2
