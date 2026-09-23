import pytest

from trice.core.resource_guard import clamp01, validate_finite_state


def test_validate_finite_state_accepts_finite_values():
    validate_finite_state({"energy": 0.5, "temperature": 1.0})


@pytest.mark.parametrize("value", [float("nan"), float("inf"), float("-inf")])
def test_validate_finite_state_rejects_non_finite_values(value):
    with pytest.raises(ValueError):
        validate_finite_state({"energy": value})


def test_clamp01():
    assert clamp01(-2.0) == 0.0
    assert clamp01(0.4) == 0.4
    assert clamp01(2.0) == 1.0
