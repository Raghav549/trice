# Multi-stack build plan

TRICE uses a layered architecture:
- Python owns orchestration and reference semantics.
- C++/CUDA/Rust/Go provide optional native execution paths.
- PyTorch/JAX/TensorFlow provide alternative ML implementations.
- NumPy/Pandas/Polars provide numerical and tabular data paths.
- FSDP/DeepSpeed/Megatron-LM provide scalable training strategies.
- Ray/Dask/Spark provide distributed execution strategies.
- W&B/MLflow provide optional experiment tracking.
- Kubeflow provides workflow/pipeline deployment integration.
- SQL provides persistent experiment and metric metadata.

These integrations are configuration and adapter surfaces first; a backend is only
promoted to production after parity tests against the Python reference path.
