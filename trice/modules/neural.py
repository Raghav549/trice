"""Adaptive neural subsystem with explicit neuron and synapse dynamics."""
from __future__ import annotations

from dataclasses import dataclass
from math import exp, isfinite

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
    refractory: float = 0.0

    def step(self, input_current: float, dt: float = 1.0) -> float:
        dt = float(dt)
        input_current = float(input_current)
        if not isfinite(dt) or dt < 0.0:
            raise ValueError("dt must be finite and >= 0")
        if not isfinite(input_current):
            raise ValueError("input_current must be finite")
        if self.refractory > 0.0:
            self.refractory = max(0.0, self.refractory - dt)
            return 0.0
        self.membrane += (input_current - self.leak * self.membrane) * dt
        spike = 1.0 if self.membrane >= self.threshold else 0.0
        if spike:
            self.membrane = 0.0
            self.refractory = 0.5
        return spike


@dataclass
class Synapse:
    pre: int
    post: int
    weight: float = 0.1
    learning_rate: float = 0.01

    def propagate(self, spike: float) -> float:
        spike = float(spike)
        return self.weight * max(0.0, min(1.0, spike))

    def update(self, pre_spike: float, post_spike: float) -> None:
        delta = self.learning_rate * (float(pre_spike) * float(post_spike) - 0.05 * abs(self.weight))
        self.weight = max(-1.0, min(1.0, self.weight + delta))


class NeuralModule(StatefulModule):
    name = "neural"

    def __init__(self, neuron_count: int = 8) -> None:
        super().__init__()
        if neuron_count < 1:
            raise ValueError("neuron_count must be >= 1")
        self.neurons = [Neuron() for _ in range(neuron_count)]
        self.synapses = [
            Synapse(index, (index + 1) % neuron_count) for index in range(neuron_count)
        ]
        self.activity = 0.0
        self.plasticity = 0.01

    def step(self, state: OrganismState, context: ModuleContext, dt: float = 1.0):
        dt = float(dt)
        if not isfinite(dt) or dt < 0.0:
            raise ValueError("dt must be finite and >= 0")
        sensory = float(context.signals.get("sensory", state.sensory))
        stress = float(context.signals.get("stress", state.stress))
        drive = sensory + 0.25 * state.arousal - 0.20 * stress
        spikes = [neuron.step(drive, dt) for neuron in self.neurons]

        recurrent = [0.0] * len(self.neurons)
        for synapse in self.synapses:
            recurrent[synapse.post] += synapse.propagate(spikes[synapse.pre])
        for index, current in enumerate(recurrent):
            if current:
                spikes[index] = self.neurons[index].step(current, dt)

        for synapse in self.synapses:
            synapse.update(spikes[synapse.pre], spikes[synapse.post])
        self.activity = sum(spikes) / len(spikes)
        self.plasticity = min(1.0, max(0.0, self.plasticity + 0.001 * (self.activity - 0.2)))
        return {"neural": self.activity, "arousal": sigmoid(drive)}
