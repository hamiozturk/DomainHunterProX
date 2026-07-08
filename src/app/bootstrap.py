import sys

from src.logger import logger
from src.config import ConfigManager
from src.database import Database

from src.app.application import Application
from src.ui.main_window import MainWindow


def bootstrap():

    logger.info("Starting application...")

    config = ConfigManager()

    database = Database()

    app = Application(sys.argv)

    window = MainWindow(config, database)

    window.show()

    logger.success("Application started successfully.")

    sys.exit(app.exec())