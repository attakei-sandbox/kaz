"""Catalog and sub child components
"""
import json


class Catalog(object):
    """Application catalog

    Control local management application version and installed flag.
    This catalog does not manage how to get applications
    """
    def __init__(self):
        self.versions = []
        self.latest = None
        self.installed = None

    def add_version(self, version):
        """Add new version.

        :params version: version string
        """
        self.versions.append(version)
        self.latest = version

    def save(self, dest):
        """Save catalog data into JSON file
        """
        with dest.open('w') as fp:
            json.dump(self.__dict__, fp)

    def load(self, src):
        """Load catalog data from JSON file
        """
        data = json.loads(src.read_text())
        self.versions = data.get('versions', [])
        self.latest = data.get('latest', None)
        self.installed = data.get('installed', None)
