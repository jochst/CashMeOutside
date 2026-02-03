"""
Utility functions for the application
"""
import logging
from typing import Any

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


def log_info(message: str, **kwargs: Any) -> None:
    """Log info message"""
    logger.info(message, extra=kwargs)


def log_error(message: str, **kwargs: Any) -> None:
    """Log error message"""
    logger.error(message, extra=kwargs)


def log_warning(message: str, **kwargs: Any) -> None:
    """Log warning message"""
    logger.warning(message, extra=kwargs)
