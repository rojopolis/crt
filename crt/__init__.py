'''
CRT
'''
from ._version import get_versions
from . import cli
from . import compute

__version__ = get_versions()['version']
del get_versions

__all__ = [
    'cli',
    'compute'
]
