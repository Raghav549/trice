from trice.human.lifecycle import LifecycleState


def test_lifecycle_stage_progression():
    state = LifecycleState(age_years=11.9, developmental_stage="childhood")
    state.step(0.2)
    assert state.developmental_stage == "adolescence"


def test_lifecycle_stops_after_death():
    state = LifecycleState(age_years=80, developmental_stage="older_adult", alive=False)
    state.step(1.0)
    assert state.age_years == 80
