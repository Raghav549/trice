"""Coverage utilities for the declarative anatomy registry."""
from __future__ import annotations

from collections import Counter
from typing import Iterable, Mapping


def status_counts(records: Iterable[Mapping[str, object]]) -> dict[str, int]:
    counts = Counter(str(record.get("status", "UNKNOWN")) for record in records)
    return dict(sorted(counts.items()))


def missing_tests(records: Iterable[Mapping[str, object]]) -> tuple[str, ...]:
    missing: list[str] = []
    for record in records:
        name = str(record.get("name", ""))
        tests = record.get("tests")
        if name and not tests:
            missing.append(name)
    return tuple(sorted(missing))
