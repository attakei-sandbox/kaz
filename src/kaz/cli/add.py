import click

from . import find_appdir, cmd
from ..core import Application


@cmd.command(name='add')
@click.argument('name')
@click.argument('asset')
def handler(name, asset):
    root = find_appdir()
    if not root.exists():
        click.echo(
            click.style('WARNING:', fg='yellow', bg='magenta'), nl=False)
        click.echo(
            click.style(' Root directory is not exists', fg='magenta'))
        return
    app = Application(root)
    if app.repo_exists(name):
        click.echo(click.style(
            'Application "{}" is already registered.'.format(name),
            fg='magenta'))
        return
    github_path = click.prompt('Enter GitHub project path(xxx/yyy)')
    if len(github_path.split('/')) != 2:
        click.echo(click.style('Invalid path is passed', fg='magenta'))
        return
    app.add_repo(
        name,
        {'vendor': 'github', 'path': github_path, 'asset': asset})
