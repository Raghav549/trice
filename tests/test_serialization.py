from trice.runtime.serialization import dumps_state, loads_state


def test_state_serialization_is_stable():
    payload = dumps_state({"b": 2, "a": 1})
    assert payload == '{"a":1.0,"b":2.0}'
    assert loads_state(payload) == {"a": 1.0, "b": 2.0}
