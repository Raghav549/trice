from trice.core.provenance_record import ProvenanceRecord
def test_provenance_validates():
    ProvenanceRecord("heart","internal-model",confidence=.5).validate()
