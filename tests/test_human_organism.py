from trice.human.organism import HumanOrganism


def test_human_organism_is_steppable():
    organism = HumanOrganism()
    state = organism.step(0.1, {"movement": 0.1})
    assert organism.time == 0.1
    assert state["time"] == 0.1
