import pytest

from trice.human.vital_signs import VitalSigns


def test_vital_signs_validate():
    VitalSigns().validate()


def test_vital_signs_reject_invalid_oxygen():
    with pytest.raises(ValueError):
        VitalSigns(oxygen_saturation=1.5).validate()
