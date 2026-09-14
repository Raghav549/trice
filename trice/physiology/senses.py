"""Dedicated visual, auditory, olfactory, gustatory and vestibular abstractions."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class VisualSystem:
    acuity: float = 1.0
    luminance: float = 0.5
    contrast: float = 0.5

    def encode(self, luminance: float, contrast: float) -> dict[str, float]:
        self.luminance = max(0.0, min(1.0, float(luminance)))
        self.contrast = max(0.0, min(1.0, float(contrast)))
        return {"visual_luminance": self.luminance, "visual_contrast": self.contrast, "visual_signal": self.acuity * self.contrast}


@dataclass
class AuditorySystem:
    sensitivity: float = 1.0
    loudness: float = 0.0
    pitch: float = 0.5

    def encode(self, loudness: float, pitch: float) -> dict[str, float]:
        self.loudness = max(0.0, min(1.0, float(loudness)))
        self.pitch = max(0.0, min(1.0, float(pitch)))
        return {"auditory_loudness": self.loudness, "auditory_pitch": self.pitch, "auditory_signal": self.sensitivity * self.loudness}


@dataclass
class ChemosensorySystem:
    smell: float = 0.0
    taste: float = 0.0

    def encode(self, smell: float, taste: float) -> dict[str, float]:
        self.smell = max(0.0, min(1.0, float(smell)))
        self.taste = max(0.0, min(1.0, float(taste)))
        return {"olfactory_signal": self.smell, "gustatory_signal": self.taste}


@dataclass
class VestibularSystem:
    balance: float = 1.0
    acceleration: float = 0.0

    def encode(self, acceleration: float) -> dict[str, float]:
        self.acceleration = max(-1.0, min(1.0, float(acceleration)))
        self.balance = max(0.0, 1.0 - abs(self.acceleration))
        return {"vestibular_acceleration": self.acceleration, "vestibular_balance": self.balance}
