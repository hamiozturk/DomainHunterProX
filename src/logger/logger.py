import logging
import sys


def create_logger(name: str) -> logging.Logger:

    logger = logging.getLogger(name)

    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "[%(levelname)s] %(name)s - %(message)s"
    )

    handler = logging.StreamHandler(sys.stdout)

    handler.setFormatter(formatter)

    logger.addHandler(handler)

    logger.propagate = False

    return logger