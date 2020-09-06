#!/usr/bin/env python
"""
interval_tree
======

Command line tool to dump data to sentry.

"""

from setuptools import setup
from itree import VERSION as itree_version

setup(
    name='itree',
    version='.'.join(map(str, itree_version)),
    author='Adam DePrince',
    author_email='adeprince@nypublicradio.org',
    description='Interval tree implementation',
    long_description=__doc__,
    py_modules = [
        "interval_tree/itree",
        ],
    packages = ["itree"],
    zip_safe=True,
    license='MIT',
    include_package_data=True,
    classifiers=[
    ],
    url = "https://github.com/wnyc/interval_tree",
    install_requires = [
        ]
)

