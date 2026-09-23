import pytest

from trice.runtime.training_stack import TrainingStack


def test_training_stack_accepts_scalable_modes():
    for mode in ("single", "fsdp", "deepspeed", "megatron"):
        TrainingStack(parallelism=mode).validate()


def test_training_stack_rejects_unknown_framework():
    with pytest.raises(ValueError):
        TrainingStack(framework="unknown").validate()
