from trice.runtime.scaling import DEEPSPEED, FSDP, MEGATRON


def test_scaling_strategies_have_explicit_names():
    for strategy in (FSDP, DEEPSPEED, MEGATRON):
        strategy.validate()
        assert strategy.total_devices == 1
