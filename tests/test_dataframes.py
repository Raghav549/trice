import pytest

from trice.runtime.dataframes import pandas_frame, polars_frame


def test_pandas_frame_optional():
    try:
        frame = pandas_frame([{"x": 1}])
    except RuntimeError:
        pytest.skip("pandas not installed")
    assert list(frame.columns) == ["x"]


def test_polars_frame_optional():
    try:
        frame = polars_frame([{"x": 1}])
    except RuntimeError:
        pytest.skip("polars not installed")
    assert frame.height == 1
