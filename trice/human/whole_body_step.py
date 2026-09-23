"""Whole-human step coordinator across major state surfaces."""
from __future__ import annotations

from dataclasses import dataclass, field

from .body_surface import BodySurface
from .circulation_state import CirculationState
from .endocrine_state import EndocrineState
from .fluid_balance import FluidBalance
from .hematology_state import HematologyState
from .immune_state import ImmuneState
from .musculoskeletal_state import MusculoskeletalState
from .nervous_state import NervousState
from .renal_state import RenalState
from .respiration_state import RespirationState
from .sensory_organs import SensoryOrgans
from .sleep_state import SleepState
from .thermoregulation_state import ThermoregulationState


@dataclass
class WholeBodyState:
    """Coupled high-level state; component models remain abstractions."""

    surface: BodySurface = field(default_factory=BodySurface)
    circulation: CirculationState = field(default_factory=CirculationState)
    endocrine: EndocrineState = field(default_factory=EndocrineState)
    fluids: FluidBalance = field(default_factory=FluidBalance)
    blood: HematologyState = field(default_factory=HematologyState)
    immune: ImmuneState = field(default_factory=ImmuneState)
    movement: MusculoskeletalState = field(default_factory=MusculoskeletalState)
    nervous: NervousState = field(default_factory=NervousState)
    renal: RenalState = field(default_factory=RenalState)
    respiration: RespirationState = field(default_factory=RespirationState)
    senses: SensoryOrgans = field(default_factory=SensoryOrgans)
    sleep: SleepState = field(default_factory=SleepState)
    temperature: ThermoregulationState = field(default_factory=ThermoregulationState)

    def step(self, dt: float, inputs: dict[str, float] | None = None) -> dict[str, float]:
        values = dict(inputs or {})
        sensed = self.senses.ingest(values)
        activity = max(0.0, min(1.0, abs(float(values.get("movement", 0.0)))))
        stress = max(0.0, min(1.0, float(values.get("stress", 0.0))))
        sleep_input = float(values.get("sleep", 0.0))

        nervous = self.nervous.step(dt, sensory_load=max(abs(v) for v in sensed.values()), threat=stress)
        respiration = self.respiration.step(dt, demand=activity)
        circulation = self.circulation.step(dt, activity=activity)
        blood_capacity = self.blood.oxygen_capacity()
        immune = self.immune.step(dt, pathogen_input=values.get("pathogen", 0.0), damage_input=stress * 0.1)
        endocrine = self.endocrine
        endocrine.cortisol = max(0.0, min(1.0, 0.8 * endocrine.cortisol + 0.2 * stress))
        endocrine.adrenaline = max(0.0, min(1.0, 0.8 * endocrine.adrenaline + 0.2 * stress * activity))
        endocrine.clamp()
        fluids = self.fluids.step(dt, water_intake=max(0.0, values.get("water", 0.0)), loss=activity * 0.03)
        renal = self.renal.step(dt, hydration=fluids["water"], solute_load=max(0.0, values.get("solute", 0.0)))
        movement = self.movement.step(dt, command=values.get("movement", 0.0), load=activity)
        sleep = self.sleep.step(dt, sleep_input=sleep_input)
        temperature = self.temperature.step(dt, ambient_temperature=values.get("ambient_temperature", 1.0), activity=activity)
        surface = self.surface.step(dt, injury=values.get("injury", 0.0), dryness=1.0 - fluids["water"])

        return {
            **sensed,
            **nervous,
            **respiration,
            **circulation,
            "blood_oxygen_capacity": blood_capacity,
            **immune,
            "endocrine_cortisol": endocrine.cortisol,
            "endocrine_adrenaline": endocrine.adrenaline,
            **fluids,
            **renal,
            **movement,
            **sleep,
            **temperature,
            **surface,
        }
