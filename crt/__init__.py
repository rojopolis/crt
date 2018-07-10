'''
CRT
'''
from ._version import get_versions
from . import cli
from . import compute
from . import template

__version__ = get_versions()['version']
del get_versions

__all__ = [
    'cli',
    'compute',
    'template',
]
