"""Body-position and joint-sense state surface."""
from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Proprioception:
    joint_positions: dict[str, float] = field(default_factory=dict)
    confidence: float = 1.0

    def ingest(self, positions: dict[str, float] | None = None) -> dict[str, float]:
        source = positions or {}
        self.joint_positions = {
            str(name): max(-1.0, min(1.0, float(value)))
            for name, value in source.items()
        }
        self.confidence = 1.0 if self.joint_positions else 0.0
        return {
            "proprioception_confidence": self.confidence,
            "proprioception_joint_count": float(len(self.joint_positions)),
        }
