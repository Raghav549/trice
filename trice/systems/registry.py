"""Machine-readable whole-body coverage registry.

This registry is intentionally explicit. A component may only be reported as
implemented when a corresponding executable subsystem exists and is tested.
"""
from __future__ import annotations
from dataclasses import dataclass
from enum import StrEnum


class Status(StrEnum):
    IMPLEMENTED = "IMPLEMENTED"
    ABSTRACTED = "ABSTRACTED"
    PLANNED = "PLANNED"
    UNMODELED = "UNMODELED"


@dataclass(frozen=True)
class Component:
    id: str
    name: str
    system: str
    layer: str
    status: Status


COMPONENTS = [
    Component("brain", "Brain", "nervous", "organ", Status.ABSTRACTED),
    Component("heart", "Heart", "cardiovascular", "organ", Status.ABSTRACTED),
    Component("lungs", "Lungs", "respiratory", "organ", Status.ABSTRACTED),
    Component("liver", "Liver", "hepatobiliary", "organ", Status.ABSTRACTED),
    Component("kidneys", "Kidneys", "renal", "organ", Status.ABSTRACTED),
    Component("stomach", "Stomach", "digestive", "organ", Status.ABSTRACTED),
    Component("small_intestine", "Small intestine", "digestive", "organ", Status.ABSTRACTED),
    Component("large_intestine", "Large intestine", "digestive", "organ", Status.ABSTRACTED),
    Component("pancreas", "Pancreas", "digestive_endocrine", "organ", Status.ABSTRACTED),
    Component("gallbladder", "Gallbladder", "hepatobiliary", "organ", Status.ABSTRACTED),
    Component("spleen", "Spleen", "immune_lymphatic", "organ", Status.ABSTRACTED),
    Component("thyroid", "Thyroid", "endocrine", "organ", Status.ABSTRACTED),
    Component("adrenal_glands", "Adrenal glands", "endocrine", "organ", Status.ABSTRACTED),
    Component("pituitary", "Pituitary gland", "endocrine", "organ", Status.ABSTRACTED),
    Component("hypothalamus", "Hypothalamus", "neuroendocrine", "brain_region", Status.ABSTRACTED),
    Component("skin", "Skin", "integumentary", "organ", Status.ABSTRACTED),
    Component("bones", "Bones", "musculoskeletal", "tissue_system", Status.ABSTRACTED),
    Component("skeletal_muscle", "Skeletal muscle", "musculoskeletal", "tissue_system", Status.ABSTRACTED),
    Component("bone_marrow", "Bone marrow", "hematopoietic", "tissue", Status.ABSTRACTED),
    Component("blood", "Blood", "hematologic", "fluid_tissue", Status.ABSTRACTED),
    Component("immune_system", "Immune system", "immune", "system", Status.ABSTRACTED),
    Component("lymphatic_system", "Lymphatic system", "lymphatic", "system", Status.ABSTRACTED),
    Component("peripheral_nerves", "Peripheral nerves", "nervous", "system", Status.ABSTRACTED),
    Component("sensory_systems", "Sensory systems", "sensory", "system", Status.ABSTRACTED),
    Component("reproductive_system", "Reproductive system", "reproductive", "system", Status.ABSTRACTED),
    Component("genome", "Genome", "genetic", "molecular", Status.ABSTRACTED),
    Component("proteome", "Proteome", "molecular", "molecular", Status.ABSTRACTED),
    Component("mitochondria", "Mitochondria", "cellular", "organelle", Status.ABSTRACTED),
    Component("nucleus", "Nucleus", "cellular", "organelle", Status.ABSTRACTED),
    Component("ribosomes", "Ribosomes", "cellular", "organelle", Status.ABSTRACTED),
    Component("synapses", "Synapses", "nervous", "micro", Status.ABSTRACTED),
    Component("neurotransmitters", "Neurotransmitters", "neural_chemistry", "molecular", Status.ABSTRACTED),
    Component("dopamine", "Dopamine", "neural_chemistry", "molecular", Status.ABSTRACTED),
    Component("serotonin", "Serotonin", "neural_chemistry", "molecular", Status.ABSTRACTED),
    Component("endorphins", "Endorphins", "neural_chemistry", "molecular", Status.ABSTRACTED),
    Component("glial_cells", "Glial cells", "nervous", "cellular", Status.ABSTRACTED),
    Component("rbc", "Red blood cells", "hematologic", "cellular", Status.ABSTRACTED),
    Component("wbc", "White blood cells", "immune_hematologic", "cellular", Status.ABSTRACTED),
    Component("platelets", "Platelets", "hematologic", "cellular", Status.ABSTRACTED),
    Component("hemoglobin", "Hemoglobin", "hematologic", "molecular", Status.ABSTRACTED),
    Component("dna", "DNA", "genetic", "molecular", Status.ABSTRACTED),
    Component("rna", "RNA", "genetic", "molecular", Status.ABSTRACTED),
    Component("genes", "Genes", "genetic", "molecular", Status.ABSTRACTED),
    Component("amino_acids", "Amino acids", "metabolic", "molecular", Status.ABSTRACTED),
    Component("vitamins", "Vitamins", "metabolic", "molecular", Status.ABSTRACTED),
    Component("minerals", "Minerals", "metabolic", "molecular", Status.ABSTRACTED),
    Component("atoms", "Atoms", "physical", "submolecular", Status.ABSTRACTED),
]


def validate_unique_ids() -> None:
    ids = [component.id for component in COMPONENTS]
    duplicates = {item for item in ids if ids.count(item) > 1}
    if duplicates:
        raise AssertionError(f"Duplicate biological component IDs: {sorted(duplicates)}")


def summary() -> dict[str, int]:
    validate_unique_ids()
    out = {status.value: 0 for status in Status}
    for component in COMPONENTS:
        out[component.status.value] += 1
    out["TOTAL"] = len(COMPONENTS)
    return out
