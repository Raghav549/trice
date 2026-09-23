"""Core material pools used to couple intake, digestion, blood and renal models."""
from __future__ import annotations
from dataclasses import dataclass

@dataclass
class MaterialPools:
    carbohydrates:float=0.0
    proteins:float=0.0
    fats:float=0.0
    omega3:float=0.0
    omega6:float=0.0
    vitamins:float=0.0
    minerals:float=0.0
    water:float=0.0
    oxygen:float=0.21
    carbon_dioxide:float=0.0
    nitrogenous_waste:float=0.0

    def ingest(self, *, carbohydrates=0.0, proteins=0.0, fats=0.0,
               omega3=0.0, omega6=0.0, vitamins=0.0, minerals=0.0,
               water=0.0, oxygen=0.0, dt=1.0)->dict[str,float]:
        dt=max(0.0,float(dt))
        for name,value in locals().items():
            if name in {"dt","self"}: continue
            if hasattr(self,name):
                setattr(self,name,max(0.0,getattr(self,name)+max(0.0,float(value))*dt))
        return self.snapshot()

    def snapshot(self)->dict[str,float]:
        return {k:float(v) for k,v in self.__dict__.items()}
