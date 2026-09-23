"""Environment contract for perception/action experiments."""
from __future__ import annotations
from dataclasses import dataclass, field

@dataclass
class Environment:
    state:dict[str,float]=field(default_factory=dict)

    def observe(self)->dict[str,float]:
        return dict(self.state)

    def apply(self, action:dict[str,float])->dict[str,float]:
        self.state.update({k:float(v) for k,v in action.items()})
        return self.observe()
