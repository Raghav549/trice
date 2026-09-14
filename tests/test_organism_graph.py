from trice.core.organism_graph import OrganismGraph


def test_core_couplings_exist() -> None:
    graph = OrganismGraph()
    assert "neural" in graph.neighbors("sensory")
    assert "immune" in graph.neighbors("stress")
    assert any(c.channel == "oxygenation_feedback" for c in graph.incoming("cardiovascular"))
    assert graph.neighbors("neural")
