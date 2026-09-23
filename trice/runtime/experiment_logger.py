"""Optional experiment tracking facade for W&B and MLflow."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class ExperimentLogger:
    project: str = "trice"
    enabled: bool = False
    backend: str = "none"
    _run: Any = field(default=None, init=False, repr=False)

    def start(self, config: dict[str, Any] | None = None) -> None:
        if not self.enabled:
            return
        if self.backend == "wandb":
            try:
                import wandb
            except ImportError as exc:
                raise RuntimeError("W&B backend requires optional wandb") from exc
            self._run = wandb.init(project=self.project, config=config or {})
        elif self.backend == "mlflow":
            try:
                import mlflow
            except ImportError as exc:
                raise RuntimeError("MLflow backend requires optional mlflow") from exc
            mlflow.set_experiment(self.project)
            self._run = mlflow.start_run()
            if config:
                mlflow.log_params(config)
        elif self.backend != "none":
            raise ValueError(f"unknown tracking backend: {self.backend}")

    def log(self, metrics: dict[str, float], step: int | None = None) -> None:
        if not self.enabled:
            return
        if self.backend == "wandb":
            self._run.log(metrics, step=step)
        elif self.backend == "mlflow":
            import mlflow
            for name, value in metrics.items():
                mlflow.log_metric(name, float(value), step=step)

    def close(self) -> None:
        if not self.enabled:
            return
        if self.backend == "wandb" and self._run is not None:
            self._run.finish()
        elif self.backend == "mlflow":
            import mlflow
            mlflow.end_run()
        self._run = None
