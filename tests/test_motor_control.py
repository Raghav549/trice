from trice.physiology.motor_control import MotorControlModel
def test_limb_control():
    s=MotorControlModel().step(movement=.8,balance=.9,precision=.95)
    assert s["finger_control"]>s["hand_control"]-0.1
