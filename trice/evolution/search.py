"""Safe computational evolutionary search over model parameters."""
from __future__ import annotations

from dataclasses import dataclass
import random
from typing import Callable, Sequence


@dataclass(frozen=True)
class Candidate:
    genome: tuple[float, ...]
    score: float


def mutate(genome: Sequence[float], rng: random.Random, sigma: float = 0.05) -> tuple[float, ...]:
    sigma = max(0.0, float(sigma))
    return tuple(float(value) + rng.gauss(0.0, sigma) for value in genome)


def evolve(
    evaluate: Callable[[tuple[float, ...]], float],
    seed: Sequence[float],
    *,
    generations: int = 20,
    population_size: int = 16,
    mutation_sigma: float = 0.05,
    seed_value: int = 0,
) -> Candidate:
    if generations < 1 or population_size < 2:
        raise ValueError("generations >= 1 and population_size >= 2 are required")
    rng = random.Random(seed_value)
    population = [Candidate(tuple(seed), evaluate(tuple(seed)))]
    while len(population) < population_size:
        genome = mutate(seed, rng, mutation_sigma)
        population.append(Candidate(genome, evaluate(genome)))
    for _ in range(generations):
        population.sort(key=lambda item: item.score, reverse=True)
        elites = population[: max(2, population_size // 4)]
        next_population = list(elites)
        while len(next_population) < population_size:
            parent = rng.choice(elites)
            child = mutate(parent.genome, rng, mutation_sigma)
            next_population.append(Candidate(child, evaluate(child)))
        population = next_population
    return max(population, key=lambda item: item.score)
