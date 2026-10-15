import logging
from pathlib import Path


LOG_FOLDER = Path("logs")
LOG_FILE = LOG_FOLDER / "app.log"

LOG_FOLDER.mkdir(parents=True, exist_ok=True)


logging.basicConfig(
    filename=str(LOG_FILE),
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def log_info(message):
    """Write an informational message to the application log."""
    logging.info(message)


def log_error(message):
    """Write an error message to the application log."""
    logging.error(message)
