"""Innate/adaptive immune surveillance abstraction."""
from dataclasses import dataclass

@dataclass
class ImmuneState:
    innate_activity:float=.5
    adaptive_activity:float=.4
    inflammation:float=.1
    memory:float=.2
    pathogen_load:float=0.0
    tissue_damage:float=0.0

class ImmuneNetwork:
    def __init__(self): self.state=ImmuneState()
    def step(self, antigen:float=0.0, damage:float=0.0, stress:float=0.0, dt:float=1.0):
        dt=max(0.0,float(dt)); ag=max(0.0,min(1.0,float(antigen))); da=max(0.0,min(1.0,float(damage))); st=max(0.0,min(1.0,float(stress))); s=self.state
        s.pathogen_load=max(0.0,min(1.0,s.pathogen_load+ag*.12*dt-s.innate_activity*.08*dt-s.adaptive_activity*.06*dt))
        s.innate_activity=max(0.0,min(1.0,s.innate_activity+(.35+ag*.7+s.pathogen_load*.3-s.innate_activity)*.2*dt))
        s.adaptive_activity=max(0.0,min(1.0,s.adaptive_activity+(.25+ag*.6+s.memory*.2-s.adaptive_activity)*.08*dt))
        s.inflammation=max(0.0,min(1.0,.1+.65*s.pathogen_load+.25*da+.1*st))
        s.memory=max(0.0,min(1.0,s.memory+.03*s.adaptive_activity*dt))
        s.tissue_damage=max(0.0,min(1.0,s.tissue_damage+.05*da*dt-.02*s.adaptive_activity*dt))
        return s.__dict__.copy()
