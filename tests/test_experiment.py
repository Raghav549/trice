from trice.core.experiment import Experiment


def test_experiment_parameters_are_normalized():
    exp = Experiment("baseline", seed=7, parameters={"b": 2, "a": 1})
    assert exp.normalized_parameters() == {"a": 1.0, "b": 2.0}
