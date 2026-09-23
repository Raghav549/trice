"""Policy-to-action normalization boundary."""
from __future__ import annotations

from collections.abc import Mapping

from .action_space import Action


def select_action(raw: Mapping[str, float]) -> Action:
    """Convert arbitrary policy output into the validated action space."""
    movement = max(-1.0, min(1.0, float(raw.get("movement", 0.0))))
    attention = max(0.0, min(1.0, float(raw.get("attention", 0.0))))
    return Action(movement=movement, attention=attention)
