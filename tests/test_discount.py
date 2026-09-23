import pytest

from trice.ai.discount import discounted_returns


def test_discounted_returns():
    assert discounted_returns([1.0, 1.0], gamma=0.5) == [1.5, 1.0]


def test_discount_gamma_is_validated():
    with pytest.raises(ValueError):
        discounted_returns([1.0], gamma=1.1)
