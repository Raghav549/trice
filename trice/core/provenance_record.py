"""Typed provenance metadata for computational/scientific claims."""
from dataclasses import dataclass

@dataclass(frozen=True)
class ProvenanceRecord:
    component_id:str
    source:str
    claim_type:str="computational_abstraction"
    confidence:float=.0
    notes:str=""

    def validate(self)->None:
        if not self.component_id or not self.source: raise ValueError("component_id and source are required")
        if not 0<=self.confidence<=1: raise ValueError("confidence must be in [0,1]")
