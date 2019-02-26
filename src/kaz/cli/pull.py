import click

from . import find_appdir, cmd
from ..core import Application


@cmd.command(name='pull')
@click.argument('name')
def handler(name):
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
