from pathlib import Path


def test_compute_stack_documented():
    text = Path("docs/COMPUTE_STACK.md").read_text()
    required = ("Python", "C++", "CUDA", "Rust", "Go", "PyTorch", "JAX", "TensorFlow",
                "NumPy", "Pandas", "Polars", "DeepSpeed", "Megatron-LM", "FSDP",
                "Ray", "Dask", "Spark", "Weights & Biases", "MLflow", "Kubeflow", "SQL")
    assert all(name in text for name in required)
