import os
import os.path
from pathlib import Path

from ..core import DEFAULT_ROOT_DIR


ROOT_DIR_ENV = 'KAZ_ROOT'


def find_appdir():
    """Find application directory for CLI
    """
    if ROOT_DIR_ENV in os.environ:
        return Path(os.environ[ROOT_DIR_ENV])
    return Path.home() / DEFAULT_ROOT_DIR
