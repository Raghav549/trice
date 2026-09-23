"""Low-overhead state tracing for reproducible experiments."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Mapping


@dataclass
class StateTrace:
    """Store compact time-stamped state snapshots."""

    samples: list[tuple[float, dict[str, float]]] = field(default_factory=list)

    def record(self, time: float, state: Mapping[str, float]) -> None:
        self.samples.append((float(time), {str(k): float(v) for k, v in state.items()}))

    def latest(self) -> dict[str, float]:
        if not self.samples:
            return {}
        return dict(self.samples[-1][1])

    def clear(self) -> None:
        self.samples.clear()
