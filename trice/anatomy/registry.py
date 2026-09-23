"""Queryable anatomy registry built from the canonical catalog."""
from __future__ import annotations
from .catalog import ANATOMY, AnatomyNode, CoverageStatus

INDEX={node.id:node for node in ANATOMY}

def get(component_id:str)->AnatomyNode:
    return INDEX[component_id]

def missing()->tuple[AnatomyNode,...]:
    return tuple(n for n in ANATOMY if n.status in (CoverageStatus.PLANNED,CoverageStatus.UNMODELED))

def systems()->tuple[str,...]:
    return tuple(sorted({n.system for n in ANATOMY}))

def validate_parents()->None:
    for node in ANATOMY:
        if node.parent is not None and node.parent not in INDEX:
            raise AssertionError(f"Unknown parent {node.parent!r} for {node.id!r}")
