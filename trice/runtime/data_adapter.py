"""Small tabular/dataframe compatibility layer."""
from __future__ import annotations

from collections.abc import Iterable, Mapping
from typing import Any


def records_to_rows(records: Iterable[Mapping[str, Any]]) -> list[dict[str, Any]]:
    return [dict(record) for record in records]


def to_numpy(rows: list[Mapping[str, Any]], columns: list[str]) -> Any:
    try:
        import numpy as np
    except ImportError as exc:
        raise RuntimeError("NumPy adapter requires optional numpy") from exc
    return np.asarray([[row.get(column, 0.0) for column in columns] for row in rows], dtype=float)


def to_pandas(rows: list[Mapping[str, Any]], columns: list[str]) -> Any:
    try:
        import pandas as pd
    except ImportError as exc:
        raise RuntimeError("Pandas adapter requires optional pandas") from exc
    return pd.DataFrame(rows, columns=columns)


def to_polars(rows: list[Mapping[str, Any]], columns: list[str]) -> Any:
    try:
        import polars as pl
    except ImportError as exc:
        raise RuntimeError("Polars adapter requires optional polars") from exc
    return pl.DataFrame(rows, schema=columns)
