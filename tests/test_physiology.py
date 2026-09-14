from trice.systems.cellular import CellState, MolecularState
from trice.systems.immune import ImmuneSystem
from trice.systems.neural import BrainCognitiveState, NeuromodulatorState, NeuralCircuit
from trice.systems.physiology import (
    CardiovascularModel,
    DigestiveMetabolicModel,
    NeuroEndocrineModel,
    RenalModel,
    RespiratoryModel,
)


def test_organ_models_return_bounded_states():
    cardio = CardiovascularModel().step(0.8, 0.4)
    resp = RespiratoryModel().step(0.8)
    renal = RenalModel().step(0.6, 0.8)
    digestive = DigestiveMetabolicModel().step(0.7, 0.5)
    endocrine = NeuroEndocrineModel().step(0.6, 0.7)
    for result in (cardio, resp, renal, digestive, endocrine):
        assert all(0.0 <= value <= 1.0 for value in result.values())


def test_cellular_states_are_bounded():
    molecular = MolecularState()
    cellular = CellState()
    for _ in range(20):
        molecular.step(0.6, 0.8)
        cellular.step(0.5, 0.3)
    assert all(0.0 <= v <= 1.0 for v in molecular.__dict__.values())
    assert all(0.0 <= v <= 1.0 for v in cellular.__dict__.values())


def test_neural_and_immune_layers_adapt():
    circuit = NeuralCircuit()
    cognitive = BrainCognitiveState()
    neuromod = NeuromodulatorState()
    immune = ImmuneSystem()
    for _ in range(10):
        signal = circuit.step(0.7, neuromod.dopamine)
        cognitive.step(signal, 0.5, 0.7)
        neuromod.step(0.7, cognitive.threat, 0.2)
        immune.step(cognitive.threat, 0.2)
    assert 0.0 <= signal <= 1.0
    assert 0.0 <= immune.surveillance <= 1.0
    assert 0.0 <= cognitive.long_memory <= 1.0
