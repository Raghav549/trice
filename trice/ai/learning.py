"""Small, testable online-learning primitive for policy adaptation."""
from dataclasses import dataclass

@dataclass
class AdaptiveScalar:
    value:float=0.0
    learning_rate:float=.05
    def update(self, error:float)->float:
        self.value += self.learning_rate*float(error)
        return self.value
