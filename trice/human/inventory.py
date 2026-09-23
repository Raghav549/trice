"""Machine-readable whole-human subsystem inventory."""
from __future__ import annotations

from dataclasses import dataclass

from .anatomy_layers import BiologicalLayer


@dataclass(frozen=True)
class HumanComponent:
    name: str
    layer: BiologicalLayer
    domain: str
    status: str = "ABSTRACTED"
    description: str = ""


COMPONENTS = (
    HumanComponent("genome", BiologicalLayer.MOLECULAR, "genetics", "ABSTRACTED", "DNA/genetic state"),
    HumanComponent("cellular_state", BiologicalLayer.CELLULAR, "cell biology", "ABSTRACTED", "generic cell state"),
    HumanComponent("blood", BiologicalLayer.TISSUE, "hematology", "ABSTRACTED", "circulating blood abstraction"),
    HumanComponent("heart", BiologicalLayer.ORGAN, "cardiovascular", "ABSTRACTED", "cardiac state"),
    HumanComponent("lungs", BiologicalLayer.ORGAN, "respiratory", "ABSTRACTED", "gas exchange abstraction"),
    HumanComponent("kidneys", BiologicalLayer.ORGAN, "renal", "ABSTRACTED", "renal regulation abstraction"),
    HumanComponent("brain", BiologicalLayer.ORGAN, "nervous", "ABSTRACTED", "cognitive/neural state"),
    HumanComponent("nervous_system", BiologicalLayer.SYSTEM, "nervous", "ABSTRACTED", "sensory and neural integration"),
    HumanComponent("endocrine_system", BiologicalLayer.SYSTEM, "endocrine", "ABSTRACTED", "hormonal regulation"),
    HumanComponent("immune_system", BiologicalLayer.SYSTEM, "immune", "ABSTRACTED", "immune signaling and defense"),
    HumanComponent("musculoskeletal_system", BiologicalLayer.SYSTEM, "movement", "ABSTRACTED", "movement mechanics"),
    HumanComponent("whole_body_homeostasis", BiologicalLayer.WHOLE_BODY, "homeostasis", "ABSTRACTED", "integrated regulation"),
    HumanComponent("mind_behavior", BiologicalLayer.WHOLE_BODY, "cognition", "ABSTRACTED", "perception, cognition and action"),
)


def inventory_by_layer(layer: BiologicalLayer) -> tuple[HumanComponent, ...]:
    return tuple(component for component in COMPONENTS if component.layer is layer)
