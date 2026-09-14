"""Run a tiny TRICE organism simulation."""
from trice.organism import TriceOrganism
from trice.core.module import ModuleContext
from trice.modules import EndocrineModule, ImmuneModule, MemoryModule, NeuralModule


def main() -> None:
    organism = TriceOrganism()
    neural = NeuralModule(neuron_count=16)
    immune = ImmuneModule()
    memory = MemoryModule(capacity=64)
    endocrine = EndocrineModule()

    organism.add_module(neural)
    organism.add_module(immune)
    organism.add_module(memory)
    organism.add_module(endocrine)

    memory.encode(0.8, salience=0.9, context="demo")

    for _ in range(20):
        state = organism.step(
            ModuleContext(
                environment={"darkness": 0.2, "context": "demo"},
                signals={"sensory": 0.65, "anomaly": 0.05},
            )
        )
        print(state.vector())


if __name__ == "__main__":
    main()
