"""Oral intake, mastication and swallowing abstraction."""
from dataclasses import dataclass

@dataclass
class OralState:
    food_present:float=0.0
    chewing:float=0.0
    saliva:float=.5
    bolus:float=0.0
    taste_input:float=0.0
    swallow_signal:float=0.0

class OralModel:
    def __init__(self): self.state=OralState()
    def step(self, food=0.0, chewing=0.0, taste=0.0, saliva=.5, swallow=False, dt=1.0):
        dt=max(0.0,float(dt)); s=self.state
        s.food_present=max(0.0,s.food_present+max(0.0,float(food))*dt)
        s.chewing=max(0.0,min(1.0,float(chewing)))
        s.saliva=max(0.0,min(1.0,float(saliva)))
        s.taste_input=max(-1.0,min(1.0,float(taste)))
        processed=min(s.food_present,s.chewing*.35*dt+s.saliva*.08*dt)
        s.food_present-=processed; s.bolus+=processed
        s.swallow_signal=1.0 if swallow and s.bolus>0 else 0.0
        if s.swallow_signal: s.bolus=max(0.0,s.bolus-0.8*s.bolus)
        return s.__dict__.copy()
