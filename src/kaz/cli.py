import click

from . import __version__ as ver


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
    cmd()
