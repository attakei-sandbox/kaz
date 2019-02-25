import os
import os.path
from pathlib import Path
import textwrap

import click

from . import __version__ as ver
from .core import Application, DEFAULT_ROOT_DIR


ROOT_DIR_ENV = 'KAZ_ROOT'


def find_appdir():
    """Find application directory for CLI
    """
    if ROOT_DIR_ENV in os.environ:
        return Path(os.environ[ROOT_DIR_ENV])
    return Path.home() / DEFAULT_ROOT_DIR


@click.group()
def cmd():
    """Portable application manager"""
    pass


@cmd.command()
def version():
    """Display version"""
    msg = 'kaz {}'
    click.echo(msg.format(ver))


@cmd.command()
@click.argument(
    'root',
    default=os.path.expanduser('~/' + DEFAULT_ROOT_DIR),
    type=click.Path(resolve_path=True))
def init(root):
    """Initialize kaz env

    If you don't specify ROOT as initialize target,
    kaz initialize target is used '~/.kaz'.
    """
    root = Path(root)
    if root.exists():
        click.echo(
            'Path is already exists. Please specify non-exists path.',
            err=True)
        return
    app = Application(root)
    app.create()
    click.echo(textwrap.dedent("""
    Thank you for using kaz.
    Initialize is finished in {root}.

    Next your steps:
        1. Set your root directory into environment
        export KAZ_ROOT={root}
        2. Set bin directory of kaz into enviroment variables PATH
        export PATH={root}/bin:$PATH
    """.format(root=root)).strip())


def main():
    """Etrypoint"""
    cmd()
