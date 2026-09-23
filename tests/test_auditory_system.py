from trice.human.auditory_system import AuditorySystem


def test_auditory_system_extracts_salience():
    result = AuditorySystem().ingest(loudness=0.5, pitch=0.7, spatial=0.25)
    assert result["auditory_salience"] == 0.4
    assert result["auditory_pitch"] == 0.7
