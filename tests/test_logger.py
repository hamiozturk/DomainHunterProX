from src.logger import create_logger


def test_logger():

    logger = create_logger("DomainHunter")

    logger.info("Logger çalışıyor.")

    logger.warning("Warning örneği.")

    logger.error("Error örneği.")


if __name__ == "__main__":
    test_logger()