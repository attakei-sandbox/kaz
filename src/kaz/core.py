"""Core of kaz
"""
import logging
import logging.config
import sys
from pathlib import Path
from .logging import get_logconf


DEFAULT_ROOT_DIR = '.kaz'
Logger = logging.getLogger(__name__)


class Application(object):
    """Main application container
    """
    MOD_DIR = 0o700

    def __init__(self, root=None):
        self.root = Path.home() / DEFAULT_ROOT_DIR \
            if root is None else Path(root).resolve()
        self.logger = Logger.getChild('Application')

    @property
    def log_dir(self):
        return self.root / 'log'

    @property
    def bin_dir(self):
        return self.root / 'bin'

    @property
    def repo_dir(self):
        return self.root / 'repo'

    def create(self):
        """Prepare application root
        """
        try:
            self.root.mkdir(self.MOD_DIR)
        except FileExistsError:
            sys.stderr.write('Application path is already exists.\n')
            return
        self.bin_dir.mkdir(self.MOD_DIR)
        self.log_dir.mkdir(self.MOD_DIR)
        self.repo_dir.mkdir(self.MOD_DIR)
        # Logging handler need to exists output folder
        logging.config.dictConfig(get_logconf(self.log_dir))
        self.logger.info('Initialized!')
