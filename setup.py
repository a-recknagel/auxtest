import sys

from setuptools import find_packages, setup

if sys.version_info < (3, 6):
    raise RuntimeError("This module requires at least Python 3.6.")

try:
    from src.auxtest.settings import VERSION
except ImportError:
    VERSION = '0.0.0'

setup(
    version=VERSION,
    install_requires=[
        'flask',
        'requests',
    ],
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
)
