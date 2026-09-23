"""RBC/WBC/platelet population dynamics abstraction."""
from dataclasses import dataclass

@dataclass
class HematologyState:
    rbc:float=1.0
    wbc:float=0.5
    platelets:float=0.8
    oxygen_carrying:float=0.7
    immune_readiness:float=0.5

class HematologyModel:
    def __init__(self): self.state=HematologyState()
    def step(self, oxygen_demand:float=0.5, immune_signal:float=0.0, blood_loss:float=0.0, dt:float=1.0):
        dt=max(0.0,float(dt)); oxygen_demand=max(0.0,min(1.0,float(oxygen_demand))); immune_signal=max(0.0,min(1.0,float(immune_signal))); blood_loss=max(0.0,min(1.0,float(blood_loss)))
        s=self.state
        s.rbc=max(0.0,s.rbc-0.002*blood_loss*dt+0.0005*(1-s.rbc)*dt)
        s.platelets=max(0.0,s.platelets-0.003*blood_loss*dt+0.001*(1-s.platelets)*dt)
        s.wbc=max(0.0,min(1.0,s.wbc+(immune_signal-s.wbc)*0.05*dt))
        s.oxygen_carrying=max(0.0,min(1.0,s.rbc*(1.0-0.15*oxygen_demand)))
        s.immune_readiness=max(0.0,min(1.0,0.6*s.wbc+0.4*s.platelets))
        return self.state.__dict__.copy()
