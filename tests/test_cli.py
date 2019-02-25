from pathlib import Path
from tempfile import mkdtemp
from unittest import mock

from kaz.cli import find_appdir


def test_app_dir_default():
    app_dir = find_appdir()
    assert app_dir == Path.home() / '.kaz'


def test_app_dir_by_env():
    root = Path(mkdtemp())
    with mock.patch.dict('os.environ', KAZ_ROOT=str(root)):
        app_dir = find_appdir()
        assert app_dir == root
