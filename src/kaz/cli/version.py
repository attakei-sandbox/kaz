import click

from .. import __version__ as ver
from . import cmd


@cmd.command()
def version():
    """Display version"""
    msg = 'kaz {}'
    click.echo(msg.format(ver))
