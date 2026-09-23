from trice.runtime.model_interface import ModelInterface


class _Echo:
    def predict(self, observation):
        return observation

    def update(self, observation, target):
        return sum(abs(a - b) for a, b in zip(observation, target))


def test_model_interface_shape():
    model: ModelInterface = _Echo()
    assert list(model.predict([1.0, 2.0])) == [1.0, 2.0]
    assert model.update([1.0], [0.5]) == 0.5
