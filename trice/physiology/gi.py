"""Gastrointestinal tract flow abstraction."""
from dataclasses import dataclass

@dataclass
class GIState:
    oral:float=0.0
    gastric:float=0.0
    small_intestinal:float=0.0
    absorbed:float=0.0
    colonic:float=0.0
    fecal_output:float=0.0

class GIModel:
    def __init__(self): self.state=GIState()
    def step(self, food:float=0.0, water:float=0.0, stress:float=0.0, dt:float=1.0):
        dt=max(0.0,float(dt)); food=max(0.0,float(food)); water=max(0.0,float(water))
        s=self.state
        s.oral += food*dt
        transit=min(s.oral, (0.25+0.25*(1.0-max(0.0,min(1.0,stress))))*dt)
        s.oral -= transit; s.gastric += transit
        gastric=min(s.gastric, 0.18*dt*(1.0-0.3*max(0.0,min(1.0,stress))))
        s.gastric -= gastric; s.small_intestinal += gastric
        absorbed=min(s.small_intestinal, 0.5*s.small_intestinal*dt)
        s.small_intestinal -= absorbed; s.absorbed += absorbed
        colonic=min(s.absorbed, 0.12*s.absorbed*dt)
        s.colonic += colonic; s.fecal_output=max(0.0,s.fecal_output+0.05*s.colonic*dt-0.02*water*dt)
        return self.state.__dict__.copy()
