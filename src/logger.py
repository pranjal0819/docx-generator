import logging

from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)


class ColoredFormatter(logging.Formatter):
    """Custom formatter to color log messages based on their level."""

    COLORS = {
        "DEBUG": Fore.BLUE,
        "INFO": Fore.GREEN,
        "WARNING": Fore.YELLOW,
        "ERROR": Fore.RED,
        "CRITICAL": Fore.RED + Style.BRIGHT,
        "RESET": Style.RESET_ALL,
    }

    def format(self, record: logging.LogRecord) -> str:
        color = self.COLORS.get(record.levelname, self.COLORS["RESET"])
        reset = self.COLORS["RESET"]
        return f"{color}{super().format(record)}{reset}"


def setup_logger(name: str) -> logging.Logger:
    """
    Set up a logger with a specified name and return it.
    """
    logger = logging.getLogger(name)
    handler = logging.StreamHandler()
    formatter = ColoredFormatter("%(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)  # Default level
    return logger


def set_log_level(logger: logging.Logger, level_name: str):
    """
    Set the logging level of the specified logger based on user input.
    """
    levels = {
        "debug": logging.DEBUG,
        "info": logging.INFO,
        "warning": logging.WARNING,
        "error": logging.ERROR,
        "critical": logging.CRITICAL,
    }
    level = levels.get(level_name.lower())
    if level is not None:
        logger.setLevel(level)
        logger.info(f"Logging level set to {level_name.upper()}.")
    else:
        logger.warning("Invalid logging level. Using default INFO level.")
