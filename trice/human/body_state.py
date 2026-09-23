"""Unified top-level human computational state."""
from __future__ import annotations

from dataclasses import dataclass, field

from .behavior import BehavioralState
from .external_state import ExternalState
from .homeostatic_state import HomeostaticState
from .internal_state import InternalState
from .lifecycle import LifecycleState
from .mind import MindState


@dataclass
class HumanState:
    lifecycle: LifecycleState = field(default_factory=LifecycleState)
    internal: InternalState = field(default_factory=InternalState)
    homeostasis: HomeostaticState = field(default_factory=HomeostaticState)
    external: ExternalState = field(default_factory=ExternalState)
    behavior: BehavioralState = field(default_factory=BehavioralState)
    mind: MindState = field(default_factory=MindState)

    def validate(self) -> None:
        if self.lifecycle.age_years < 0:
            raise ValueError("age cannot be negative")
        self.internal.clamp()
        self.homeostasis.clamp()
        self.behavior.clamp()
        self.mind.clamp()
