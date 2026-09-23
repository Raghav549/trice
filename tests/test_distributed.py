from trice.runtime.distributed import DistributedPlan, map_batches


def test_distributed_reference_semantics():
    result = map_batches([1, 2, 3], lambda x: x * 2, DistributedPlan(workers=2))
    assert result == [2, 4, 6]


def test_distributed_plan_defaults_to_local():
    assert DistributedPlan().backend == "local"
