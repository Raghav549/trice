"""Macronutrient and micronutrient bookkeeping abstraction."""
from dataclasses import dataclass

@dataclass
class NutritionState:
    carbohydrate:float=0.0
    protein:float=0.0
    fat:float=0.0
    omega3:float=0.0
    omega6:float=0.0
    vitamins:float=0.0
    minerals:float=0.0
    fiber:float=0.0

class NutritionModel:
    def __init__(self): self.state=NutritionState()
    def step(self, *, carbohydrate=0.0, protein=0.0, fat=0.0, omega3=0.0, omega6=0.0, vitamins=0.0, minerals=0.0, fiber=0.0, dt=1.0):
        dt=max(0.0,float(dt)); s=self.state
        for k,v in {"carbohydrate":carbohydrate,"protein":protein,"fat":fat,"omega3":omega3,"omega6":omega6,"vitamins":vitamins,"minerals":minerals,"fiber":fiber}.items():
            setattr(s,k,max(0.0,getattr(s,k)+max(0.0,float(v))*dt))
        return s.__dict__.copy()
