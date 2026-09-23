"""Computational visual-perception state surface."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class VisionSystem:
    acuity: float = 1.0
    luminance: float = 0.0
    contrast: float = 0.5
    motion_signal: float = 0.0
    visual_salience: float = 0.0

    def ingest(self, luminance: float = 0.0, contrast: float = 0.5, motion: float = 0.0) -> dict[str, float]:
        self.luminance = max(0.0, min(1.0, float(luminance)))
        self.contrast = max(0.0, min(1.0, float(contrast)))
        self.motion_signal = max(0.0, min(1.0, abs(float(motion))))
        self.visual_salience = max(0.0, min(1.0, 0.5 * self.contrast + 0.5 * self.motion_signal))
        return {
            "visual_acuity": self.acuity,
            "visual_luminance": self.luminance,
            "visual_contrast": self.contrast,
            "visual_motion": self.motion_signal,
            "visual_salience": self.visual_salience,
        }
