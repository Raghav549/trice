from trice.core.coupling import CouplingGraph


def test_coupling_graph_routes_signals():
    graph = CouplingGraph()
    graph.add("respiration", "oxygen", "cardiovascular", 0.5)
    graph.add("metabolism", "energy", "cognition", 1.0)
    assert len(graph.targets_for("respiration", "oxygen")) == 1
    graph.validate()


def test_coupling_graph_rejects_empty_endpoint():
    graph = CouplingGraph()
    try:
        graph.add("", "x", "y")
    except ValueError:
        pass
    else:
        raise AssertionError("expected ValueError")
