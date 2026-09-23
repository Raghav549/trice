import pytest

from trice.runtime.data_adapter import records_to_rows, to_numpy


def test_records_to_rows():
    assert records_to_rows([{"a": 1}]) == [{"a": 1}]


def test_numpy_adapter_is_optional():
    try:
        value = to_numpy([{"a": 1, "b": 2}], ["a", "b"])
    except RuntimeError:
        pytest.skip("numpy not installed")
    assert value.shape == (1, 2)
