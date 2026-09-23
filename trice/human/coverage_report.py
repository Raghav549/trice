"""Whole-human integration report generator."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class CoverageReport:
    molecular: int
    cellular: int
    tissue: int
    organ: int
    system: int
    whole_body: int

    @property
    def total(self) -> int:
        return self.molecular + self.cellular + self.tissue + self.organ + self.system + self.whole_body

    def as_dict(self) -> dict[str, int]:
        return {
            "molecular": self.molecular,
            "cellular": self.cellular,
            "tissue": self.tissue,
            "organ": self.organ,
            "system": self.system,
            "whole_body": self.whole_body,
            "total": self.total,
        }


def build_report(records: list[dict[str, object]]) -> CoverageReport:
    counts = {key: 0 for key in ("molecular", "cellular", "tissue", "organ", "system", "whole_body")}
    for record in records:
        layer = str(record.get("layer", ""))
        if layer in counts:
            counts[layer] += 1
    return CoverageReport(**counts)
