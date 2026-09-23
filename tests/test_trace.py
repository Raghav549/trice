from trice.core.trace import StateTrace


def test_state_trace_records_and_returns_latest():
    trace = StateTrace()
    trace.record(0.1, {"energy": 0.8})
    trace.record(0.2, {"energy": 0.7, "stress": 0.1})
    assert trace.latest()["energy"] == 0.7
    assert len(trace.samples) == 2
    trace.clear()
    assert trace.latest() == {}
