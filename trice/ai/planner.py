"""Small deterministic planner interface."""
from __future__ import annotations
from dataclasses import dataclass
from .goals import Goal

@dataclass
class Planner:
    def choose(self, observations:dict[str,float], goals:list[Goal])->Goal|None:
        if not goals: return None
        return max(goals,key=lambda g: abs(g.error(observations.get(g.name,0.0)))*g.weight)
