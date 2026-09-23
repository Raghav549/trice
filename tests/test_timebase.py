import pytest

from trice.core.timebase import Timebase


def test_timebase_advances_deterministically():
    tb = Timebase()
    assert tb.advance(0.1) == 0.1
    assert tb.advance(0.2) == 0.30000000000000004
    assert tb.steps == 2


def test_timebase_rejects_nonpositive_dt():
    with pytest.raises(ValueError):
        Timebase().advance(0.0)
