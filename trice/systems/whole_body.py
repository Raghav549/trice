"""Whole-body subsystem registry and coupling primitives.

The registry is intentionally explicit: a body component must be registered
before it can be reported as implemented. Statuses are computational metadata,
not claims of biological equivalence.
"""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Dict, Iterable


class CoverageStatus(str, Enum):
    IMPLEMENTED = "IMPLEMENTED"
    ABSTRACTED = "ABSTRACTED"
    PLANNED = "PLANNED"
    UNMODELED = "UNMODELED"


@dataclass(frozen=True)
class BiologicalComponent:
    name: str
    layer: str
    status: CoverageStatus
    description: str = ""


# Minimum explicit registry. The list is deliberately broad so omissions are visible.
COMPONENTS: tuple[BiologicalComponent, ...] = (
    BiologicalComponent("atoms", "physical", CoverageStatus.ABSTRACTED),
    BiologicalComponent("ions", "physical", CoverageStatus.ABSTRACTED),
    BiologicalComponent("water", "physical", CoverageStatus.ABSTRACTED),
    BiologicalComponent("electrolytes", "physical", CoverageStatus.ABSTRACTED),
    BiologicalComponent("minerals", "physical", CoverageStatus.ABSTRACTED),
    BiologicalComponent("vitamins", "chemical", CoverageStatus.ABSTRACTED),
    BiologicalComponent("amino_acids", "chemical", CoverageStatus.ABSTRACTED),
    BiologicalComponent("lipids", "chemical", CoverageStatus.ABSTRACTED),
    BiologicalComponent("carbohydrates", "chemical", CoverageStatus.ABSTRACTED),
    BiologicalComponent("dna", "genetic", CoverageStatus.ABSTRACTED),
    BiologicalComponent("rna", "genetic", CoverageStatus.ABSTRACTED),
    BiologicalComponent("genes", "genetic", CoverageStatus.ABSTRACTED),
    BiologicalComponent("epigenetic_state", "genetic", CoverageStatus.ABSTRACTED),
    BiologicalComponent("nucleus", "cellular", CoverageStatus.ABSTRACTED),
    BiologicalComponent("mitochondria", "cellular", CoverageStatus.ABSTRACTED),
    BiologicalComponent("ribosomes", "cellular", CoverageStatus.ABSTRACTED),
    BiologicalComponent("endoplasmic_reticulum", "cellular", CoverageStatus.ABSTRACTED),
    BiologicalComponent("golgi_apparatus", "cellular", CoverageStatus.ABSTRACTED),
    BiologicalComponent("lysosomes", "cellular", CoverageStatus.ABSTRACTED),
    BiologicalComponent("peroxisomes", "cellular", CoverageStatus.ABSTRACTED),
    BiologicalComponent("cytoskeleton", "cellular", CoverageStatus.ABSTRACTED),
    BiologicalComponent("cell_membrane", "cellular", CoverageStatus.ABSTRACTED),
    BiologicalComponent("red_blood_cells", "blood", CoverageStatus.ABSTRACTED),
    BiologicalComponent("white_blood_cells", "blood", CoverageStatus.ABSTRACTED),
    BiologicalComponent("platelets", "blood", CoverageStatus.ABSTRACTED),
    BiologicalComponent("plasma", "blood", CoverageStatus.ABSTRACTED),
    BiologicalComponent("hemoglobin", "blood", CoverageStatus.ABSTRACTED),
    BiologicalComponent("heart", "cardiovascular", CoverageStatus.ABSTRACTED),
    BiologicalComponent("arteries", "cardiovascular", CoverageStatus.ABSTRACTED),
    BiologicalComponent("veins", "cardiovascular", CoverageStatus.ABSTRACTED),
    BiologicalComponent("capillaries", "cardiovascular", CoverageStatus.ABSTRACTED),
    BiologicalComponent("lungs", "respiratory", CoverageStatus.ABSTRACTED),
    BiologicalComponent("trachea", "respiratory", CoverageStatus.ABSTRACTED),
    BiologicalComponent("bronchi", "respiratory", CoverageStatus.ABSTRACTED),
    BiologicalComponent("alveoli", "respiratory", CoverageStatus.ABSTRACTED),
    BiologicalComponent("mouth", "digestive", CoverageStatus.ABSTRACTED),
    BiologicalComponent("esophagus", "digestive", CoverageStatus.ABSTRACTED),
    BiologicalComponent("stomach", "digestive", CoverageStatus.ABSTRACTED),
    BiologicalComponent("small_intestine", "digestive", CoverageStatus.ABSTRACTED),
    BiologicalComponent("large_intestine", "digestive", CoverageStatus.ABSTRACTED),
    BiologicalComponent("rectum", "digestive", CoverageStatus.ABSTRACTED),
    BiologicalComponent("anus", "digestive", CoverageStatus.ABSTRACTED),
    BiologicalComponent("liver", "hepatobiliary", CoverageStatus.ABSTRACTED),
    BiologicalComponent("gallbladder", "hepatobiliary", CoverageStatus.ABSTRACTED),
    BiologicalComponent("pancreas", "digestive", CoverageStatus.ABSTRACTED),
    BiologicalComponent("kidneys", "renal", CoverageStatus.ABSTRACTED),
    BiologicalComponent("nephrons", "renal", CoverageStatus.ABSTRACTED),
    BiologicalComponent("ureters", "urinary", CoverageStatus.ABSTRACTED),
    BiologicalComponent("bladder", "urinary", CoverageStatus.ABSTRACTED),
    BiologicalComponent("urethra", "urinary", CoverageStatus.ABSTRACTED),
    BiologicalComponent("bones", "musculoskeletal", CoverageStatus.ABSTRACTED),
    BiologicalComponent("joints", "musculoskeletal", CoverageStatus.ABSTRACTED),
    BiologicalComponent("cartilage", "musculoskeletal", CoverageStatus.ABSTRACTED),
    BiologicalComponent("skeletal_muscle", "musculoskeletal", CoverageStatus.ABSTRACTED),
    BiologicalComponent("tendons", "musculoskeletal", CoverageStatus.ABSTRACTED),
    BiologicalComponent("ligaments", "musculoskeletal", CoverageStatus.ABSTRACTED),
    BiologicalComponent("skin", "integumentary", CoverageStatus.ABSTRACTED),
    BiologicalComponent("neurons", "nervous", CoverageStatus.ABSTRACTED),
    BiologicalComponent("glial_cells", "nervous", CoverageStatus.ABSTRACTED),
    BiologicalComponent("dendrites", "nervous", CoverageStatus.ABSTRACTED),
    BiologicalComponent("axons", "nervous", CoverageStatus.ABSTRACTED),
    BiologicalComponent("synapses", "nervous", CoverageStatus.ABSTRACTED),
    BiologicalComponent("myelin", "nervous", CoverageStatus.ABSTRACTED),
    BiologicalComponent("hippocampal_memory", "brain", CoverageStatus.ABSTRACTED),
    BiologicalComponent("prefrontal_control", "brain", CoverageStatus.ABSTRACTED),
    BiologicalComponent("amygdala_value_threat", "brain", CoverageStatus.ABSTRACTED),
    BiologicalComponent("hypothalamic_regulation", "brain", CoverageStatus.ABSTRACTED),
    BiologicalComponent("basal_ganglia_action_selection", "brain", CoverageStatus.ABSTRACTED),
    BiologicalComponent("cerebellar_motor_learning", "brain", CoverageStatus.ABSTRACTED),
    BiologicalComponent("brainstem_autonomic_control", "brain", CoverageStatus.ABSTRACTED),
    BiologicalComponent("neurotransmitters", "neural_chemistry", CoverageStatus.ABSTRACTED),
    BiologicalComponent("dopamine", "neural_chemistry", CoverageStatus.ABSTRACTED),
    BiologicalComponent("serotonin", "neural_chemistry", CoverageStatus.ABSTRACTED),
    BiologicalComponent("endorphins", "neural_chemistry", CoverageStatus.ABSTRACTED),
    BiologicalComponent("electrical_impulses", "nervous", CoverageStatus.ABSTRACTED),
    BiologicalComponent("endocrine_glands", "endocrine", CoverageStatus.ABSTRACTED),
    BiologicalComponent("hormonal_signals", "endocrine", CoverageStatus.ABSTRACTED),
    BiologicalComponent("immune_system", "immune", CoverageStatus.ABSTRACTED),
    BiologicalComponent("innate_immunity", "immune", CoverageStatus.ABSTRACTED),
    BiologicalComponent("adaptive_immunity", "immune", CoverageStatus.ABSTRACTED),
    BiologicalComponent("reproductive_system", "reproductive", CoverageStatus.ABSTRACTED),
    BiologicalComponent("sensory_systems", "sensory", CoverageStatus.ABSTRACTED),
    BiologicalComponent("vestibular_system", "sensory", CoverageStatus.ABSTRACTED),
    BiologicalComponent("microbiome_interface", "digestive", CoverageStatus.ABSTRACTED),
)


def coverage_map() -> Dict[str, BiologicalComponent]:
    return {c.name: c for c in COMPONENTS}


def coverage_by_status(status: CoverageStatus) -> Iterable[BiologicalComponent]:
    return tuple(c for c in COMPONENTS if c.status is status)
