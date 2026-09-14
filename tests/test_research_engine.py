from trice.research.evolution import EvolutionConfig, EvolutionEngine, Genome
from trice.research.objectives import Objective, multi_objective_score


def test_evolution_improves_simple_objective_deterministically():
    config = EvolutionConfig(population_size=8, generations=6, seed=7)
    population = [Genome((float(i),)) for i in range(8)]
    engine = EvolutionEngine(config)
    best, score = engine.run(population, lambda genome: genome.genes[0])
    assert best.genes[0] >= 7.0
    assert score >= 7.0


def test_multi_objective_score_respects_direction():
    objectives = [Objective("accuracy", 2.0, True), Objective("latency", 1.0, False)]
    score = multi_objective_score((0.9, 0.2), objectives)
    assert score > 0.4
