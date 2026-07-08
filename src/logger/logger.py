from pathlib import Path
from loguru import logger
import sys

APP_NAME = "DomainHunter Pro X"

BASE_DIR = Path(__file__).resolve().parents[2]
LOG_DIR = BASE_DIR / "logs"

LOG_DIR.mkdir(parents=True, exist_ok=True)

logger.remove()

logger.add(
    sys.stdout,
    level="INFO",
    colorize=True,
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
           "<level>{level: <8}</level> | "
           "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - "
           "<level>{message}</level>"
)

logger.add(
    LOG_DIR / "application.log",
    rotation="10 MB",
    retention=20,
    compression="zip",
    level="DEBUG",
    enqueue=True,
    encoding="utf-8"
)

logger.info(f"{APP_NAME} Logger initialized.")