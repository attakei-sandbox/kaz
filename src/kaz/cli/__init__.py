"""CLI endpoint and utils
"""
import importlib
import os
from pathlib import Path

import click

from ..core import DEFAULT_ROOT_DIR


ROOT_DIR_ENV = 'KAZ_ROOT'


def find_appdir():
    """Find application directory for CLI

    :returns: application root directory
    """
    if ROOT_DIR_ENV in os.environ:
        return Path(os.environ[ROOT_DIR_ENV])
    return Path.home() / DEFAULT_ROOT_DIR


@click.group()
def cmd():
    """Portable application manager"""
    pass


def main():
    """Etrypoint

    Find and import submodules as command entrypoint
    """
    commands_dir = Path(__file__).parent
    for module in commands_dir.glob('*.py'):
        if module.name.startswith('__'):
            continue
        importlib.import_module(__name__ + '.' + module.stem)
    cmd()
