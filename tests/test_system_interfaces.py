from trice.human.system_interfaces import SubsystemSpec


def test_subsystem_spec_is_explicit():
    spec = SubsystemSpec("cardiovascular", "organ", ("activity",), ("heart_rate",))
    assert spec.status == "ABSTRACTED"
    assert spec.outputs == ("heart_rate",)
