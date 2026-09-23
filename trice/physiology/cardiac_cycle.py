"""Cardiac cycle and perfusion abstraction."""
from dataclasses import dataclass

@dataclass
class CardiacState:
    sinoatrial_drive:float=.5
    heart_rate:float=.5
    stroke_output:float=.5
    cardiac_output:float=.5
    perfusion:float=.5

class CardiacCycle:
    def __init__(self): self.state=CardiacState()
    def step(self, demand:float=.5, sympathetic:float=.0, dt:float=1.0):
        dt=max(0.0,float(dt)); demand=max(0.0,min(1.0,float(demand))); sympathetic=max(0.0,min(1.0,float(sympathetic)))
        s=self.state
        target=.35+.4*demand+.2*sympathetic
        s.sinoatrial_drive += (target-s.sinoatrial_drive)*min(1.0,.7*dt)
        s.heart_rate=max(0.0,min(1.0,s.sinoatrial_drive))
        s.stroke_output=max(0.0,min(1.0,.55+.25*demand-.18*sympathetic))
        s.cardiac_output=max(0.0,min(1.0,s.heart_rate*s.stroke_output))
        s.perfusion=max(0.0,min(1.0,.35+.75*s.cardiac_output))
        return self.state.__dict__.copy()
