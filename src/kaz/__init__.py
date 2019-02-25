from pathlib import Path


version_file = Path(__file__).parent / 'version.txt'

__version__ = version_file.read_text().strip()
