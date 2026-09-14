"""Executable molecular genetics abstractions for TRICE.

The module models information flow (DNA -> RNA -> protein) computationally.
It does not prescribe wet-lab procedures or claim biochemical equivalence.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from math import isfinite


CODON_TABLE: dict[str, str] = {
    "UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L",
    "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
    "UAU": "Y", "UAC": "Y", "UAA": "*", "UAG": "*",
    "UGU": "C", "UGC": "C", "UGA": "*", "UGG": "W",
    "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
    "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
    "CAU": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
    "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",
    "AUU": "I", "AUC": "I", "AUA": "I", "AUG": "M",
    "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
    "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K",
    "AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R",
    "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
    "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
    "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E",
    "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G",
}


def _clean_dna(sequence: str) -> str:
    sequence = sequence.upper().replace(" ", "").replace("\n", "")
    if not sequence:
        raise ValueError("DNA sequence must be non-empty")
    if any(base not in "ACGT" for base in sequence):
        raise ValueError("DNA sequence must contain only A, C, G, T")
    return sequence


def transcribe_dna(sequence: str) -> str:
    """Transcribe a DNA coding strand into an RNA sequence."""
    return _clean_dna(sequence).replace("T", "U")


def translate_rna(sequence: str) -> str:
    """Translate RNA codons to a one-letter amino-acid sequence."""
    rna = sequence.upper().replace(" ", "").replace("\n", "")
    if any(base not in "ACGU" for base in rna):
        raise ValueError("RNA sequence must contain only A, C, G, U")
    amino_acids: list[str] = []
    for index in range(0, len(rna) - 2, 3):
        amino_acid = CODON_TABLE[rna[index : index + 3]]
        if amino_acid == "*":
            break
        amino_acids.append(amino_acid)
    return "".join(amino_acids)


@dataclass
class GenomeState:
    genes: dict[str, float] = field(default_factory=dict)
    regulatory_activity: dict[str, float] = field(default_factory=dict)
    dna_integrity: float = 1.0
    rna_activity: dict[str, float] = field(default_factory=dict)
    protein_activity: dict[str, float] = field(default_factory=dict)
    dna_sequences: dict[str, str] = field(default_factory=dict)
    mrna_sequences: dict[str, str] = field(default_factory=dict)
    protein_sequences: dict[str, str] = field(default_factory=dict)

    def regulate(self, signal: float) -> None:
        signal = float(signal)
        if not isfinite(signal):
            raise ValueError("signal must be finite")
        signal = max(-1.0, min(1.0, signal))
        for name, expression in list(self.genes.items()):
            regulator = self.regulatory_activity.get(name, 0.0)
            updated = expression + 0.1 * signal * (1.0 - abs(regulator))
            self.genes[name] = max(0.0, min(1.0, updated))

    def transcribe(self) -> None:
        self.rna_activity = {name: value for name, value in self.genes.items() if value > 0.0}
        self.mrna_sequences = {
            name: transcribe_dna(sequence)
            for name, sequence in self.dna_sequences.items()
            if self.genes.get(name, 0.0) > 0.0
        }

    def translate(self) -> None:
        self.protein_activity = {name: 0.8 * value for name, value in self.rna_activity.items()}
        self.protein_sequences = {
            name: translate_rna(sequence) for name, sequence in self.mrna_sequences.items()
        }

    def damage(self, amount: float) -> None:
        amount = float(amount)
        if not isfinite(amount):
            raise ValueError("damage amount must be finite")
        self.dna_integrity = max(0.0, min(1.0, self.dna_integrity - max(0.0, amount)))

    def repair(self, amount: float) -> None:
        amount = float(amount)
        if not isfinite(amount):
            raise ValueError("repair amount must be finite")
        self.dna_integrity = max(0.0, min(1.0, self.dna_integrity + max(0.0, amount)))

    def step(self, signal: float = 0.0) -> dict[str, float]:
        self.regulate(signal)
        self.transcribe()
        self.translate()
        return {
            "dna_integrity": self.dna_integrity,
            "active_genes": float(len(self.genes)),
            "active_rna": float(len(self.rna_activity)),
            "active_proteins": float(len(self.protein_activity)),
            "transcribed_sequences": float(len(self.mrna_sequences)),
        }
