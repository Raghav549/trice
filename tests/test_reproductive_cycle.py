import pytest

from trice.human.reproductive_cycle import ReproductiveCycle


def test_reproductive_cycle_progresses():
    cycle = ReproductiveCycle()
    assert cycle.step(7.0) == 0.25


def test_reproductive_cycle_validates_period():
    with pytest.raises(ValueError):
        ReproductiveCycle(period=0).step(1)
