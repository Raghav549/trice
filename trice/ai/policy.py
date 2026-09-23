"""Deterministic baseline policy interface.
A learned model can replace this policy without changing the body simulator.
"""
from __future__ import annotations

class Policy:
    def act(self, observations:dict[str,float])->dict[str,float]:
        energy=observations.get("energy",.5)
        stress=observations.get("stress",.0)
        return {"movement":max(-1.0,min(1.0,energy-.5)), "attention":max(0.0,min(1.0,1.0-stress))}
