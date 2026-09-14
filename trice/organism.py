"""Whole-organism coordinator for the TRICE simulation."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, Iterable, List

from .core.energy import EnergyBudget
from .core.homeostasis import HomeostasisEngine
from .core.module import BodyModule, ModuleContext
from .core.types import OrganismState


@dataclass
class TriceOrganism:
    """Coordinate coupled body-inspired modules over simulation time."""

    state: OrganismState = field(default_factory=OrganismState)
    energy: EnergyBudget = field(default_factory=EnergyBudget)
    homeostasis: HomeostasisEngine = field(default_factory=HomeostasisEngine)
    modules: List[BodyModule] = field(default_factory=list)

    def add_module(self, module: BodyModule) -> None:
        self.modules.append(module)

    def step(self, context: ModuleContext | None = None, dt: float = 1.0) -> OrganismState:
        context = context or ModuleContext()
        dt = max(0.0, float(dt))
        self.state.time += dt
        self.energy.step(dt)
        self.state.energy = self.energy.fraction

        updates: Dict[str, float] = {}
        for module in self.modules:
            module_updates = module.step(self.state, context, dt)
            updates.update({key: float(value) for key, value in module_updates.items()})
            self.state.modules[module.name] = float(module_updates.get(module.name, self.state.modules.get(module.name, 0.0)))

        for key, value in updates.items():
            if hasattr(self.state, key):
                setattr(self.state, key, value)
            else:
                self.state.modules[key] = value

        self.state = self.homeostasis.regulate(self.state, dt)
        self.state.energy = self.energy.fraction
        return self.state

    def snapshot(self) -> Dict[str, float]:
        return self.state.vector()
