import click

from .. import __version__ as ver
from . import (
    app as app_cmds,
    repo as repo_cmds,
)


@click.group()
def cmd():
    """Portable application manager"""
    pass


@cmd.command()
def version():
    """Display version"""
    msg = 'kaz {}'
    click.echo(msg.format(ver))


def main():
    """Etrypoint"""
    app_cmds.register(cmd)
    repo_cmds.register(cmd)
    cmd()
