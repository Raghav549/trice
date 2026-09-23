"""Composable pipeline stages for training/evaluation."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable, Iterable


@dataclass
class Pipeline:
    stages: list[Callable[[Any], Any]]

    def run(self, value: Any) -> Any:
        current = value
        for stage in self.stages:
            current = stage(current)
        return current

    def append(self, stage: Callable[[Any], Any]) -> None:
        self.stages.append(stage)


def compose(*stages: Callable[[Any], Any]) -> Pipeline:
    return Pipeline(list(stages))
