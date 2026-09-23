from trice.runtime.pipeline import compose


def test_pipeline_composes_stages():
    pipeline = compose(lambda x: x + 1, lambda x: x * 2)
    assert pipeline.run(3) == 8
