'''
CRT
'''
from __future__ import absolute_import
from crt._version import get_versions
from crt import compute
from crt import template


__version__ = get_versions()['version']
del get_versions

__all__ = [
    'compute',
    'template',
]
