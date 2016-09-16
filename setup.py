#! /usr/bin/env python

import setuptools


setuptools.setup(
    name='mock-import',
    version='0.0.2',
    author='Eyal Posener',
    author_email='posener@gmail.com',
    description='A mocking functions for imports',
    keywords='mock import',
    url='http://github.com/posener/mock-import.git',
    packages=['mock_import'],
    install_requires=['mock>=2.0.0'],
)
