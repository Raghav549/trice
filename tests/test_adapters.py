import pytest

from trice.runtime.adapters import jax_array, numpy_array, tensorflow_tensor, torch_tensor


def test_numpy_adapter():
    try:
        value = numpy_array([1, 2])
    except RuntimeError:
        pytest.skip("numpy not installed")
    assert value.shape == (2,)


def test_torch_adapter():
    try:
        value = torch_tensor([1, 2])
    except RuntimeError:
        pytest.skip("torch not installed")
    assert tuple(value.shape) == (2,)


def test_jax_adapter():
    try:
        value = jax_array([1, 2])
    except RuntimeError:
        pytest.skip("jax not installed")
    assert tuple(value.shape) == (2,)


def test_tensorflow_adapter():
    try:
        value = tensorflow_tensor([1, 2])
    except RuntimeError:
        pytest.skip("tensorflow not installed")
    assert tuple(value.shape) == (2,)
