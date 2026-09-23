"""Optional accelerator adapters.

These are intentionally capability-based: a backend advertises what it can do
without forcing CUDA, XLA, TensorFlow or distributed packages into core TRICE.
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class AcceleratorInfo:
    name: str
    device: str = "cpu"
    available: bool = True
    capabilities: tuple[str, ...] = ()


def detect_accelerators() -> tuple[AcceleratorInfo, ...]:
    result = [AcceleratorInfo("cpu", "cpu", True, ("scalar", "reference"))]
    try:
        import torch
    except ImportError:
        torch = None
    if torch is not None:
        cuda_available = bool(torch.cuda.is_available())
        result.append(
            AcceleratorInfo(
                "pytorch",
                "cuda" if cuda_available else "cpu",
                True,
                ("tensor", "autograd", "cuda") if cuda_available else ("tensor", "autograd"),
            )
        )
    return tuple(result)
