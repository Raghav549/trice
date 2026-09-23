"""Explicit goal/task representation for agent experiments."""
from dataclasses import dataclass, field

@dataclass
class Goal:
    name:str
    target:float=.0
    weight:float=1.0
    metadata:dict[str,str]=field(default_factory=dict)

    def error(self, value:float)->float:
        return float(self.target)-float(value)
