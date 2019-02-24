from pathlib import Path

import click

from . import __version__ as ver
from .core import Application


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
@click.argument('root', type=click.Path(resolve_path=True))
def init(root):
    """Initialize kaz env"""
    root = Path(root)
    if root.exists():
        click.echo(
            'Path is already exists. Please specify non-exists path.',
            err=True)
        return
    app = Application(root)
    app.create()
    # TODO: Display follow-up message


def main():
    """Etrypoint"""
    cmd()
