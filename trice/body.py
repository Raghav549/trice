"""Integrated computational body controller.

The controller composes independently testable organ-system models into one
state transition. All numeric relationships are simulation abstractions.
"""
from __future__ import annotations

from dataclasses import dataclass, field

from .brain.cognition import CognitiveState
from .brain.neuromodulation import Neuromodulators
from .endocrine.axis import EndocrineAxes
from .immune.engine import ImmuneEngine
from .molecular.genetics import GenomeState
from .physiology.cardiovascular import CardiovascularModel
from .physiology.cellular import CellularModel
from .physiology.digestion import DigestionModel
from .physiology.metabolism import MetabolismModel
from .physiology.motor import MotorModel
from .physiology.renal import RenalModel
from .physiology.respiratory import RespiratoryModel
from .physiology.sensory import SensoryModel


@dataclass
class ComputationalBody:
    """Integrated body-inspired state machine."""

    genome: GenomeState = field(default_factory=lambda: GenomeState(genes={"homeostasis": 0.7}))
    cells: CellularModel = field(default_factory=CellularModel)
    metabolism: MetabolismModel = field(default_factory=MetabolismModel)
    cardiovascular: CardiovascularModel = field(default_factory=CardiovascularModel)
    respiratory: RespiratoryModel = field(default_factory=RespiratoryModel)
    digestion: DigestionModel = field(default_factory=DigestionModel)
    renal: RenalModel = field(default_factory=RenalModel)
    motor: MotorModel = field(default_factory=MotorModel)
    sensory: SensoryModel = field(default_factory=SensoryModel)
    endocrine: EndocrineAxes = field(default_factory=EndocrineAxes)
    immune: ImmuneEngine = field(default_factory=ImmuneEngine)
    cognition: CognitiveState = field(default_factory=CognitiveState)
    neuromodulators: Neuromodulators = field(default_factory=Neuromodulators)

    def step(self, dt: float, inputs: dict[str, float] | None = None) -> dict[str, float]:
        inputs = inputs or {}
        sensory = self.sensory.ingest(inputs)
        activity = abs(float(inputs.get("movement", 0.0)))
        stress = float(inputs.get("stress", 0.0))
        food = float(inputs.get("food", 0.0))
        sleep = float(inputs.get("sleep", 0.0))

        cell = self.cells.step(dt, workload=0.2 + 0.4 * activity, damage_input=max(0.0, stress))
        metabolic = self.metabolism.step(dt, intake=food, activity=activity, stress=stress)
        cardio = self.cardiovascular.step(dt, activity=activity)
        resp = self.respiratory.step(dt, metabolic_demand=0.2 + 0.5 * activity)
        digestive = self.digestion.step(dt, food=food, stress=stress)
        renal = self.renal.step(dt, intake=food * 0.2, metabolic_load=stress)
        endocrine = self.endocrine.step(dt, stress=stress, glucose=metabolic["glucose"], circadian=inputs.get("circadian", 0.5))
        immune = self.immune.step(dt, stress=stress, damage=cell["dna_damage"] * 0.2)
        cognition = self.cognition.step(dt, sensory_salience=max(map(abs, sensory.values()), default=0.0), reward=inputs.get("reward", 0.0), threat=stress, sleep=sleep)
        neuro = self.neuromodulators.step(dt, reward=inputs.get("reward", 0.0), threat=stress, attention=cognition["attention"], pain=sensory["pain"] if sensory["pain"] > 0 else 0.0)
        motor = self.motor.step(dt, command=inputs.get("movement", 0.0), sensory_error=1.0 - sensory["vestibular"] if sensory["vestibular"] >= 0 else 1.0)
        genome = self.genome.step(signal=stress * -0.2 + metabolic["body_energy"] * 0.1)

        state: dict[str, float] = {}
        for group in (cell, metabolic, cardio, resp, digestive, renal, endocrine, immune, cognition, neuro, motor, genome):
            state.update(group)
        return state
