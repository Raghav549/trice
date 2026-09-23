"""Backend selection contract."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Protocol, Sequence


class ArrayBackend(Protocol):
    name: str

    def as_array(self, values: Sequence[float]) -> Any:
        ...

    def to_list(self, value: Any) -> list[float]:
        ...


@dataclass
class NumpyBackend:
    name: str = "numpy"

    def __post_init__(self) -> None:
        import numpy as np
        self._np = np

    def as_array(self, values: Sequence[float]) -> Any:
        return self._np.asarray(values, dtype=self._np.float32)

    def to_list(self, value: Any) -> list[float]:
        return [float(v) for v in self._np.asarray(value).reshape(-1).tolist()]


class TorchBackend:
    name: str = "torch"

    def __init__(self, device: str = "cpu") -> None:
        try:
            import torch
        except ImportError as exc:
            raise RuntimeError("TorchBackend requires optional torch") from exc
        self._torch = torch
        self.device = torch.device(device)

    def as_array(self, values: Sequence[float]) -> Any:
        return self._torch.tensor(list(values), dtype=self._torch.float32, device=self.device)

    def to_list(self, value: Any) -> list[float]:
        return [float(v) for v in value.detach().cpu().reshape(-1).tolist()]
