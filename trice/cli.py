"""Command-line entry point for running reproducible TRICE simulations."""
from __future__ import annotations

import argparse
import json

from .organism import TriceOrganism
from .core.simulation import Simulation


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="trice", description="Run the TRICE whole-organism simulator")
    parser.add_argument("--steps", type=int, default=100)
    parser.add_argument("--dt", type=float, default=0.1)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    organism = TriceOrganism()
    simulation = Simulation(organism.step)
    results = simulation.run(args.steps, args.dt)
    if not results:
        print(json.dumps(organism.snapshot(), indent=2, sort_keys=True))
        return 0
    final = results[-1]
    print(json.dumps({"state": final.state.vector(), "health": final.report.ok}, indent=2, sort_keys=True))
    return 0 if final.report.ok else 2


if __name__ == "__main__":
    raise SystemExit(main())
