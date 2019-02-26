import click

from ..core import Application
from . import cmd, find_appdir


@cmd.command(name='link')
@click.argument('name')
@click.argument('version')
def handler(name, version):
    """Link specify version as enabled command"""
    root = find_appdir()
    if not root.exists():
        click.echo(
            click.style('WARNING:', fg='yellow', bg='magenta'), nl=False)
        click.echo(
            click.style(' Root directory is not exists', fg='magenta'))
        return
    app = Application(root)
    if not app.repo_exists(name):
        click.echo(click.style(
            'Application "{}" is not exists.'.format(name),
            fg='magenta'))
        return
    app.link_repo(name, version)
