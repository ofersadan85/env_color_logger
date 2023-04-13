import logging
import tempfile

from env_color_logger import EnvLogger


def test_env_logger_default_values(monkeypatch):
    monkeypatch.delenv("LOG_FILE_ROTATE", raising=False)
    monkeypatch.delenv("LOG_FILE_PATH", raising=False)
    monkeypatch.delenv("LOG_FILE_SIZE", raising=False)
    monkeypatch.delenv("LOG_FORMAT", raising=False)
    monkeypatch.delenv("LOG_LEVEL", raising=False)
    monkeypatch.delenv("LOG_COLOR", raising=False)

    logger = EnvLogger("test_logger")

    assert logger.level == logging.INFO
    assert len(logger.handlers) == 1
    assert isinstance(logger.handlers[0], logging.StreamHandler)


def test_env_logger_with_file_rotate(monkeypatch):
    with tempfile.TemporaryDirectory() as tempdir:
        monkeypatch.setenv("LOG_FILE_ROTATE", "3")
        monkeypatch.setenv("LOG_FILE_PATH", tempdir)
        monkeypatch.setenv("LOG_FILE_SIZE", "1024")

        logger = EnvLogger("test_logger")

        assert logger.level == logging.INFO
        assert len(logger.handlers) == 2
        assert isinstance(logger.handlers[1], logging.handlers.RotatingFileHandler)

        file_handler = logger.handlers[1]
        assert file_handler.maxBytes == 1024
        assert file_handler.backupCount == 3

        # Close the file handler to avoid locking the file(s) on Windows
        for handler in logger.handlers:
            handler.close()
