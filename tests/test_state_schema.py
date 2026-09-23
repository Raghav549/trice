import pytest

from trice.core.state_schema import StateField, StateSchema


def test_state_schema_validates_bounds():
    schema = StateSchema((StateField("energy", 0.0, 1.0),))
    schema.validate({"energy": 0.8})
    with pytest.raises(ValueError):
        schema.validate({"energy": 2.0})
    assert schema.names == ("energy",)
