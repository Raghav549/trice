from trice.systems.whole_body import COMPONENTS, CoverageStatus, coverage_map


def test_registry_has_no_duplicate_component_names():
    names = [component.name for component in COMPONENTS]
    assert len(names) == len(set(names))


def test_every_component_has_explicit_status():
    assert COMPONENTS
    assert all(component.status in set(CoverageStatus) for component in COMPONENTS)


def test_core_whole_body_components_are_registered():
    registry = coverage_map()
    required = {
        "dna", "genes", "ribosomes", "mitochondria", "neurons", "synapses",
        "heart", "lungs", "liver", "kidneys", "stomach", "small_intestine",
        "red_blood_cells", "white_blood_cells", "skeletal_muscle", "skin",
        "immune_system", "endocrine_glands", "hippocampal_memory",
    }
    assert required.issubset(registry)
