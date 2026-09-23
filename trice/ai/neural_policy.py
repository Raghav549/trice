"""Small neural policy adapter with optional PyTorch implementation."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class NeuralPolicyConfig:
    input_size: int = 9
    hidden_size: int = 64
    output_size: int = 2
    learning_rate: float = 1e-3

    def validate(self) -> None:
        if min(self.input_size, self.hidden_size, self.output_size) < 1:
            raise ValueError("network sizes must be positive")
        if self.learning_rate <= 0:
            raise ValueError("learning_rate must be positive")


class TorchNeuralPolicy:
    """Lazy PyTorch MLP policy; core package does not require torch."""

    def __init__(self, config: NeuralPolicyConfig | None = None) -> None:
        cfg = config or NeuralPolicyConfig()
        cfg.validate()
        try:
            import torch
            import torch.nn as nn
        except ImportError as exc:
            raise RuntimeError("TorchNeuralPolicy requires optional torch") from exc
        self.torch = torch
        self.model = nn.Sequential(
            nn.Linear(cfg.input_size, cfg.hidden_size),
            nn.Tanh(),
            nn.Linear(cfg.hidden_size, cfg.output_size),
        )

    def predict(self, observation: list[float]) -> list[float]:
        tensor = self.torch.tensor(observation, dtype=self.torch.float32)
        with self.torch.no_grad():
            output = self.model(tensor)
        return [float(value) for value in output.tolist()]
