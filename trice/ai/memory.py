"""Agent memory adapter using existing TRICE memory semantics."""
from dataclasses import dataclass, field

@dataclass
class AgentMemory:
    capacity:int=256
    traces:list[tuple[str,float]]=field(default_factory=list)

    def store(self,key:str,value:float)->None:
        self.traces.append((str(key),float(value)))
        if len(self.traces)>max(1,self.capacity):
            self.traces=self.traces[-self.capacity:]

    def recall(self,key:str)->float:
        for k,v in reversed(self.traces):
            if k==key: return v
        return 0.0
