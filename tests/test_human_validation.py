import pytest

from trice.human.validation import validate_human_output


def test_human_validation_accepts_whole_body_state():
    validate_human_output({"water": 0.5, "alertness": 0.8})


def test_human_validation_rejects_invalid_bounded_value():
    with pytest.raises(ValueError):
        validate_human_output({"water": 2.0})
