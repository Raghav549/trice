"""Breathing control and gas-balance abstraction."""
from dataclasses import dataclass

@dataclass
class BreathingState:
    respiratory_drive:float=0.4
    ventilation:float=0.5
    oxygenation:float=0.7
    co2:float=0.2
    breath_cycle:float=0.0

class BreathingModel:
    def __init__(self): self.state=BreathingState()
    def step(self, oxygen_demand:float=.5, air_input:float=1.0, dt:float=1.0):
        dt=max(0.0,float(dt)); demand=max(0.0,min(1.0,float(oxygen_demand))); air=max(0.0,float(air_input))
        s=self.state
        target=.25+.65*demand+.08*s.co2
        s.respiratory_drive += (target-s.respiratory_drive)*min(1.0,.8*dt)
        s.ventilation=max(0.0,min(1.0,s.respiratory_drive*(0.35+0.25*min(1.0,air))))
        s.co2=max(0.0,min(1.0,s.co2+.12*demand*dt-.18*s.ventilation*dt))
        s.oxygenation=max(0.0,min(1.0,.25+.8*s.ventilation-.18*s.co2))
        s.breath_cycle=(s.breath_cycle+dt*max(.1,s.ventilation))%1.0
        return self.state.__dict__.copy()
