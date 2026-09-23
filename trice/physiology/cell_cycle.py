"""Cellular energy, membrane and damage-repair state abstraction."""
from dataclasses import dataclass

@dataclass
class CellCycleState:
    atp:float=.7
    membrane_potential:float=.55
    dna_integrity:float=1.0
    oxidative_stress:float=.1
    apoptosis_signal:float=0.0
    repair_activity:float=.4

class CellCycleModel:
    def __init__(self): self.state=CellCycleState()
    def step(self, oxygen:float=.7, nutrients:float=.6, damage:float=0.0, dt:float=1.0):
        dt=max(0.0,float(dt)); o=max(0.0,min(1.0,float(oxygen))); n=max(0.0,min(1.0,float(nutrients))); d=max(0.0,min(1.0,float(damage))); s=self.state
        s.atp=max(0.0,min(1.0,s.atp+(.5*o+.4*n-s.atp)*.2*dt))
        s.oxidative_stress=max(0.0,min(1.0,s.oxidative_stress+.12*o+.08*d-.07*s.atp))
        s.dna_integrity=max(0.0,min(1.0,s.dna_integrity-.05*d*dt+.02*s.repair_activity*dt))
        s.repair_activity=max(0.0,min(1.0,.2+.6*(1-s.dna_integrity)))
        s.apoptosis_signal=max(0.0,min(1.0,(1-s.dna_integrity)*.8+s.oxidative_stress*.2))
        s.membrane_potential=max(0.0,min(1.0,.35+.55*s.atp))
        return s.__dict__.copy()
