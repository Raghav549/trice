from trice.runtime.training_adapter import TrainingAdapter


def test_training_adapter_supports_requested_frameworks():
    for framework in ("pytorch", "jax", "tensorflow"):
        for strategy in ("single", "fsdp", "deepspeed", "megatron"):
            TrainingAdapter(framework=framework, strategy=strategy).validate()


def test_training_adapter_reference_step():
    adapter = TrainingAdapter()
    assert adapter.step(2, lambda batch: batch * 0.5) == 1.0
