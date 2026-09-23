"""Bridge between the legacy subsystem models and the human state surface."""
from __future__ import annotations

from collections.abc import Mapping

from trice.core.observations import observe
from trice.human.body_state import HumanState


def ingest_body_state(human: HumanState, body_state: Mapping[str, float]) -> None:
    obs = observe(body_state)
    human.internal.body_energy = max(0.0, min(1.0, obs["body_energy"]))
    human.internal.glucose = max(0.0, obs["glucose"])
    human.internal.oxygen = max(0.0, obs["oxygen"])
    human.internal.temperature = obs["temperature"]
    human.behavior.fatigue = max(0.0, min(1.0, 1.0 - human.internal.body_energy))
    human.behavior.threat = max(0.0, min(1.0, obs["stress"]))
    human.mind.attention = max(0.0, min(1.0, obs["attention"]))
    human.mind.arousal = max(0.0, min(1.0, obs["arousal"]))


def export_human_state(human: HumanState) -> dict[str, float]:
    return {
        "body_energy": human.internal.body_energy,
        "glucose": human.internal.glucose,
        "oxygen": human.internal.oxygen,
        "temperature": human.internal.temperature,
        "stress": human.behavior.threat,
        "attention": human.mind.attention,
        "arousal": human.mind.arousal,
        "pain": human.internal.pain,
    }
