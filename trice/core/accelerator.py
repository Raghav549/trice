"""Execution backend contract for CPU reference and future accelerators."""
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Callable, Sequence

class ExecutionBackend(ABC):
    name="abstract"
    @abstractmethod
    def map(self, fn:Callable[[float],float], values:Sequence[float])->list[float]:
        raise NotImplementedError

class CPUBackend(ExecutionBackend):
    name="cpu"
    def map(self, fn, values): return [fn(float(v)) for v in values]

def validate_equivalence(reference:list[float], accelerated:list[float], tolerance:float=1e-9)->None:
    if len(reference)!=len(accelerated): raise AssertionError("backend result length mismatch")
    for a,b in zip(reference,accelerated):
        if abs(float(a)-float(b))>float(tolerance): raise AssertionError("backend numerical mismatch")
