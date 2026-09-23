"""Skin, hair, nails and barrier-state abstraction."""
from dataclasses import dataclass

@dataclass
class IntegumentState:
    barrier:float=1.0
    hydration:float=0.7
    sebum:float=0.5
    sweat:float=0.0
    hair_growth:float=0.5
    nail_growth:float=0.5
    wound_load:float=0.0

class IntegumentModel:
    def __init__(self): self.state=IntegumentState()
    def step(self, temperature:float=0.5, stress:float=0.0, hydration:float=0.7, dt:float=1.0):
        dt=max(0.0,float(dt)); temperature=max(0.0,min(1.0,float(temperature))); stress=max(0.0,min(1.0,float(stress))); hydration=max(0.0,min(1.0,float(hydration)))
        s=self.state
        s.hydration += (hydration-s.hydration)*min(1.0,0.5*dt)
        s.sebum += ((0.35+0.35*stress)-s.sebum)*min(1.0,0.2*dt)
        s.sweat=max(0.0,min(1.0,s.sweat+(temperature-0.55)*0.5*dt))
        s.hair_growth=max(0.0,min(1.0,s.hair_growth+(s.hydration-0.5)*0.03*dt))
        s.nail_growth=max(0.0,min(1.0,s.nail_growth+(s.hydration-0.5)*0.02*dt))
        s.barrier=max(0.0,min(1.0,0.85*s.hydration+0.15*(1.0-s.wound_load)))
        return self.state.__dict__.copy()
