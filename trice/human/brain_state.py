"""High-level central brain state surface."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class BrainState:
    arousal: float = 0.5
    attention: float = 0.5
    working_memory: float = 0.5
    long_term_memory: float = 0.5
    threat_response: float = 0.0
    reward_signal: float = 0.0
    executive_control: float = 0.5

    def step(self, dt: float, sensory_salience: float = 0.0, reward: float = 0.0, threat: float = 0.0, sleep: float = 0.0) -> dict[str, float]:
        if dt <= 0:
            raise ValueError("dt must be positive")
        sensory_salience = max(0.0, min(1.0, float(sensory_salience)))
        threat = max(0.0, min(1.0, float(threat)))
        sleep = max(0.0, min(1.0, float(sleep)))
        self.arousal = max(0.0, min(1.0, 0.85 * self.arousal + 0.15 * max(sensory_salience, threat) - 0.1 * sleep * dt))
        self.attention = max(0.0, min(1.0, 0.7 * self.attention + 0.3 * sensory_salience))
        self.working_memory = max(0.0, min(1.0, 0.96 * self.working_memory + 0.04 * self.attention))
        self.long_term_memory = max(0.0, min(1.0, self.long_term_memory + 0.01 * self.working_memory * dt))
        self.threat_response = max(0.0, min(1.0, 0.8 * self.threat_response + 0.2 * threat))
        self.reward_signal = max(-1.0, min(1.0, 0.8 * self.reward_signal + 0.2 * float(reward)))
        self.executive_control = max(0.0, min(1.0, 0.6 * self.executive_control + 0.4 * (1.0 - self.threat_response)))
        return {
            "brain_arousal": self.arousal,
            "brain_attention": self.attention,
            "working_memory": self.working_memory,
            "long_term_memory": self.long_term_memory,
            "brain_threat_response": self.threat_response,
            "brain_reward_signal": self.reward_signal,
            "executive_control": self.executive_control,
        }
