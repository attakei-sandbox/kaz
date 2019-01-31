"""Tests of kaz application container
"""
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
