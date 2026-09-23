import pytest

from trice.ai.episode import Episode


def test_episode_accumulates_and_finishes():
    ep = Episode()
    ep.add(1.0)
    ep.add(-0.25)
    ep.finish(survival=1.0)
    assert ep.return_sum == 0.75
    with pytest.raises(RuntimeError):
        ep.add(1.0)


def test_episode_reset():
    ep = Episode()
    ep.add(1.0)
    ep.finish()
    ep.reset()
    assert ep.return_sum == 0.0
    assert not ep.done
