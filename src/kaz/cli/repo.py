"""List of repository management commands
"""
import click

from .utils import find_appdir
from ..core import Application


@click.argument('name')
@click.argument('asset')
def add(name, asset):
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


@click.argument('name')
def pull(name):
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


@click.argument('name')
@click.argument('version')
def link(name, version):
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


def register(cmd):
    cmd.command()(add)
    cmd.command()(pull)
    cmd.command()(link)
