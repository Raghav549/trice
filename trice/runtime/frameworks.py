"""Optional framework detection and adapter contracts.

Heavy ML/distributed frameworks are detected lazily so the core package remains
importable on a minimal Python installation.
"""
from __future__ import annotations

import importlib.util
from dataclasses import dataclass


@dataclass(frozen=True)
class FrameworkStatus:
    name: str
    available: bool


FRAMEWORKS = (
    "torch",
    "jax",
    "tensorflow",
    "pandas",
    "numpy",
    "polars",
    "ray",
    "dask",
    "pyspark",
    "wandb",
    "mlflow",
)


def detect_frameworks() -> tuple[FrameworkStatus, ...]:
    return tuple(
        FrameworkStatus(name, importlib.util.find_spec(name) is not None)
        for name in FRAMEWORKS
    )
