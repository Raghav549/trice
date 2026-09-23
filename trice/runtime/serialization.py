"""JSON-friendly serialization for simulation checkpoints and states."""
from __future__ import annotations

import json
from collections.abc import Mapping
from typing import Any


def dumps_state(state: Mapping[str, float]) -> str:
    return json.dumps({str(k): float(v) for k, v in state.items()}, sort_keys=True, separators=(",", ":"))


def loads_state(payload: str) -> dict[str, float]:
    value: Any = json.loads(payload)
    if not isinstance(value, dict):
        raise ValueError("state payload must encode an object")
    return {str(k): float(v) for k, v in value.items()}
