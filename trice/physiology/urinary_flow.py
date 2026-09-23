"""Computational urine-formation and urinary-tract flow abstraction."""
from __future__ import annotations
from dataclasses import dataclass

@dataclass
class UrinaryState:
    filtered_load:float=0.0
    reabsorbed_water:float=0.0
    solute_load:float=0.0
    urine_volume:float=0.0
    bladder_volume:float=0.0
    voided_volume:float=0.0

class UrinaryFlowModel:
    def step(self, *, renal_filtration=0.0, hydration=0.5, waste_load=0.0,
             bladder_capacity=1.0, void=0.0, dt=1.0)->dict[str,float]:
        dt=max(0.0,float(dt))
        filtration=max(0.0,float(renal_filtration))
        hydration=max(0.0,min(1.0,float(hydration)))
        waste=max(0.0,min(1.0,float(waste_load)))
        self.state.filtered_load+=filtration*dt
        self.state.solute_load=max(0.0,self.state.solute_load+0.5*waste*dt-0.15*hydration*dt)
        self.state.reabsorbed_water=max(0.0,0.25*hydration)
        produced=max(0.0,self.state.filtered_load*0.05*(1.0-self.state.reabsorbed_water))
        self.state.urine_volume=max(0.0,self.state.urine_volume+produced*dt)
        capacity=max(0.01,float(bladder_capacity))
        self.state.bladder_volume=min(capacity,self.state.bladder_volume+self.state.urine_volume*0.1*dt)
        self.state.urine_volume*=0.9**dt
        if float(void)>0.5:
            self.state.voided_volume=self.state.bladder_volume
            self.state.bladder_volume=0.0
        else:
            self.state.voided_volume=0.0
        return self.state.__dict__.copy()

    def __init__(self)->None:
        self.state=UrinaryState()
