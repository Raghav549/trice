import pytest

from trice.core.module import ModuleContext
from trice.core.types import OrganismState
from trice.modules.neural import NeuralModule, Neuron, Synapse


def test_neuron_refractory_cycle_is_deterministic() -> None:
    neuron = Neuron(threshold=0.5, leak=0.0)
    assert neuron.step(1.0, dt=1.0) == 1.0
    assert neuron.step(1.0, dt=0.1) == 0.0
    assert neuron.step(1.0, dt=0.5) == 1.0


def test_synapse_weight_remains_bounded_and_adaptive() -> None:
    synapse = Synapse(0, 1, weight=0.9, learning_rate=0.5)
    for _ in range(20):
        synapse.update(1.0, 1.0)
    assert -1.0 <= synapse.weight <= 1.0
    assert synapse.propagate(1.0) == synapse.weight


def test_neural_module_produces_finite_state() -> None:
    module = NeuralModule(neuron_count=4)
    state = OrganismState(arousal=0.5)
    result = module.step(state, ModuleContext(signals={"sensory": 1.0}), dt=0.1)
    assert set(result) == {"neural", "arousal"}
    assert all(value == value for value in result.values())


def test_neuron_rejects_invalid_dt() -> None:
    with pytest.raises(ValueError, match="dt"):
        Neuron().step(1.0, dt=-1.0)
