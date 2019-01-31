"""Core of kaz
"""
from pathlib import Path


DEFAULT_ROOT_DIR = '.kaz'


class Application(object):
    """Main application container
    """
    def __init__(self, root=None):
        self.root = Path.home() / DEFAULT_ROOT_DIR \
            if root is None else Path(root).resolve()
