import os.path
from pathlib import Path
from tempfile import mkdtemp

from kaz.catalog import Catalog


def test_handle_versions():
    catalog = Catalog()
    catalog.add_version('0.0.1')
    assert len(catalog.versions) == 1


def test_add_version_latest():
    catalog = Catalog()
    catalog.add_version('0.0.2')
    catalog.add_version('0.0.1')
    assert len(catalog.versions) == 2
    assert catalog.latest == '0.0.1'


def test_save():
    catalog_file = os.path.join(mkdtemp(), 'catalog.json')
    catalog_file = Path(catalog_file)
    catalog = Catalog()
    catalog.add_version('0.0.1')
    catalog.save(catalog_file)
    assert catalog_file.exists() is True
    catalog_text = catalog_file.read_text()
    assert catalog_text.count('"0.0.1"', 2)


def test_load():
    catalog_file = Path(os.path.join(mkdtemp(), 'catalog.json'))
    catalog_file.write_text('{"versions":["0.0.1"],"latest":"0.0.1"}')
    catalog = Catalog()
    catalog.load(catalog_file)
    assert len(catalog.versions) == 1
    assert catalog.latest == '0.0.1'
