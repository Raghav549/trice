import pytest

from trice.runtime.experiment_logger import ExperimentLogger


def test_disabled_logger_is_noop():
    logger = ExperimentLogger(enabled=False)
    logger.start({"lr": 1e-3})
    logger.log({"loss": 0.2}, step=1)
    logger.close()


def test_unknown_backend_rejected_when_enabled():
    with pytest.raises(ValueError):
        ExperimentLogger(enabled=True, backend="unknown").start()
