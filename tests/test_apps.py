"""Tests of kaz application container
"""
import os
from pathlib import Path
from tempfile import mkdtemp


def test_app_instance():
    from kaz.core import Application
    app = Application()
    assert app.root == Path.home() / '.kaz'


def test_app_custom_root():
    from kaz.core import Application
    root = mkdtemp()
    app = Application(root)
    assert app.root == Path(root)


def test_app_create():
    from kaz.core import Application, DEFAULT_ROOT_DIR
    root = os.path.join(mkdtemp(), DEFAULT_ROOT_DIR)
    app = Application(root)
    app.create()
    root = Path(root)
    assert root.exists()
    assert (root / 'bin').exists()
    assert (root / 'log').exists()
    assert (root / 'repo').exists()
    assert (root / 'log' / 'kaz.log').exists()


def test_app_create_duplicated(capsys):
    from kaz.core import Application, DEFAULT_ROOT_DIR
    root = os.path.join(mkdtemp(), DEFAULT_ROOT_DIR)
    app = Application(root)
    app.create()
    app.create()
    cap = capsys.readouterr()
    assert 'Application path is already exists' in cap.err
