"""Hepatic metabolism and detoxification abstraction."""
from dataclasses import dataclass

@dataclass
class LiverState:
    glycogen:float=0.5
    protein_synthesis:float=0.6
    lipid_processing:float=0.5
    bile_support:float=0.6
    toxin_load:float=0.1

class LiverModel:
    def __init__(self): self.state=LiverState()
    def step(self, glucose:float=0.5, amino_acids:float=0.5, fats:float=0.5, toxin_input:float=0.0, dt:float=1.0):
        dt=max(0.0,float(dt)); glucose=max(0.0,min(1.0,float(glucose))); amino_acids=max(0.0,min(1.0,float(amino_acids))); fats=max(0.0,min(1.0,float(fats))); toxin_input=max(0.0,min(1.0,float(toxin_input)))
        s=self.state
        s.glycogen=max(0.0,min(1.0,s.glycogen+0.12*(glucose-s.glycogen)*dt))
        s.protein_synthesis=max(0.0,min(1.0,0.3+0.7*amino_acids))
        s.lipid_processing=max(0.0,min(1.0,0.25+0.65*fats))
        s.bile_support=max(0.0,min(1.0,0.4+0.5*fats))
        s.toxin_load=max(0.0,min(1.0,s.toxin_load+0.2*toxin_input*dt-0.08*s.toxin_load*dt))
        return self.state.__dict__.copy()
