from trice.human.coverage_report import build_report


def test_coverage_report_counts_layers():
    report = build_report([
        {"layer": "molecular"},
        {"layer": "organ"},
        {"layer": "organ"},
        {"layer": "whole_body"},
    ])
    assert report.organ == 2
    assert report.total == 4
