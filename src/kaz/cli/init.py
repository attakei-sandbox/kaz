import os
import textwrap
from pathlib import Path

import click

from ..core import Application, DEFAULT_ROOT_DIR
from . import cmd


@cmd.command(name='init')
@click.argument(
    'root',
    default=os.path.expanduser('~/' + DEFAULT_ROOT_DIR),
    type=click.Path(resolve_path=True))
def handler(root):
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
