"""Canonical anatomy/physiology inventory.

The catalog is intentionally explicit: external and internal anatomy are tracked
so missing coverage is visible. Status describes software implementation, not
biological equivalence.
"""
from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum


class CoverageStatus(StrEnum):
    IMPLEMENTED = "IMPLEMENTED"
    ABSTRACTED = "ABSTRACTED"
    PLANNED = "PLANNED"
    UNMODELED = "UNMODELED"


@dataclass(frozen=True)
class AnatomyNode:
    id: str
    name: str
    scale: str
    system: str
    parent: str | None
    function: str
    status: CoverageStatus
    notes: str = ""


ANATOMY: tuple[AnatomyNode, ...] = (
    # External integument and appendages
    AnatomyNode("skin", "Skin", "organ", "integumentary", None, "Barrier, sensation, thermoregulation", CoverageStatus.ABSTRACTED),
    AnatomyNode("epidermis", "Epidermis", "tissue", "integumentary", "skin", "Outer barrier layer", CoverageStatus.ABSTRACTED),
    AnatomyNode("dermis", "Dermis", "tissue", "integumentary", "skin", "Connective tissue, vessels, nerves", CoverageStatus.ABSTRACTED),
    AnatomyNode("hair", "Hair", "appendage", "integumentary", "skin", "Protection and thermoregulatory contribution", CoverageStatus.ABSTRACTED),
    AnatomyNode("hair_follicle", "Hair follicle", "microstructure", "integumentary", "hair", "Hair production interface", CoverageStatus.ABSTRACTED),
    AnatomyNode("sebaceous_gland", "Sebaceous gland", "gland", "integumentary", "skin", "Sebum secretion", CoverageStatus.ABSTRACTED),
    AnatomyNode("sweat_gland", "Sweat gland", "gland", "integumentary", "skin", "Thermoregulatory secretion", CoverageStatus.ABSTRACTED),
    AnatomyNode("nail", "Nail", "appendage", "integumentary", None, "Distal digit protection", CoverageStatus.ABSTRACTED),
    AnatomyNode("nail_bed", "Nail bed", "tissue", "integumentary", "nail", "Supports nail plate", CoverageStatus.ABSTRACTED),
    AnatomyNode("fingers", "Fingers", "region", "musculoskeletal", None, "Fine manipulation and touch", CoverageStatus.ABSTRACTED),
    AnatomyNode("toes", "Toes", "region", "musculoskeletal", None, "Balance and propulsion", CoverageStatus.ABSTRACTED),
    AnatomyNode("upper_limb", "Upper limb", "region", "musculoskeletal", None, "Reach and manipulation", CoverageStatus.ABSTRACTED),
    AnatomyNode("lower_limb", "Lower limb", "region", "musculoskeletal", None, "Support, gait and propulsion", CoverageStatus.ABSTRACTED),

    # Head/oral/airway interfaces
    AnatomyNode("nose", "Nose", "organ", "respiratory", None, "Air entry, filtration and olfaction", CoverageStatus.ABSTRACTED),
    AnatomyNode("nasal_cavity", "Nasal cavity", "cavity", "respiratory", "nose", "Condition incoming air", CoverageStatus.ABSTRACTED),
    AnatomyNode("mouth", "Mouth", "organ_region", "digestive", None, "Food intake and speech interface", CoverageStatus.ABSTRACTED),
    AnatomyNode("teeth", "Teeth", "organ", "digestive", "mouth", "Mechanical food breakdown", CoverageStatus.ABSTRACTED),
    AnatomyNode("tongue", "Tongue", "organ", "digestive", "mouth", "Manipulation, swallowing and taste", CoverageStatus.ABSTRACTED),
    AnatomyNode("salivary_glands", "Salivary glands", "gland", "digestive", "mouth", "Saliva secretion", CoverageStatus.ABSTRACTED),
    AnatomyNode("pharynx", "Pharynx", "tube", "respiratory_digestive", None, "Shared passage for air and food", CoverageStatus.ABSTRACTED),
    AnatomyNode("larynx", "Larynx", "organ_region", "respiratory", "pharynx", "Airway protection and phonation", CoverageStatus.ABSTRACTED),

    # Major organ systems
    AnatomyNode("brain", "Brain", "organ", "nervous", None, "Integration, learning, action control", CoverageStatus.ABSTRACTED),
    AnatomyNode("spinal_cord", "Spinal cord", "organ", "nervous", None, "Signal relay and reflex integration", CoverageStatus.ABSTRACTED),
    AnatomyNode("heart", "Heart", "organ", "cardiovascular", None, "Blood pumping", CoverageStatus.ABSTRACTED),
    AnatomyNode("lungs", "Lungs", "organ", "respiratory", None, "Gas exchange", CoverageStatus.ABSTRACTED),
    AnatomyNode("stomach", "Stomach", "organ", "digestive", None, "Mechanical/chemical digestion", CoverageStatus.ABSTRACTED),
    AnatomyNode("small_intestine", "Small intestine", "organ", "digestive", None, "Digestion and nutrient absorption", CoverageStatus.ABSTRACTED),
    AnatomyNode("large_intestine", "Large intestine", "organ", "digestive", None, "Water/electrolyte recovery and fecal processing", CoverageStatus.ABSTRACTED),
    AnatomyNode("liver", "Liver", "organ", "hepatobiliary", None, "Metabolism, synthesis, detoxification and bile production", CoverageStatus.ABSTRACTED),
    AnatomyNode("gallbladder", "Gallbladder", "organ", "hepatobiliary", None, "Bile storage and release", CoverageStatus.ABSTRACTED),
    AnatomyNode("pancreas", "Pancreas", "organ", "digestive_endocrine", None, "Digestive enzymes and endocrine regulation", CoverageStatus.ABSTRACTED),
    AnatomyNode("kidneys", "Kidneys", "organs", "renal", None, "Filtration, fluid/electrolyte and acid-base regulation", CoverageStatus.ABSTRACTED),
    AnatomyNode("ureters", "Ureters", "tube", "urinary", None, "Urine transport", CoverageStatus.ABSTRACTED),
    AnatomyNode("bladder", "Urinary bladder", "organ", "urinary", None, "Urine storage", CoverageStatus.ABSTRACTED),
    AnatomyNode("urethra", "Urethra", "tube", "urinary", None, "Urine outflow", CoverageStatus.ABSTRACTED),
    AnatomyNode("spleen", "Spleen", "organ", "immune_lymphatic", None, "Blood filtration and immune functions", CoverageStatus.ABSTRACTED),
    AnatomyNode("lymph_nodes", "Lymph nodes", "organs", "lymphatic", None, "Immune surveillance and lymph filtering", CoverageStatus.ABSTRACTED),
    AnatomyNode("thyroid", "Thyroid", "gland", "endocrine", None, "Metabolic regulation", CoverageStatus.ABSTRACTED),
    AnatomyNode("pituitary", "Pituitary", "gland", "endocrine", None, "Hormonal control", CoverageStatus.ABSTRACTED),
    AnatomyNode("adrenal_glands", "Adrenal glands", "glands", "endocrine", None, "Stress and metabolic signaling", CoverageStatus.ABSTRACTED),
    AnatomyNode("reproductive_organs", "Reproductive organs", "organs", "reproductive", None, "Reproduction and endocrine functions", CoverageStatus.ABSTRACTED),

    # Cellular / molecular substrate
    AnatomyNode("cell_membrane", "Cell membrane", "organelle", "cellular", None, "Selective transport and signaling", CoverageStatus.ABSTRACTED),
    AnatomyNode("cytoplasm", "Cytoplasm", "cellular_compartment", "cellular", None, "Intracellular chemical environment", CoverageStatus.ABSTRACTED),
    AnatomyNode("nucleus", "Nucleus", "organelle", "cellular_genetic", None, "Genome storage and regulation", CoverageStatus.ABSTRACTED),
    AnatomyNode("mitochondria", "Mitochondria", "organelle", "cellular_metabolic", None, "Energy metabolism", CoverageStatus.ABSTRACTED),
    AnatomyNode("ribosomes", "Ribosomes", "organelle", "cellular_genetic", None, "Protein synthesis machinery", CoverageStatus.ABSTRACTED),
    AnatomyNode("endoplasmic_reticulum", "Endoplasmic reticulum", "organelle", "cellular", None, "Protein/lipid processing", CoverageStatus.ABSTRACTED),
    AnatomyNode("golgi_apparatus", "Golgi apparatus", "organelle", "cellular", None, "Protein/lipid modification and trafficking", CoverageStatus.ABSTRACTED),
    AnatomyNode("lysosomes", "Lysosomes", "organelle", "cellular", None, "Intracellular degradation", CoverageStatus.ABSTRACTED),
    AnatomyNode("dna", "DNA", "molecule", "genetic", None, "Information storage", CoverageStatus.ABSTRACTED),
    AnatomyNode("rna", "RNA", "molecule", "genetic", None, "Gene-expression intermediates", CoverageStatus.ABSTRACTED),
    AnatomyNode("proteins", "Proteins", "molecule", "molecular", None, "Structure, catalysis, transport and signaling", CoverageStatus.ABSTRACTED),
    AnatomyNode("lipids", "Lipids", "molecule", "metabolic", None, "Membranes, storage and signaling", CoverageStatus.ABSTRACTED),
    AnatomyNode("fatty_acids", "Fatty acids", "molecule", "metabolic", None, "Energy substrates and membrane components", CoverageStatus.ABSTRACTED),
    AnatomyNode("omega_3", "Omega-3 fatty acids", "molecule_group", "metabolic", "fatty_acids", "Lipid substrates/signaling precursors", CoverageStatus.ABSTRACTED),
    AnatomyNode("omega_6", "Omega-6 fatty acids", "molecule_group", "metabolic", "fatty_acids", "Lipid substrates/signaling precursors", CoverageStatus.ABSTRACTED),
    AnatomyNode("carbohydrates", "Carbohydrates", "molecule_group", "metabolic", None, "Energy substrates", CoverageStatus.ABSTRACTED),
    AnatomyNode("amino_acids", "Amino acids", "molecule_group", "metabolic", None, "Protein building blocks and metabolic substrates", CoverageStatus.ABSTRACTED),
    AnatomyNode("vitamins", "Vitamins", "molecule_group", "metabolic", None, "Micronutrient cofactor/signaling roles", CoverageStatus.ABSTRACTED),
    AnatomyNode("minerals", "Minerals", "molecule_group", "metabolic", None, "Electrolyte/cofactor/structural roles", CoverageStatus.ABSTRACTED),
    AnatomyNode("water", "Water", "molecule", "fluid_balance", None, "Solvent and fluid-balance substrate", CoverageStatus.ABSTRACTED),
    AnatomyNode("oxygen", "Oxygen", "molecule", "respiratory", None, "Oxidative metabolism substrate", CoverageStatus.ABSTRACTED),
    AnatomyNode("carbon_dioxide", "Carbon dioxide", "molecule", "respiratory", None, "Metabolic waste and acid-base signal", CoverageStatus.ABSTRACTED),

    # Blood/immune
    AnatomyNode("blood", "Blood", "fluid_tissue", "hematologic", None, "Transport and regulation", CoverageStatus.ABSTRACTED),
    AnatomyNode("red_blood_cells", "Red blood cells", "cell_population", "hematologic", "blood", "Gas transport", CoverageStatus.ABSTRACTED),
    AnatomyNode("white_blood_cells", "White blood cells", "cell_population", "immune", "blood", "Immune surveillance and response", CoverageStatus.ABSTRACTED),
    AnatomyNode("platelets", "Platelets", "cell_fragment_population", "hematologic", "blood", "Hemostasis", CoverageStatus.ABSTRACTED),
    AnatomyNode("hemoglobin", "Hemoglobin", "protein", "hematologic", "red_blood_cells", "Oxygen/carbon-dioxide transport contribution", CoverageStatus.ABSTRACTED),

    # Waste/outputs and material intake
    AnatomyNode("urine", "Urine", "output_fluid", "urinary", None, "Excretory output carrying water, solutes and waste", CoverageStatus.ABSTRACTED),
    AnatomyNode("feces", "Feces", "output_material", "digestive", None, "Digestive waste output", CoverageStatus.ABSTRACTED),
    AnatomyNode("air_intake", "Air intake", "input_flow", "respiratory", None, "Environmental gas input", CoverageStatus.ABSTRACTED),
    AnatomyNode("food_intake", "Food intake", "input_flow", "digestive", None, "Nutrient and energy input", CoverageStatus.ABSTRACTED),
    AnatomyNode("water_intake", "Water intake", "input_flow", "fluid_balance", None, "Fluid input", CoverageStatus.ABSTRACTED),
)


def by_status(status: CoverageStatus) -> tuple[AnatomyNode, ...]:
    return tuple(item for item in ANATOMY if item.status is status)


def summary() -> dict[str, int]:
    result = {status.value: 0 for status in CoverageStatus}
    for item in ANATOMY:
        result[item.status.value] += 1
    result["TOTAL"] = len(ANATOMY)
    return result


def validate_unique_ids() -> None:
    ids = [item.id for item in ANATOMY]
    duplicates = {item for item in ids if ids.count(item) > 1}
    if duplicates:
        raise AssertionError(f"Duplicate anatomy ids: {sorted(duplicates)}")
