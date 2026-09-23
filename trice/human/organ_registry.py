"""Whole-human organ and system registry."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class SystemDomain(str, Enum):
    NERVOUS = "nervous"
    SENSORY = "sensory"
    CARDIOVASCULAR = "cardiovascular"
    RESPIRATORY = "respiratory"
    DIGESTIVE = "digestive"
    RENAL = "renal"
    ENDOCRINE = "endocrine"
    IMMUNE = "immune"
    MUSCULOSKELETAL = "musculoskeletal"
    INTEGUMENTARY = "integumentary"
    REPRODUCTIVE = "reproductive"


@dataclass(frozen=True)
class OrganSpec:
    name: str
    domain: SystemDomain
    status: str = "ABSTRACTED"


ORGANS = (
    OrganSpec("brain", SystemDomain.NERVOUS),
    OrganSpec("spinal_cord", SystemDomain.NERVOUS),
    OrganSpec("eyes", SystemDomain.SENSORY),
    OrganSpec("ears", SystemDomain.SENSORY),
    OrganSpec("heart", SystemDomain.CARDIOVASCULAR),
    OrganSpec("lungs", SystemDomain.RESPIRATORY),
    OrganSpec("stomach", SystemDomain.DIGESTIVE),
    OrganSpec("small_intestine", SystemDomain.DIGESTIVE),
    OrganSpec("large_intestine", SystemDomain.DIGESTIVE),
    OrganSpec("liver", SystemDomain.DIGESTIVE),
    OrganSpec("kidneys", SystemDomain.RENAL),
    OrganSpec("bladder", SystemDomain.RENAL),
    OrganSpec("pituitary", SystemDomain.ENDOCRINE),
    OrganSpec("thyroid", SystemDomain.ENDOCRINE),
    OrganSpec("adrenals", SystemDomain.ENDOCRINE),
    OrganSpec("spleen", SystemDomain.IMMUNE),
    OrganSpec("bone_marrow", SystemDomain.IMMUNE),
    OrganSpec("bones", SystemDomain.MUSCULOSKELETAL),
    OrganSpec("skeletal_muscle", SystemDomain.MUSCULOSKELETAL),
    OrganSpec("skin", SystemDomain.INTEGUMENTARY),
    OrganSpec("reproductive_organs", SystemDomain.REPRODUCTIVE),
)


def organs_for(domain: SystemDomain) -> tuple[OrganSpec, ...]:
    return tuple(organ for organ in ORGANS if organ.domain is domain)
