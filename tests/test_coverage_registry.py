from trice.systems.registry import Status, summary, validate_unique_ids


def test_registry_ids_are_unique():
    validate_unique_ids()


def test_registry_accounts_for_every_status():
    result = summary()
    assert result["TOTAL"] > 0
    assert sum(result[status.value] for status in Status) == result["TOTAL"]
