"""Airway-to-gas-exchange flow abstraction."""
from dataclasses import dataclass

@dataclass
class AirwayState:
    nasal_air:float=0.0
    airway_air:float=0.0
    alveolar_exchange:float=0.0
    oxygenation:float=0.5
    co2_removal:float=0.5

class RespiratoryFlowModel:
    def __init__(self): self.state=AirwayState()
    def step(self, air:float=0.0, metabolic_demand:float=0.5, dt:float=1.0):
        dt=max(0.0,float(dt)); air=max(0.0,float(air)); demand=max(0.0,min(1.0,float(metabolic_demand)))
        s=self.state
        s.nasal_air += air*dt
        moved=min(s.nasal_air,0.6*dt); s.nasal_air-=moved; s.airway_air+=moved
        exchanged=min(s.airway_air,0.5*dt); s.airway_air-=exchanged; s.alveolar_exchange+=exchanged
        s.oxygenation=max(0.0,min(1.0,0.2+0.8*s.alveolar_exchange/(1.0+s.alveolar_exchange)-0.15*demand))
        s.co2_removal=max(0.0,min(1.0,0.2+0.7*s.oxygenation))
        return self.state.__dict__.copy()
