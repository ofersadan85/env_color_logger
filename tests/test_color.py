import logging

import pytest

from env_color_logger import Color, ColorFormatter, EnvLogger, default_color_map


def test_color_formatter_format():
    formatter = ColorFormatter("%(levelname)s: %(message)s", default_color_map)
    record = logging.LogRecord(
        "test_logger", logging.DEBUG, "test.py", 42, "test message", [], None
    )

    formatted_message = formatter.format(record)
    assert formatted_message.startswith(Color.BLUE.value)
    assert formatted_message.endswith(Color.RESET.value)
    assert "DEBUG: test message" in formatted_message


@pytest.mark.parametrize(
    "env_value,expected_color",
    [
        ("true", True),
        ("1", True),
        ("yes", True),
        ("false", False),
        ("0", False),
        ("no", False),
    ],
)
def test_env_logger_color_output(monkeypatch, env_value, expected_color):
    monkeypatch.setenv("LOG_COLOR", env_value)
    logger = EnvLogger("test_logger")
    formatter = logger.handlers[0].formatter

    if expected_color:
        assert isinstance(formatter, ColorFormatter)
    else:
        assert not isinstance(formatter, ColorFormatter)
