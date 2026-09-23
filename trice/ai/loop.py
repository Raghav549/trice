"""Agent-environment loop connecting observations, policy and body actions."""
from __future__ import annotations
from dataclasses import dataclass, field
from .policy import Policy
from .state import AgentState

@dataclass
class AgentLoop:
    policy:Policy=field(default_factory=Policy)
    state:AgentState=field(default_factory=AgentState)

    def step(self, observations:dict[str,float])->dict[str,float]:
        self.state.observations=dict(observations)
        action=self.policy.act(observations)
        self.state.actions=dict(action)
        self.state.reward=float(observations.get("reward",0.0))
        self.state.confidence=max(0.0,min(1.0,1.0-abs(self.state.reward)*0.25))
        return action
