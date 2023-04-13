import logging
import os
from logging.handlers import RotatingFileHandler
from pathlib import Path

from dotenv import load_dotenv

from .color import Color, ColorFormatter, default_color_map

__all__ = ["EnvLogger", "Color", "ColorFormatter", "default_color_map"]
DEFAULT_FMT = "%(asctime)s %(filename)s:%(lineno)d %(levelname)s: %(message)s"
DEFAULT_FILE_SIZE = 10 * 1024 * 1024  # 10 MB


class EnvLogger(logging.Logger):
    def __init__(self, name: str) -> None:
        load_dotenv()
        try:
            LOG_FILE_ROTATE = int(os.getenv("LOG_FILE_ROTATE", 0))
        except ValueError:
            LOG_FILE_ROTATE = 0
        LOG_FILE_PATH = Path(os.getenv("LOG_FILE_PATH", f"{__name__}.log"))
        if LOG_FILE_PATH.is_dir():
            LOG_FILE_PATH = LOG_FILE_PATH / f"{__name__}.log"
        try:
            LOG_FILE_SIZE = int(os.getenv("LOG_FILE_SIZE", DEFAULT_FILE_SIZE))
        except ValueError:
            LOG_FILE_SIZE = DEFAULT_FILE_SIZE
        LOG_FORMAT = os.getenv("LOG_FORMAT", DEFAULT_FMT)
        LOG_LEVEL = os.getenv("LOG_LEVEL", logging.INFO)
        if os.getenv("LOG_COLOR", "true").lower() in ("true", "1", "yes"):
            stream_formatter = ColorFormatter(LOG_FORMAT)
        else:
            stream_formatter = logging.Formatter(LOG_FORMAT)

        super().__init__(name, LOG_LEVEL)
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(stream_formatter)
        self.addHandler(stream_handler)
        if LOG_FILE_ROTATE > 0:
            file_handler = RotatingFileHandler(
                LOG_FILE_PATH, maxBytes=LOG_FILE_SIZE, backupCount=LOG_FILE_ROTATE
            )
            file_handler.setFormatter(logging.Formatter(LOG_FORMAT))
            self.addHandler(file_handler)
            self.debug(
                f"Logging to file {LOG_FILE_PATH} (max {LOG_FILE_SIZE} bytes, keep {LOG_FILE_ROTATE} files)"
            )
