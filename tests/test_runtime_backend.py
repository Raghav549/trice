import pytest

from trice.runtime.backend import NumpyBackend, TorchBackend


def test_numpy_backend_round_trip():
    backend = NumpyBackend()
    value = backend.as_array([1, 2, 3])
    assert backend.to_list(value) == [1.0, 2.0, 3.0]


def test_torch_backend_is_optional():
    try:
        backend = TorchBackend()
    except RuntimeError:
        pytest.skip("torch not installed")
    value = backend.as_array([1, 2])
    assert backend.to_list(value) == [1.0, 2.0]
