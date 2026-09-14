"""Safe, reproducible evolutionary search over computational configurations."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Iterable

from ..core.randomness import DeterministicRNG


@dataclass(frozen=True)
class Genome:
    """Immutable numeric genome used for computational architecture search."""

    genes: tuple[float, ...]

    def mutate(self, rng: DeterministicRNG, rate: float = 0.1, scale: float = 0.05) -> "Genome":
        if not 0.0 <= rate <= 1.0:
            raise ValueError("rate must be within [0, 1]")
        values = list(self.genes)
        for i, value in enumerate(values):
            if rng.random() < rate:
                values[i] = value + rng.uniform(-scale, scale)
        return Genome(tuple(values))

    @staticmethod
    def crossover(a: "Genome", b: "Genome", rng: DeterministicRNG) -> "Genome":
        if len(a.genes) != len(b.genes):
            raise ValueError("genomes must have equal length")
        values = tuple(a.genes[i] if rng.random() < 0.5 else b.genes[i] for i in range(len(a.genes)))
        return Genome(values)


@dataclass(frozen=True)
class EvolutionConfig:
    population_size: int = 32
    generations: int = 25
    mutation_rate: float = 0.1
    mutation_scale: float = 0.05
    seed: int = 0

    def validate(self) -> None:
        if self.population_size < 2:
            raise ValueError("population_size must be >= 2")
        if self.generations < 1:
            raise ValueError("generations must be >= 1")
        if not 0.0 <= self.mutation_rate <= 1.0:
            raise ValueError("mutation_rate must be within [0, 1]")
        if self.mutation_scale < 0:
            raise ValueError("mutation_scale must be non-negative")


class EvolutionEngine:
    """Minimal deterministic evolutionary optimizer."""

    def __init__(self, config: EvolutionConfig):
        config.validate()
        self.config = config
        self.rng = DeterministicRNG(config.seed)

    def run(self, initial: Iterable[Genome], fitness: Callable[[Genome], float]) -> tuple[Genome, float]:
        population = list(initial)
        if len(population) < 2:
            raise ValueError("initial population must contain at least two genomes")
        best = max(population, key=fitness)
        best_score = float(fitness(best))
        for _ in range(self.config.generations):
            ranked = sorted(((float(fitness(g)), g) for g in population), key=lambda item: item[0], reverse=True)
            if ranked[0][0] > best_score:
                best_score, best = ranked[0]
            survivors = [g for _, g in ranked[: max(2, len(ranked) // 2)]]
            next_population = survivors[:]
            while len(next_population) < self.config.population_size:
                a = self.rng.choice(survivors)
                b = self.rng.choice(survivors)
                child = Genome.crossover(a, b, self.rng).mutate(
                    self.rng, self.config.mutation_rate, self.config.mutation_scale
                )
                next_population.append(child)
            population = next_population
        return best, best_score
