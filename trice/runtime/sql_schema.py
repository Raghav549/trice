"""SQL schema for persistent experiment metadata.

This module only emits standard SQL DDL; a database driver remains optional.
"""
from __future__ import annotations

SCHEMA_SQL = """
CREATE TABLE IF NOT EXISTS experiments (
    experiment_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    seed INTEGER NOT NULL,
    created_at TEXT NOT NULL,
    config_json TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS metrics (
    experiment_id INTEGER NOT NULL,
    step INTEGER NOT NULL,
    name TEXT NOT NULL,
    value REAL NOT NULL,
    FOREIGN KEY (experiment_id) REFERENCES experiments(experiment_id)
);

CREATE INDEX IF NOT EXISTS idx_metrics_experiment_step
ON metrics(experiment_id, step);
"""


def schema_sql() -> str:
    return SCHEMA_SQL.strip()
