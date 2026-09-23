import pytest

from trice.core.checks import require_keys, require_range


def test_require_keys():
    require_keys({"a": 1.0, "b": 2.0}, ("a", "b"))
    with pytest.raises(KeyError):
        require_keys({"a": 1.0}, ("a", "b"))


def test_require_range():
    require_range(0.5, 0.0, 1.0, "x")
    with pytest.raises(ValueError):
        require_range(2.0, 0.0, 1.0, "x")
