"""Core-body temperature and heat-loss regulation abstraction."""
from dataclasses import dataclass

@dataclass
class ThermalState:
    core_temperature:float=.5
    heat_generation:float=.5
    heat_loss:float=.3
    shivering:float=0.0
    sweating:float=0.0

class ThermoregulationModel:
    def __init__(self): self.state=ThermalState()
    def step(self, ambient:float=.5, activity:float=.3, hydration:float=.7, dt:float=1.0):
        dt=max(0.0,float(dt)); a=max(0.0,min(1.0,float(ambient))); act=max(0.0,min(1.0,float(activity))); hyd=max(0.0,min(1.0,float(hydration))); s=self.state
        s.heat_generation=max(0.0,min(1.0,.35+.55*act))
        s.shivering=max(0.0,min(1.0,(.45-a)*1.8))
        s.sweating=max(0.0,min(1.0,max(0.0,a-.6)*1.5*hyd))
        s.heat_loss=max(0.0,min(1.0,.25+.45*(1-a)+.25*s.sweating))
        s.core_temperature=max(0.0,min(1.0,s.core_temperature+(.5-s.core_temperature)*.08*dt+(s.heat_generation-s.heat_loss)*.04*dt))
        return s.__dict__.copy()
