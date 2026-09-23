"""Hormonal feedback network abstraction."""
from dataclasses import dataclass

@dataclass
class EndocrineState:
    thyroid_signal:float=.5
    insulin_signal:float=.5
    glucagon_signal:float=.4
    cortisol_signal:float=.2
    reproductive_signal:float=.4
    growth_signal:float=.4

class EndocrineNetwork:
    def __init__(self): self.state=EndocrineState()
    def step(self, glucose:float=.5, stress:float=.2, energy:float=.5, circadian:float=.5, dt:float=1.0):
        dt=max(0.0,float(dt)); g=max(0.0,min(1.0,float(glucose))); st=max(0.0,min(1.0,float(stress))); en=max(0.0,min(1.0,float(energy))); c=max(0.0,min(1.0,float(circadian))); s=self.state
        s.insulin_signal=max(0.0,min(1.0,.15+.75*g))
        s.glucagon_signal=max(0.0,min(1.0,.2+.65*(1-g)))
        s.cortisol_signal=max(0.0,min(1.0,.15+.7*st))
        s.thyroid_signal=max(0.0,min(1.0,.25+.5*en+.15*c-.15*st))
        s.reproductive_signal=max(0.0,min(1.0,.2+.5*en+.1*c))
        s.growth_signal=max(0.0,min(1.0,.2+.45*en+.15*(1-st)))
        return s.__dict__.copy()
