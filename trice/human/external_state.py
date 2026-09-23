"""Environment-facing human state."""
from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class ExternalState:
    position: tuple[float, float, float] = (0.0, 0.0, 0.0)
    ambient_temperature: float = 1.0
    light: float = 0.0
    sound: float = 0.0
    contact: float = 0.0
    odors: dict[str, float] = field(default_factory=dict)
    nutrients: dict[str, float] = field(default_factory=dict)

    def move(self, dx: float, dy: float, dz: float = 0.0) -> None:
        x, y, z = self.position
        self.position = (x + float(dx), y + float(dy), z + float(dz))
