#!/usr/bin/env python
"""
The setup script.
"""
import os
import io
import vppopt
from setuptools import setup, find_packages
#==============Package meta-data==============#
NAME = 'vppopt'
DESCRIPTION = 'Virtual Power Plant Optimization Platform'
URL = 'https://github.com/cenaero-enb/h2cs-design'
EMAIL = 'vanlong.le@cenaero.be'
AUTHOR = 'Van Long Le'
REQUIRES_PYTHON = '>=3.6.0'
VERSION = vppopt.__version__
STATUS = "Underdevelopment"

## What packages are required for this module to be executed?
REQUIRED = [
    # 'pandas',
    # 'oemof.solph'
]

## What packages are optional?
EXTRAS = {
    # 'fancy feature': ['django'],
}

here = os.path.abspath(os.path.dirname(__file__))

# Note: this will only work if 'README.md' is present in your MANIFEST.in file!
try:
    with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description = '\n' + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

# Load the package's __version__.py module as a dictionary.
about = {}
if not VERSION:
    project_slug = NAME.lower().replace("-", "_").replace(" ", "_")
    with open(os.path.join(here, project_slug, '__version__.py')) as f:
        exec(f.read(), about)
else:
    about['__version__'] = VERSION


setup(
    name=NAME,
    version=about['__version__'],
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(exclude=["tests", "*.tests", "*.tests.*", "tests.*"]),
    #package_data={"":["*.cfg"]},
    include_package_data=True,
    entry_points={
        'console_scripts': ['vppopt=vppopt.interfaces.cli:main'],
    },
    install_requires=REQUIRED,
    extras_require=EXTRAS,    
    license='MIT',
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
    ],

)