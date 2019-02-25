"""Repository for GitHub releases
"""
import fnmatch
import json

import requests
from github import Github

from ..catalog import Catalog


class Repository(object):
    def __init__(self):
        self.repo_path = None
        self.metadata = None
        self.catalog = Catalog()
        self.metadata_path = None
        self.catalog_path = None

    def load(self, repo_path):
        self.repo_path = repo_path
        self.metadata_path = repo_path / 'metadata.json'
        self.metadata = json.loads(self.metadata_path.read_text())
        self.catalog_path = repo_path / 'catalog.json'
        self.catalog.load(self.catalog_path)

    def pull(self):
        gh = Github()
        repo = gh.get_repo(self.metadata['path'])
        release = repo.get_latest_release()
        assets = [
            asset
            for asset in release.get_assets()
            if fnmatch.fnmatch(asset.name, self.metadata['asset'])]
        # TODO: format for click?
        if len(assets) > 1:
            print('warning')
            return
        asset = assets[0]
        print('Download version {} ({}) ...'.format(
            release.title, asset.name
        ))
        asset_path = self.repo_path / release.title
        with asset_path.open('wb') as fp:
            resp = requests.get(asset.browser_download_url)
            fp.write(resp.content)
        asset_path.chmod(0o700)
        self.catalog.add_version(release.title)
        self.catalog.save(self.catalog_path)
        print('Done!')
