"""Computational auditory-perception state surface."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class AuditorySystem:
    hearing_gain: float = 1.0
    loudness: float = 0.0
    pitch: float = 0.5
    spatial_signal: float = 0.0
    auditory_salience: float = 0.0

    def ingest(self, loudness: float = 0.0, pitch: float = 0.5, spatial: float = 0.0) -> dict[str, float]:
        self.loudness = max(0.0, min(1.0, float(loudness)))
        self.pitch = max(0.0, min(1.0, float(pitch)))
        self.spatial_signal = max(0.0, min(1.0, abs(float(spatial))))
        self.auditory_salience = max(0.0, min(1.0, 0.6 * self.loudness + 0.4 * self.spatial_signal))
        return {
            "hearing_gain": self.hearing_gain,
            "auditory_loudness": self.loudness,
            "auditory_pitch": self.pitch,
            "auditory_spatial": self.spatial_signal,
            "auditory_salience": self.auditory_salience,
        }
