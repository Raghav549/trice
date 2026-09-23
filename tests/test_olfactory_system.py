from trice.human.olfactory_system import OlfactorySystem


def test_olfactory_system_aggregates_molecular_input():
    result = OlfactorySystem().ingest({"coffee": 0.8, "smoke": 0.2})
    assert result["olfactory_salience"] == 0.5
