"""Minimal adaptive neural subsystem."""
from __future__ import annotations

from dataclasses import dataclass, field
from math import exp
from typing import List

from ..core.module import ModuleContext, StatefulModule
from ..core.types import OrganismState


def sigmoid(x: float) -> float:
    if x >= 0:
        z = exp(-x)
        return 1.0 / (1.0 + z)
    z = exp(x)
    return z / (1.0 + z)


@dataclass
class Neuron:
    threshold: float = 0.5
    membrane: float = 0.0
    leak: float = 0.1

    def step(self, input_current: float, dt: float = 1.0) -> float:
        self.membrane += (input_current - self.leak * self.membrane) * max(dt, 0.0)
        spike = 1.0 if self.membrane >= self.threshold else 0.0
        if spike:
            self.membrane = 0.0
        return spike


class NeuralModule(StatefulModule):
    name = "neural"

    def __init__(self, neuron_count: int = 8) -> None:
        super().__init__()
        if neuron_count < 1:
            raise ValueError("neuron_count must be >= 1")
        self.neurons: List[Neuron] = [Neuron() for _ in range(neuron_count)]
        self.activity = 0.0
        self.plasticity = 0.01

    def step(self, state: OrganismState, context: ModuleContext, dt: float = 1.0):
        sensory = float(context.signals.get("sensory", state.sensory))
        stress = float(context.signals.get("stress", state.stress))
        drive = sensory + 0.25 * state.arousal - 0.20 * stress
        spikes = [n.step(drive, dt) for n in self.neurons]
        self.activity = sum(spikes) / len(spikes)
        self.plasticity = min(1.0, max(0.0, self.plasticity + 0.001 * (self.activity - 0.2)))
        return {"neural": self.activity, "arousal": sigmoid(drive)}
