from trice.human.body_surface import BodySurface


def test_body_surface_tracks_external_barrier_state():
    surface = BodySurface()
    state = surface.step(1.0, injury=0.5, dryness=0.1)
    assert 0.0 <= state["barrier_function"] <= 1.0
    assert state["wound_load"] > 0.0
