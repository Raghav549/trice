"""Optional framework adapters with lazy imports."""
from __future__ import annotations

from typing import Any, Sequence


def numpy_array(values: Sequence[float]) -> Any:
    try:
        import numpy as np
    except ImportError as exc:
        raise RuntimeError("NumPy is required for numpy_array") from exc
    return np.asarray(values, dtype=np.float32)


def torch_tensor(values: Sequence[float], device: str = "cpu") -> Any:
    try:
        import torch
    except ImportError as exc:
        raise RuntimeError("PyTorch is required for torch_tensor") from exc
    return torch.tensor(list(values), dtype=torch.float32, device=device)


def jax_array(values: Sequence[float]) -> Any:
    try:
        import jax.numpy as jnp
    except ImportError as exc:
        raise RuntimeError("JAX is required for jax_array") from exc
    return jnp.asarray(values, dtype=jnp.float32)


def tensorflow_tensor(values: Sequence[float]) -> Any:
    try:
        import tensorflow as tf
    except ImportError as exc:
        raise RuntimeError("TensorFlow is required for tensorflow_tensor") from exc
    return tf.convert_to_tensor(list(values), dtype=tf.float32)
