import pytest

from trice.runtime.config import RuntimeConfig


def test_runtime_config_accepts_stack_choices():
    RuntimeConfig(
        backend="cpu",
        framework="pytorch",
        distributed_backend="ray",
        tracker="mlflow",
        precision="bf16",
    ).validate()


def test_runtime_config_rejects_unknown_values():
    with pytest.raises(ValueError):
        RuntimeConfig(framework="unknown").validate()
