"""Versioned checkpoints for reproducible simulation resumes."""
from __future__ import annotations

import json
from dataclasses import asdict
from pathlib import Path
from typing import Any

from .types import OrganismState


SCHEMA_VERSION = 1


def save_checkpoint(path: str | Path, state: OrganismState, metadata: dict[str, Any] | None = None) -> None:
    payload = {
        "schema_version": SCHEMA_VERSION,
        "state": asdict(state),
        "metadata": metadata or {},
    }
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")


def load_checkpoint(path: str | Path) -> tuple[OrganismState, dict[str, Any]]:
    payload = json.loads(Path(path).read_text(encoding="utf-8"))
    if payload.get("schema_version") != SCHEMA_VERSION:
        raise ValueError(f"unsupported checkpoint schema: {payload.get('schema_version')!r}")
    return OrganismState.from_mapping(payload["state"]), dict(payload.get("metadata", {}))
