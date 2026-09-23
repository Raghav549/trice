from trice.human.organ_registry import ORGANS, SystemDomain, organs_for


def test_organ_registry_covers_major_domains():
    domains = {organ.domain for organ in ORGANS}
    assert set(SystemDomain).issubset(domains)
    assert organs_for(SystemDomain.NERVOUS)
