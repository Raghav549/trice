from trice.runtime.frameworks import FRAMEWORKS, detect_frameworks


def test_framework_detection_is_lazy():
    statuses = detect_frameworks()
    assert {item.name for item in statuses} == set(FRAMEWORKS)
    assert all(isinstance(item.available, bool) for item in statuses)
