"""Abstract genome/transcription/translation state machine for TRICE.

This module is purely computational and does not prescribe wet-lab procedures.
"""
from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class GenomeState:
    genes: dict[str, float] = field(default_factory=dict)
    regulatory_activity: dict[str, float] = field(default_factory=dict)
    dna_integrity: float = 1.0
    rna_activity: dict[str, float] = field(default_factory=dict)
    protein_activity: dict[str, float] = field(default_factory=dict)

    def regulate(self, signal: float) -> None:
        signal = max(-1.0, min(1.0, float(signal)))
        for name, expression in list(self.genes.items()):
            regulator = self.regulatory_activity.get(name, 0.0)
            updated = expression + 0.1 * signal * (1.0 - abs(regulator))
            self.genes[name] = max(0.0, min(1.0, updated))

    def transcribe(self) -> None:
        self.rna_activity = {name: value for name, value in self.genes.items() if value > 0.0}

    def translate(self) -> None:
        self.protein_activity = {name: 0.8 * value for name, value in self.rna_activity.items()}

    def damage(self, amount: float) -> None:
        self.dna_integrity = max(0.0, min(1.0, self.dna_integrity - max(0.0, float(amount))))

    def repair(self, amount: float) -> None:
        self.dna_integrity = max(0.0, min(1.0, self.dna_integrity + max(0.0, float(amount))))

    def step(self, signal: float = 0.0) -> dict[str, float]:
        self.regulate(signal)
        self.transcribe()
        self.translate()
        return {
            "dna_integrity": self.dna_integrity,
            "active_genes": float(len(self.genes)),
            "active_rna": float(len(self.rna_activity)),
            "active_proteins": float(len(self.protein_activity)),
        }
