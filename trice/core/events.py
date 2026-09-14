"""Typed event primitives used for explicit cross-system coupling."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Mapping


@dataclass(frozen=True)
class Event:
    """Immutable event emitted by a body subsystem."""

    time: float
    source: str
    kind: str
    payload: Mapping[str, Any]


class EventBus:
    """Deterministic in-process event bus for simulation steps."""

    def __init__(self) -> None:
        self._events: list[Event] = []

    def emit(self, event: Event) -> None:
        self._events.append(event)

    def drain(self) -> tuple[Event, ...]:
        events = tuple(self._events)
        self._events.clear()
        return events

    def peek(self) -> tuple[Event, ...]:
        return tuple(self._events)
