import json
from pathlib import Path

REPORT_PATH = Path("/app/report.json")


def load_report():
    assert REPORT_PATH.exists(), "no /app/report.json found"
    try:
        return json.loads(REPORT_PATH.read_text())
    except json.JSONDecodeError as exc:
        raise AssertionError("/app/report.json is not valid JSON") from exc


def test_report_is_json_with_required_schema():
    """Verifies success criterion 1: exact JSON output path and object schema."""
    report = load_report()
    assert isinstance(report, dict), "report must be a JSON object"
    assert set(report) == {"total_requests", "unique_ips", "top_path"}


def test_total_requests():
    """Verifies success criterion 2: count all non-empty log records."""
    value = load_report()["total_requests"]
    assert type(value) is int, "total_requests must be an integer"
    assert value == 6


def test_unique_ips():
    """Verifies success criterion 3: count distinct client IP addresses."""
    value = load_report()["unique_ips"]
    assert type(value) is int, "unique_ips must be an integer"
    assert value == 3


def test_top_path():
    """Verifies success criterion 4: report the most frequent request path."""
    value = load_report()["top_path"]
    assert isinstance(value, str), "top_path must be a string"
    assert value == "/index.html"
