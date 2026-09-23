from trice.runtime.federated import distributed_map, shard


def test_shard_is_deterministic():
    assert shard([0, 1, 2, 3], 2) == [[0, 2], [1, 3]]


def test_distributed_map_reference_semantics():
    assert distributed_map([1, 2, 3], lambda x: x + 1, 2) == [2, 3, 4]
