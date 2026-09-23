"""Zero-dependency SQLite persistence for experiments and metrics."""
from __future__ import annotations

import sqlite3
from pathlib import Path
from typing import Iterable


SCHEMA = """
CREATE TABLE IF NOT EXISTS experiments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    seed INTEGER NOT NULL,
    config_json TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS metrics (
    experiment_id INTEGER NOT NULL,
    step INTEGER NOT NULL,
    name TEXT NOT NULL,
    value REAL NOT NULL,
    FOREIGN KEY(experiment_id) REFERENCES experiments(id)
);
"""


class SQLiteStore:
    def __init__(self, path: str | Path = ":memory:") -> None:
        self.connection = sqlite3.connect(str(path))
        self.connection.executescript(SCHEMA)

    def add_experiment(self, name: str, seed: int, config_json: str) -> int:
        cursor = self.connection.execute(
            "INSERT INTO experiments(name, seed, config_json) VALUES (?, ?, ?)",
            (name, int(seed), config_json),
        )
        self.connection.commit()
        return int(cursor.lastrowid)

    def add_metrics(self, experiment_id: int, step: int, metrics: dict[str, float]) -> None:
        rows = [
            (int(experiment_id), int(step), str(name), float(value))
            for name, value in metrics.items()
        ]
        self.connection.executemany(
            "INSERT INTO metrics(experiment_id, step, name, value) VALUES (?, ?, ?, ?)",
            rows,
        )
        self.connection.commit()

    def close(self) -> None:
        self.connection.close()
