from pathlib import Path

from trice.core.checkpoint import load_checkpoint, save_checkpoint
from trice.core.events import Event, EventBus
from trice.core.types import OrganismState


def test_event_bus_is_deterministic() -> None:
    bus = EventBus()
    event = Event(1.0, "test", "signal", {"x": 1})
    bus.emit(event)
    assert bus.peek() == (event,)
    assert bus.drain() == (event,)
    assert bus.peek() == ()


def test_checkpoint_roundtrip(tmp_path: Path) -> None:
    path = tmp_path / "state.json"
    original = OrganismState(time=2.0, energy=0.7, neural=0.2, modules={"heart_rate": 70.0})
    save_checkpoint(path, original, {"experiment": "test"})
    restored, metadata = load_checkpoint(path)
    assert restored.vector() == original.vector()
    assert metadata["experiment"] == "test"
