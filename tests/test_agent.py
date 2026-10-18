import pytest

from src.agent import investigate


def test_investigation_accepts_request():
    result = investigate("Improve progress visibility")
    assert result["status"] == "investigation_ready"
    assert result["demo_only"] is True


def test_investigation_rejects_empty_request():
    with pytest.raises(ValueError):
        investigate("   ")
