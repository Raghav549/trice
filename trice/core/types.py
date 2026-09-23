"""Core whole-organism state contracts."""
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Dict, Mapping

@dataclass
class OrganismState:
    time:float=0.0
    energy:float=1.0
    temperature:float=1.0
    neural:float=0.0
    immune:float=0.0
    endocrine:float=0.0
    memory:float=0.0
    cardiovascular:float=0.0
    respiratory:float=0.0
    digestion:float=0.0
    renal:float=0.0
    motor:float=0.0
    sensory:float=0.0
    stress:float=0.0
    arousal:float=0.0
    modules:Dict[str,float]=field(default_factory=dict)

    def vector(self)->Dict[str,float]:
        base={k:v for k,v in self.__dict__.items() if k!="modules"}
        base.update(self.modules)
        return {k:float(v) for k,v in base.items()}

    @classmethod
    def from_mapping(cls,values:Mapping[str,float])->"OrganismState":
        names=set(cls.__dataclass_fields__) - {"modules"}
        known={k:float(v) for k,v in values.items() if k in names}
        known["modules"]={k:float(v) for k,v in values.items() if k not in names}
        return cls(**known)
