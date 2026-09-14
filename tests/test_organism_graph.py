import math

import pytest

from trice.core.organism_graph import Coupling, OrganismGraph


def test_core_couplings_exist() -> None:
    graph = OrganismGraph()
    assert "neural" in graph.neighbors("sensory")
    assert "immune" in graph.neighbors("stress")
    assert any(c.channel == "oxygenation_feedback" for c in graph.incoming("cardiovascular"))
    assert graph.neighbors("neural")


def test_coupling_rejects_invalid_contract() -> None:
    with pytest.raises(ValueError, match="non-empty"):
        Coupling("", "neural", "afferent")
    with pytest.raises(ValueError, match="finite"):
        Coupling("sensory", "neural", "afferent", math.inf)


def test_graph_rejects_duplicate_channels() -> None:
    coupling = Coupling("sensory", "neural", "afferent")
    with pytest.raises(ValueError, match="duplicate"):
        OrganismGraph((coupling, coupling))
