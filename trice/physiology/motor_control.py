"""Upper/lower limb and fine-motor control abstraction."""
from dataclasses import dataclass

@dataclass
class MotorState:
    posture:float=.5
    gait:float=0.0
    upper_limb_control:float=.5
    hand_control:float=.5
    finger_control:float=.5
    lower_limb_force:float=.5
    toe_control:float=.5

class MotorControlModel:
    def __init__(self): self.state=MotorState()
    def step(self, movement=0.0, balance=0.5, precision=0.5, dt=1.0):
        dt=max(0.0,float(dt)); m=max(-1.0,min(1.0,float(movement))); b=max(0.0,min(1.0,float(balance))); p=max(0.0,min(1.0,float(precision))); s=self.state
        s.posture += ((.5+.4*b)-s.posture)*min(1.0,.4*dt)
        s.gait=max(0.0,min(1.0,abs(m)*b))
        s.upper_limb_control=max(0.0,min(1.0,.5+.3*abs(m)))
        s.hand_control=max(0.0,min(1.0,.4+.4*p))
        s.finger_control=max(0.0,min(1.0,.35+.5*p))
        s.lower_limb_force=max(0.0,min(1.0,.45+.35*abs(m)))
        s.toe_control=max(0.0,min(1.0,.4+.4*b))
        return s.__dict__.copy()
