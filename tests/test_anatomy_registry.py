from trice.anatomy.registry import get, systems, validate_parents

def test_registry_links():
    validate_parents()
    assert get("liver").name == "Liver"
    assert "renal" in systems()
