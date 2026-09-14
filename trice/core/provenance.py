"""Research provenance metadata for reproducible experiments."""
from __future__ import annotations

from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from typing import Any


@dataclass(frozen=True)
class Provenance:
    model_version: str
    experiment_id: str
    created_at: str
    seed: int
    notes: str = ""

    @classmethod
    def create(cls, model_version: str, experiment_id: str, seed: int, notes: str = "") -> "Provenance":
        return cls(
            model_version=model_version,
            experiment_id=experiment_id,
            created_at=datetime.now(timezone.utc).isoformat(),
            seed=int(seed),
            notes=notes,
        )

    def as_dict(self) -> dict[str, Any]:
        return asdict(self)
