import pytest

from trice.molecular.genetics import GenomeState, transcribe_dna, translate_rna


def test_dna_to_rna_to_protein_information_flow() -> None:
    dna = "ATGGCCATTGTA"
    rna = transcribe_dna(dna)
    assert rna == "AUGGCCAUUGUA"
    assert translate_rna(rna) == "MAIV"


def test_genome_state_executes_expression_pipeline() -> None:
    genome = GenomeState(
        genes={"demo": 1.0},
        dna_sequences={"demo": "ATGGCC"},
    )
    result = genome.step()
    assert result["active_genes"] == 1.0
    assert genome.mrna_sequences["demo"] == "AUGGCC"
    assert genome.protein_sequences["demo"] == "MA"


def test_invalid_sequences_and_non_finite_signals_fail_fast() -> None:
    with pytest.raises(ValueError):
        transcribe_dna("ATGX")
    with pytest.raises(ValueError):
        translate_rna("AUGX")
    with pytest.raises(ValueError, match="finite"):
        GenomeState(genes={"g": 1.0}).regulate(float("nan"))
