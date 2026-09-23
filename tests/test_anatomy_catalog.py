from trice.anatomy.catalog import CoverageStatus, summary, validate_unique_ids


def test_anatomy_catalog_is_explicit_and_unique():
    validate_unique_ids()
    result = summary()
    assert result["TOTAL"] >= 70
    assert result[CoverageStatus.ABSTRACTED.value] > 0
