"""Optional Pandas/Polars dataframe adapters."""
from __future__ import annotations

from typing import Any


def pandas_frame(rows: list[dict[str, Any]]) -> Any:
    try:
        import pandas as pd
    except ImportError as exc:
        raise RuntimeError("Pandas is required for pandas_frame") from exc
    return pd.DataFrame(rows)


def polars_frame(rows: list[dict[str, Any]]) -> Any:
    try:
        import polars as pl
    except ImportError as exc:
        raise RuntimeError("Polars is required for polars_frame") from exc
    return pl.DataFrame(rows)
