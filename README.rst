mock_import
===========

.. image:: https://travis-ci.org/posener/mock-import.svg?branch=master
       :target: https://travis-ci.org/posener/mock-import

.. image:: https://badge.fury.io/py/mock-import.svg
       :target: https://pypi.python.org/pypi/mock-import

A helper function to mask `ImportError` s on a scoped code, using the `with`
statement, or in method a method used as a decorator.
Failed imports will be ignored, unless specified by the *do_not_mock* argument.

The *do_not_mock* argument is a package or module name, or package or module
names list. When specified, and imported in the scoped mocked code, importing
them must succeed. If `None` (the default) then no import must succeed.

Installation
------------

Using pip: ``pip install import mock``

Usage
-----

Import:
    >>> from mock_import import mock_import

Mocking import for a code block:
    >>> with mock_import():
    ...     import do_not_exists


Mocking import as a decorator:
    >>> @mock_import()
    ... def method():
    ...     import do_not_exists


