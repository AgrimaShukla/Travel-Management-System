from functools import wraps
import logging
import sqlite3
from config.prompt import PrintPrompts

logger = logging.getLogger(__name__)


def exception_handler(func):
    """Decorator to handle exceptions"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except sqlite3.OperationalError as err:
            logger.exception(err)
            print(PrintPrompts.UNEXPECTED_ISSUE)
        except sqlite3.IntegrityError as err:
            logger.exception(err)
            print(PrintPrompts.USER_EXISTS)
        except sqlite3.Error as err:
            logger.exception(err)
            print(PrintPrompts.UNEXPECTED_ISSUE)
        except Exception as err:
            logger.exception(err)
            print(PrintPrompts.UNEXPECTED_ISSUE)

    return wrapper