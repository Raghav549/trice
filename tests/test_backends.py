import pytest

from trice.core.backends import CPUBackend, TorchBackend, get_backend


def test_cpu_backend_maps_values():
    backend = CPUBackend()
    assert backend.map(lambda x: x * 2, [1, 2, 3]) == [2.0, 4.0, 6.0]


def test_unknown_backend_rejected():
    with pytest.raises(ValueError):
        get_backend("unknown")


def test_torch_backend_is_optional():
    try:
        backend = TorchBackend()
    except RuntimeError:
        pytest.skip("torch is not installed")
    assert backend.map(lambda x: x + 1, [1, 2]) == [2.0, 3.0]
