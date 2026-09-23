from trice.core.body_cycle import FullBodyCycle
from trice.core.organism_step import step_checked


def test_checked_step_returns_finite_state():
    state = step_checked(FullBodyCycle(), 0.1, {"movement": 0.2, "food": 0.1})
    assert state
