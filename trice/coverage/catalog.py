"""Whole-body coverage catalog.

Every biological item has an explicit modeling status so coverage cannot be
silently forgotten while the research architecture grows.
"""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Iterable, List


class CoverageStatus(str, Enum):
    IMPLEMENTED = "IMPLEMENTED"
    ABSTRACTED = "ABSTRACTED"
    PLANNED = "PLANNED"
    UNMODELED = "UNMODELED"


@dataclass(frozen=True)
class BiologicalComponent:
    id: str
    name: str
    layer: str
    status: CoverageStatus
    notes: str = ""


MINIMUM_CATALOG: List[BiologicalComponent] = [
    BiologicalComponent("atom", "Atoms and ions", "physical", CoverageStatus.ABSTRACTED),
    BiologicalComponent("molecule", "Small molecules", "physical", CoverageStatus.ABSTRACTED),
    BiologicalComponent("amino_acid", "Amino acids", "molecular", CoverageStatus.ABSTRACTED),
    BiologicalComponent("lipid", "Lipids and membranes", "molecular", CoverageStatus.ABSTRACTED),
    BiologicalComponent("protein", "Proteins and enzymes", "molecular", CoverageStatus.ABSTRACTED),
    BiologicalComponent("dna", "DNA and genome", "genetic", CoverageStatus.PLANNED),
    BiologicalComponent("rna", "RNA and transcription", "genetic", CoverageStatus.PLANNED),
    BiologicalComponent("gene", "Genes and regulation", "genetic", CoverageStatus.PLANNED),
    BiologicalComponent("epigenetics", "Epigenetic state", "genetic", CoverageStatus.PLANNED),
    BiologicalComponent("nucleus", "Nucleus", "cellular", CoverageStatus.PLANNED),
    BiologicalComponent("mitochondria", "Mitochondria", "cellular", CoverageStatus.PLANNED),
    BiologicalComponent("ribosome", "Ribosomes", "cellular", CoverageStatus.PLANNED),
    BiologicalComponent("er", "Endoplasmic reticulum", "cellular", CoverageStatus.PLANNED),
    BiologicalComponent("golgi", "Golgi apparatus", "cellular", CoverageStatus.PLANNED),
    BiologicalComponent("lysosome", "Lysosomes", "cellular", CoverageStatus.PLANNED),
    BiologicalComponent("peroxisome", "Peroxisomes", "cellular", CoverageStatus.PLANNED),
    BiologicalComponent("cytoskeleton", "Cytoskeleton", "cellular", CoverageStatus.PLANNED),
    BiologicalComponent("membrane", "Cell membrane and transport", "cellular", CoverageStatus.PLANNED),
    BiologicalComponent("rbc", "Red blood cells", "blood", CoverageStatus.PLANNED),
    BiologicalComponent("wbc", "White blood cells", "blood", CoverageStatus.PLANNED),
    BiologicalComponent("platelet", "Platelets", "blood", CoverageStatus.PLANNED),
    BiologicalComponent("plasma", "Plasma", "blood", CoverageStatus.PLANNED),
    BiologicalComponent("hemoglobin", "Hemoglobin and gas carriage", "blood", CoverageStatus.PLANNED),
    BiologicalComponent("immune", "Innate/adaptive immunity", "immune", CoverageStatus.IMPLEMENTED),
    BiologicalComponent("neuron", "Neurons", "neural", CoverageStatus.IMPLEMENTED),
    BiologicalComponent("synapse", "Synapses", "neural", CoverageStatus.PLANNED),
    BiologicalComponent("glia", "Glial cells", "neural", CoverageStatus.PLANNED),
    BiologicalComponent("neurotransmitter", "Neurotransmitters and neuromodulators", "neural", CoverageStatus.PLANNED),
    BiologicalComponent("action_potential", "Electrical impulses", "neural", CoverageStatus.IMPLEMENTED),
    BiologicalComponent("hippocampus", "Hippocampal-style memory", "brain", CoverageStatus.ABSTRACTED),
    BiologicalComponent("prefrontal", "Prefrontal executive control", "brain", CoverageStatus.ABSTRACTED),
    BiologicalComponent("amygdala", "Amygdala-style threat/value processing", "brain", CoverageStatus.ABSTRACTED),
    BiologicalComponent("consciousness", "Conscious-state variable", "brain", CoverageStatus.ABSTRACTED),
    BiologicalComponent("emotion", "Emotion and affect", "brain", CoverageStatus.ABSTRACTED),
    BiologicalComponent("memory", "Adaptive memory", "cognition", CoverageStatus.IMPLEMENTED),
    BiologicalComponent("endocrine", "Hormonal/endocrine regulation", "endocrine", CoverageStatus.IMPLEMENTED),
    BiologicalComponent("heart", "Heart and cardiac cycle", "cardiovascular", CoverageStatus.PLANNED),
    BiologicalComponent("vasculature", "Vessels and circulation", "cardiovascular", CoverageStatus.PLANNED),
    BiologicalComponent("lung", "Lungs and airways", "respiratory", CoverageStatus.PLANNED),
    BiologicalComponent("gas_exchange", "Gas exchange", "respiratory", CoverageStatus.PLANNED),
    BiologicalComponent("mouth", "Mouth and oral processing", "digestive", CoverageStatus.PLANNED),
    BiologicalComponent("esophagus", "Esophagus", "digestive", CoverageStatus.PLANNED),
    BiologicalComponent("stomach", "Stomach", "digestive", CoverageStatus.PLANNED),
    BiologicalComponent("intestine", "Small and large intestine", "digestive", CoverageStatus.PLANNED),
    BiologicalComponent("liver", "Liver", "digestive", CoverageStatus.PLANNED),
    BiologicalComponent("pancreas", "Pancreas", "digestive", CoverageStatus.PLANNED),
    BiologicalComponent("gallbladder", "Gallbladder", "digestive", CoverageStatus.PLANNED),
    BiologicalComponent("microbiome", "Microbiome interface", "digestive", CoverageStatus.PLANNED),
    BiologicalComponent("kidney", "Kidneys and filtration", "renal", CoverageStatus.PLANNED),
    BiologicalComponent("acid_base", "Acid-base regulation", "renal", CoverageStatus.PLANNED),
    BiologicalComponent("bone", "Bone", "musculoskeletal", CoverageStatus.PLANNED),
    BiologicalComponent("joint", "Joints", "musculoskeletal", CoverageStatus.PLANNED),
    BiologicalComponent("muscle", "Skeletal muscle", "musculoskeletal", CoverageStatus.PLANNED),
    BiologicalComponent("tendon", "Tendons and ligaments", "musculoskeletal", CoverageStatus.PLANNED),
    BiologicalComponent("proprioception", "Proprioception", "sensory", CoverageStatus.PLANNED),
    BiologicalComponent("skin", "Skin and barrier", "integumentary", CoverageStatus.PLANNED),
    BiologicalComponent("pain", "Pain sensing", "sensory", CoverageStatus.PLANNED),
    BiologicalComponent("temperature", "Thermoregulation", "homeostasis", CoverageStatus.IMPLEMENTED),
    BiologicalComponent("reproductive", "Reproductive/developmental state", "developmental", CoverageStatus.PLANNED),
    BiologicalComponent("homeostasis", "Whole-organism homeostasis", "system", CoverageStatus.IMPLEMENTED),
]


def missing_components(catalog: Iterable[BiologicalComponent] = MINIMUM_CATALOG) -> list[BiologicalComponent]:
    return [item for item in catalog if item.status in {CoverageStatus.UNMODELED, CoverageStatus.PLANNED}]
