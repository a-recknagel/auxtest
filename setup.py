import sys

from setuptools import find_packages, setup

if sys.version_info < (3, 6):
    raise RuntimeError("This module requires at least Python 3.6.")

setup(
    version='1.0.0',
    install_requires=[
        'flask',
        'requests',
    ],
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
)
