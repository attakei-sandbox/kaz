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


@cmd.command()
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


@cmd.command()
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


@cmd.command()
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


def main():
    """Etrypoint"""
    cmd()
