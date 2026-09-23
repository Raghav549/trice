"""Minimal learned-agent state contract."""
from dataclasses import dataclass, field

@dataclass
class AgentState:
    goal:str=""
    reward:float=0.0
    confidence:float=0.0
    observations:dict[str,float]=field(default_factory=dict)
    actions:dict[str,float]=field(default_factory=dict)
