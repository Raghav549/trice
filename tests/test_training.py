import pytest

from trice.runtime.training import TrainingConfig, train_loop


def test_training_loop_collects_losses():
    losses = train_loop([1, 2], lambda batch: 1.0 / batch, TrainingConfig(epochs=2))
    assert losses == [1.0, 0.5, 1.0, 0.5]


def test_training_config_validates():
    with pytest.raises(ValueError):
        TrainingConfig(epochs=0).validate()
