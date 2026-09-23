from trice.core.determinism import canonical_inputs, states_equal


def test_canonical_inputs_sort_keys():
    assert list(canonical_inputs({"b": 2, "a": 1})) == ["a", "b"]


def test_states_equal_with_tolerance():
    assert states_equal({"x": 1.0}, {"x": 1.0 + 1e-13})
