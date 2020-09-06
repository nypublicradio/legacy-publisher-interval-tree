#!/usr/bin/env python
"""
interval_tree
======

Command line tool to dump data to sentry.

"""

from setuptools import setup

setup(
    name='itree',
    version='.'.join(map(str, (0,0,0))),
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

