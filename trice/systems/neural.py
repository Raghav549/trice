"""Temporal neural, memory and neuromodulatory abstractions."""
from __future__ import annotations
from dataclasses import dataclass, field
from math import exp


def _clip(value: float) -> float:
    return max(0.0, min(1.0, float(value)))


@dataclass
class Synapse:
    weight: float = 0.5
    trace: float = 0.0

    def update(self, pre: float, post: float, learning_rate: float = 0.03, decay: float = 0.05, dt: float = 1.0) -> None:
        hebbian = _clip(pre) * _clip(post)
        self.trace += (hebbian - self.trace) * (1.0 - exp(-dt / 5.0))
        self.weight = _clip(self.weight + learning_rate * (self.trace - decay * self.weight) * dt)


@dataclass
class NeuralCircuit:
    activation: float = 0.0
    synapses: list[Synapse] = field(default_factory=list)

    def step(self, input_signal: float, neuromodulation: float = 0.0, dt: float = 1.0) -> float:
        drive = _clip(0.65 * input_signal + 0.20 * neuromodulation + 0.15 * self.activation)
        self.activation += (drive - self.activation) * (1.0 - exp(-dt / 1.5))
        for synapse in self.synapses:
            synapse.update(self.activation, drive, dt=dt)
        return self.activation


@dataclass
class BrainCognitiveState:
    attention: float = 0.3
    working_memory: float = 0.2
    long_memory: float = 0.2
    reward: float = 0.0
    threat: float = 0.0
    executive_control: float = 0.4
    sleep_pressure: float = 0.2

    def step(self, sensory: float, novelty: float, reward: float, dt: float = 1.0) -> dict[str, float]:
        sensory = _clip(sensory)
        novelty = _clip(novelty)
        reward = _clip(reward)
        self.attention = _clip(0.55 * self.attention + 0.35 * sensory + 0.20 * novelty)
        self.working_memory = _clip(self.working_memory + 0.10 * self.attention * dt - 0.04 * self.sleep_pressure * dt)
        self.long_memory = _clip(self.long_memory + 0.035 * self.working_memory * (0.5 + reward) * dt - 0.008 * self.long_memory * dt)
        self.reward = _clip(0.80 * self.reward + 0.20 * reward)
        self.threat = _clip(0.75 * self.threat + 0.25 * novelty)
        self.executive_control = _clip(0.45 + 0.40 * self.attention - 0.35 * self.threat)
        self.sleep_pressure = _clip(self.sleep_pressure + 0.004 * dt - 0.06 * self.attention * dt)
        return self.__dict__.copy()


@dataclass
class NeuromodulatorState:
    dopamine: float = 0.3
    serotonin: float = 0.4
    endorphins: float = 0.2

    def step(self, reward: float, stress: float, pain: float, dt: float = 1.0) -> dict[str, float]:
        reward = _clip(reward)
        stress = _clip(stress)
        pain = _clip(pain)
        self.dopamine = _clip(0.82 * self.dopamine + 0.16 * reward - 0.06 * stress)
        self.serotonin = _clip(0.90 * self.serotonin + 0.06 * (1.0 - stress) - 0.03 * pain)
        self.endorphins = _clip(0.88 * self.endorphins + 0.10 * pain)
        return self.__dict__.copy()
