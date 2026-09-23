from trice.ai.memory import AgentMemory

def test_memory_roundtrip():
    m=AgentMemory()
    m.store("energy",.8)
    assert m.recall("energy")==.8
