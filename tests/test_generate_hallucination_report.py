from collections import Counter
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path


SCRIPT_PATH = Path(__file__).resolve().parents[1] / "scripts" / "generate_hallucination_report.py"
SPEC = spec_from_file_location("generate_hallucination_report", SCRIPT_PATH)
generate_hallucination_report = module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(generate_hallucination_report)

chart_distribution_series = generate_hallucination_report.chart_distribution_series
summary_from_scan_report = generate_hallucination_report.summary_from_scan_report


def test_chart_distribution_series_uses_exact_bars_and_cumulative_percentages():
    summary = {
        "distribution": Counter({1: 2, 3: 1}),
        "total_papers": 10,
    }

    x_values, exact_counts, threshold_pct = chart_distribution_series(summary)

    assert x_values == [1, 2, 3]
    assert exact_counts == [2, 0, 1]
    assert threshold_pct == [30.0, 10.0, 10.0]


def test_summary_from_scan_report_uses_processed_papers_for_percent_denominator():
    scan_report = {
        "summary": {"total_papers_processed": 10},
        "papers": [
            {"source_paper_id": "a", "flagged_records": 1, "total_records": 4},
            {"source_paper_id": "b", "flagged_records": 3, "total_records": 5},
        ],
    }

    summary = summary_from_scan_report(scan_report)
    x_values, exact_counts, threshold_pct = chart_distribution_series(summary)

    assert summary["total_papers"] == 10
    assert x_values == [1, 2, 3]
    assert exact_counts == [1, 0, 1]
    assert threshold_pct == [20.0, 10.0, 10.0]
