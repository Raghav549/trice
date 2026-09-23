from trice.ai.learning import AdaptiveScalar

def test_adaptive_scalar_updates():
    m=AdaptiveScalar()
    before=m.value
    m.update(1)
    assert m.value>before
