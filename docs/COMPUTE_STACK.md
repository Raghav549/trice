# TRICE Compute Stack

TRICE keeps the core simulator dependency-light and treats heavyweight numerical,
distributed, and experiment systems as optional integrations.

## Language/runtime roles
- Python: orchestration, research models, APIs and tests.
- C++: future native kernels for performance-critical deterministic operations.
- CUDA: future GPU kernels; never required for CPU-only execution.
- Rust: future memory-safe high-throughput services and data-plane utilities.
- Go: future service/control-plane components.

## ML/data roles
- PyTorch, JAX, TensorFlow: interchangeable model/training adapters.
- NumPy: reference array backend.
- Pandas, Polars: analysis/data pipelines.
- DeepSpeed, Megatron-LM, FSDP: scalable training adapters.
- Ray, Dask, Apache Spark: distributed execution adapters.
- Weights & Biases, MLflow: experiment tracking adapters.
- Kubeflow: pipeline/deployment integration.
- SQL: persistent experiment/state metadata.

Optional frameworks are isolated behind adapters; importing core TRICE should not
require any heavyweight optional dependency.
