import pytest

from trice.ai.action_space import Action


def test_action_validates_and_serializes():
    assert Action(0.5, 0.75).as_dict() == {
        "movement": 0.5, "attention": 0.75
    }


@pytest.mark.parametrize("kwargs", [
    {"movement": 2.0},
    {"movement": -2.0},
    {"attention": 2.0},
])
def test_action_rejects_out_of_range(kwargs):
    with pytest.raises(ValueError):
        Action(**kwargs)
