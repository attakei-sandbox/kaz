import click

from ..core import Application
from . import cmd, find_appdir


@cmd.command(name='pull')
@click.argument('name')
def handler(name):
    """Pull latest distribution package"""
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
    repo = app.get_repo(name)
    repo.pull()
