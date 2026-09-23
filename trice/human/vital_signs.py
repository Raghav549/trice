"""High-level vital-sign state with explicit validation."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class VitalSigns:
    heart_rate: float = 70.0
    respiratory_rate: float = 14.0
    systolic_pressure: float = 120.0
    diastolic_pressure: float = 80.0
    oxygen_saturation: float = 0.98
    core_temperature: float = 1.0

    def validate(self) -> None:
        if self.heart_rate < 0 or self.respiratory_rate < 0:
            raise ValueError("rates cannot be negative")
        if self.systolic_pressure < 0 or self.diastolic_pressure < 0:
            raise ValueError("pressure cannot be negative")
        if not 0.0 <= self.oxygen_saturation <= 1.0:
            raise ValueError("oxygen_saturation must be within [0, 1]")
        if self.core_temperature < 0:
            raise ValueError("core_temperature cannot be negative")
