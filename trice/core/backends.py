"""Optional execution backends for TRICE numerical kernels."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable, Sequence


@dataclass
class CPUBackend:
    name: str = "cpu"

    def map(self, fn: Callable[[float], float], values: Sequence[float]) -> list[float]:
        return [float(fn(v)) for v in values]


class TorchBackend:
    """Lazy PyTorch backend; import remains optional at package runtime."""

    name = "torch"

    def __init__(self, device: str = "cpu") -> None:
        try:
            import torch
        except ImportError as exc:
            raise RuntimeError("TorchBackend requires the optional 'torch' package") from exc
        self._torch = torch
        self.device = torch.device(device)

    def tensor(self, values: Sequence[float]) -> Any:
        return self._torch.tensor(list(values), dtype=self._torch.float32, device=self.device)

    def map(self, fn: Callable[[Any], Any], values: Sequence[float]) -> list[float]:
        result = fn(self.tensor(values))
        return [float(v) for v in result.detach().cpu().flatten().tolist()]


def get_backend(name: str = "cpu") -> CPUBackend | TorchBackend:
    normalized = name.strip().lower()
    if normalized == "cpu":
        return CPUBackend()
    if normalized == "torch":
        return TorchBackend()
    raise ValueError(f"unknown backend: {name}")
