"""Nutrient absorption and transport abstraction."""
from dataclasses import dataclass

@dataclass
class AbsorptionState:
    glucose:float=0.0
    amino_acids:float=0.0
    fatty_acids:float=0.0
    vitamins:float=0.0
    minerals:float=0.0
    water:float=0.0
    portal_load:float=0.0

class AbsorptionModel:
    def __init__(self): self.state=AbsorptionState()
    def step(self, digested:float=.0, protein:float=.0, fat:float=.0, vitamins:float=.0, minerals:float=.0, water:float=.0, dt:float=1.0):
        dt=max(0.0,float(dt))
        d=max(0.0,float(digested)); p=max(0.0,float(protein)); f=max(0.0,float(fat))
        v=max(0.0,float(vitamins)); m=max(0.0,float(minerals)); w=max(0.0,float(water))
        s=self.state
        s.glucose+=.55*d*dt
        s.amino_acids+=.5*p*dt
        s.fatty_acids+=.45*f*dt
        s.vitamins+=.75*v*dt
        s.minerals+=.7*m*dt
        s.water+=.9*w*dt
        s.portal_load=.2*s.glucose+.2*s.amino_acids+.15*s.fatty_acids+.1*s.vitamins+.1*s.minerals
        return self.state.__dict__.copy()
