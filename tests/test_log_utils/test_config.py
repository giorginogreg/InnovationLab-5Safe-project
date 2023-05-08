from il_5safe.logs_utils.config import CUSTOM_LEVELS


def test_custom_levels():
    assert isinstance(CUSTOM_LEVELS, dict)
    assert "INFO" in CUSTOM_LEVELS
    assert "SUCCESS" in CUSTOM_LEVELS
    assert "WARNING" in CUSTOM_LEVELS
    assert "ERROR" in CUSTOM_LEVELS
    assert "CRITICAL" in CUSTOM_LEVELS
