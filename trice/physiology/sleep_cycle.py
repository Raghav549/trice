"""Circadian and sleep/wake-state abstraction."""
from dataclasses import dataclass

@dataclass
class SleepState:
    circadian_phase:float=0.0
    sleep_pressure:float=0.2
    sleep_depth:float=0.0
    wakefulness:float=.8

class SleepCycle:
    def __init__(self): self.state=SleepState()
    def step(self, dt:float=1.0, sleeping:bool=False, light:float=.5):
        dt=max(0.0,float(dt)); light=max(0.0,min(1.0,float(light))); s=self.state
        s.circadian_phase=(s.circadian_phase+dt/24.0)%1.0
        if sleeping:
            s.sleep_pressure=max(0.0,s.sleep_pressure-.08*dt); s.sleep_depth=min(1.0,s.sleep_depth+.12*dt)
        else:
            s.sleep_pressure=min(1.0,s.sleep_pressure+.018*dt); s.sleep_depth=max(0.0,s.sleep_depth-.15*dt)
        s.wakefulness=max(0.0,min(1.0,.65*light+.35*(1-s.sleep_depth)))
        return s.__dict__.copy()
