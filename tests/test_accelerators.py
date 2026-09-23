from trice.runtime.accelerators import detect_accelerators


def test_accelerator_detection_has_cpu_reference():
    devices = detect_accelerators()
    assert any(device.name == "cpu" and device.available for device in devices)
