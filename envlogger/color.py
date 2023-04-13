import logging
from enum import StrEnum


class Color(StrEnum):
    WHITE = "\x1b[37;20m"
    WHITE_BOLD = "\x1b[37;1m"
    BLUE = "\x1b[34;20m"
    BLUE_BOLD = "\x1b[34;1m"
    GREY = "\x1b[38;20m"
    GREY_BOLD = "\x1b[38;1m"
    GREEN = "\x1b[32;20m"
    GREEN_BOLD = "\x1b[32;1m"
    YELLOW = "\x1b[33;20m"
    YELLOW_BOLD = "\x1b[33;1m"
    RED = "\x1b[31;20m"
    RED_BOLD = "\x1b[31;1m"
    RESET = "\x1b[0m"


COLOR_MAP_TYPE = dict[int, Color]
default_color_map = {
    logging.DEBUG: Color.BLUE,
    logging.INFO: Color.GREEN,
    logging.WARNING: Color.YELLOW,
    logging.ERROR: Color.RED,
    logging.CRITICAL: Color.RED_BOLD,
}


class ColorFormatter(logging.Formatter):
    def __init__(
        self, fmt: str, color_map: COLOR_MAP_TYPE = default_color_map, **kwargs
    ) -> None:
        self.color_map = color_map
        super().__init__(fmt=fmt, **kwargs)

    def format(self, record: logging.LogRecord) -> str:
        new_fmt = self.color_map[record.levelno] + self._fmt + Color.RESET
        formatter = logging.Formatter(new_fmt)
        return formatter.format(record)
