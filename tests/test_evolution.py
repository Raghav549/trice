from trice.evolution.reconfiguration import ReconfigurationManager
from trice.evolution.search import evolve


def test_evolution_improves_simple_objective() -> None:
    target = (1.0, -1.0)
    score = lambda genome: -sum((a - b) ** 2 for a, b in zip(genome, target))
    best = evolve(score, (0.0, 0.0), generations=8, population_size=12, seed_value=7)
    assert best.score > -3.0


def test_fault_isolation_and_repair() -> None:
    manager = ReconfigurationManager()
    manager.register("heart")
    manager.inject_fault("heart", 0.9)
    assert "heart" not in manager.healthy_modules()
    manager.repair("heart", 0.8)
    assert "heart" in manager.healthy_modules()
