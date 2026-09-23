"""Structured brain-region state surface for whole-human modeling."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class BrainNetwork:
    cortex: float = 0.5
    thalamus: float = 0.5
    hypothalamus: float = 0.5
    hippocampus: float = 0.5
    basal_ganglia: float = 0.5
    cerebellum: float = 0.5
    brainstem: float = 0.5

    def step(
        self,
        dt: float,
        sensory_input: float = 0.0,
        reward: float = 0.0,
        threat: float = 0.0,
        motor_feedback: float = 0.0,
    ) -> dict[str, float]:
        if dt <= 0:
            raise ValueError("dt must be positive")
        sensory_input = max(0.0, min(1.0, float(sensory_input)))
        threat = max(0.0, min(1.0, float(threat)))
        reward = max(-1.0, min(1.0, float(reward)))
        motor_feedback = max(-1.0, min(1.0, float(motor_feedback)))

        self.thalamus = 0.85 * self.thalamus + 0.15 * sensory_input
        self.hypothalamus = 0.85 * self.hypothalamus + 0.15 * threat
        self.hippocampus = max(0.0, min(1.0, self.hippocampus + 0.01 * sensory_input * dt))
        self.basal_ganglia = max(0.0, min(1.0, 0.8 * self.basal_ganglia + 0.2 * ((reward + 1.0) / 2.0)))
        self.cerebellum = max(0.0, min(1.0, 0.9 * self.cerebellum + 0.1 * abs(motor_feedback)))
        self.brainstem = max(0.0, min(1.0, 0.9 * self.brainstem + 0.1 * max(sensory_input, threat)))
        self.cortex = max(
            0.0,
            min(1.0, 0.7 * self.cortex + 0.3 * ((self.thalamus + self.hippocampus + self.basal_ganglia) / 3.0)),
        )
        return {
            "cortex_state": self.cortex,
            "thalamus_state": self.thalamus,
            "hypothalamus_state": self.hypothalamus,
            "hippocampus_state": self.hippocampus,
            "basal_ganglia_state": self.basal_ganglia,
            "cerebellum_state": self.cerebellum,
            "brainstem_state": self.brainstem,
        }
