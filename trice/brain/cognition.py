"""Stateful cognitive control abstraction.

The model exposes computational correlates of attention, working memory,
valuation, threat processing and sleep/wake regulation. It does not claim to
implement or reproduce subjective consciousness.
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class CognitiveState:
    attention: float = 0.5
    working_memory: float = 0.2
    reward_value: float = 0.0
    threat_value: float = 0.0
    executive_control: float = 0.5
    arousal: float = 0.5
    sleep_pressure: float = 0.0
    consciousness_proxy: float = 0.5

    def step(self, dt: float, sensory_salience: float = 0.0, reward: float = 0.0, threat: float = 0.0, sleep: float = 0.0) -> dict[str, float]:
        dt = max(0.0, float(dt))
        salience = max(0.0, min(1.0, float(sensory_salience)))
        reward = max(-1.0, min(1.0, float(reward)))
        threat = max(0.0, min(1.0, float(threat)))
        sleep = max(0.0, min(1.0, float(sleep)))
        self.attention += (salience - self.attention) * min(1.0, dt * 1.2)
        self.working_memory += ((0.2 + 0.6 * self.attention) - self.working_memory) * min(1.0, dt * 0.8)
        self.reward_value += (reward - self.reward_value) * min(1.0, dt * 0.7)
        self.threat_value += (threat - self.threat_value) * min(1.0, dt * 1.0)
        self.executive_control += ((1.0 - self.threat_value) * (1.0 - self.sleep_pressure) - self.executive_control) * min(1.0, dt * 0.35)
        self.arousal += ((0.3 + 0.5 * self.attention + 0.25 * self.threat_value) - self.arousal) * min(1.0, dt * 0.5)
        self.sleep_pressure += (0.015 - self.sleep_pressure * 0.01) * dt
        if sleep > 0.5:
            self.sleep_pressure *= max(0.0, 1.0 - 0.15 * dt)
        self.consciousness_proxy = max(0.0, min(1.0, 0.5 * self.arousal + 0.3 * self.attention + 0.2 * self.executive_control))
        return {
            "attention": self.attention,
            "working_memory": self.working_memory,
            "reward_value": self.reward_value,
            "threat_value": self.threat_value,
            "executive_control": self.executive_control,
            "arousal": self.arousal,
            "sleep_pressure": self.sleep_pressure,
            "consciousness_proxy": self.consciousness_proxy,
        }
