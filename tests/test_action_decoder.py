import pytest

from trice.ai.action_decoder import decode


def test_action_decoder():
    action = decode([3.0, -1.0])
    assert action.movement == 1.0
    assert action.attention == 0.0


def test_action_decoder_requires_two_outputs():
    with pytest.raises(ValueError):
        decode([0.0])
