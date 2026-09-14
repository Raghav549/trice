"""Runtime fault injection and computational module reconfiguration."""
from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class ModuleHealth:
    score: float = 1.0
    isolated: bool = False
    repair_credit: float = 0.0


@dataclass
class ReconfigurationManager:
    modules: dict[str, ModuleHealth] = field(default_factory=dict)

    def register(self, name: str, health: ModuleHealth | None = None) -> None:
        self.modules.setdefault(name, health or ModuleHealth())

    def inject_fault(self, name: str, severity: float) -> None:
        self.register(name)
        severity = max(0.0, min(1.0, float(severity)))
        module = self.modules[name]
        module.score = max(0.0, module.score - severity)
        if module.score < 0.25:
            module.isolated = True

    def repair(self, name: str, amount: float = 0.1) -> None:
        self.register(name)
        module = self.modules[name]
        module.score = min(1.0, module.score + max(0.0, float(amount)))
        module.repair_credit += max(0.0, float(amount))
        if module.score >= 0.5:
            module.isolated = False

    def healthy_modules(self) -> tuple[str, ...]:
        return tuple(name for name, health in self.modules.items() if not health.isolated)
