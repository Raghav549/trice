"""Layered human-body inventory primitives.

The inventory is intentionally descriptive: it records the modeling layer and
does not imply that each component has a biologically complete simulator.
"""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class BiologicalLayer(str, Enum):
    MOLECULAR = "molecular"
    CELLULAR = "cellular"
    TISSUE = "tissue"
    ORGAN = "organ"
    SYSTEM = "system"
    WHOLE_BODY = "whole_body"


@dataclass(frozen=True)
class AnatomyPart:
    name: str
    layer: BiologicalLayer
    modeled: bool = False
    notes: str = ""


CORE_HUMAN_LAYERS = (
    BiologicalLayer.MOLECULAR,
    BiologicalLayer.CELLULAR,
    BiologicalLayer.TISSUE,
    BiologicalLayer.ORGAN,
    BiologicalLayer.SYSTEM,
    BiologicalLayer.WHOLE_BODY,
)
