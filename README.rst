mock_import
===========

.. image:: https://travis-ci.org/posener/mock-import.svg?branch=master
       :target: https://travis-ci.org/posener/mock-import

.. image:: https://badge.fury.io/py/mock-import.svg
       :target: https://pypi.python.org/pypi/mock-import

.. image:: https://codecov.io/gh/posener/mock-import/branch/master/graph/badge.svg
     :target: https://codecov.io/gh/posener/mock-import

A helper mocking function to mask ``ImportError`` s on a scoped code.
Failed imports will be ignored, unless specified by the *do_not_mock* argument.

Installation
------------

Using pip: ``pip install mock-import``

Usage
-----

Import:
    >>> from mock_import import mock_import

Mocking import for a code block:
    >>> with mock_import():
    ...     import no_such_module  # Won't raise ImportError
    ...     no_such_module.no_such_function()  # Won't raise AttributeError


Mocking import as a decorator:
    >>> @mock_import()
    ... def method():
    ...     import no_such_module  # Won't raise ImportError
    ...     no_such_module.no_such_function()  # Won't raise AttributeError

    >>>     import no_such_module  # raises ImportError

Making an exception:
    >>> with mock_import(do_not_mock='no_such_module'):
    ...     import no_such_other_module  # Won't raise ImportError
    ...     import no_such_module  # Will raise ImportError

    >>> with mock_import(do_not_mock=['nsm1', 'nsm2']):
    ...     import nsm  # Won't raise ImportError
    ...     import nsm1  # Will raise ImportError
    ...     import nsm2  # Will raise ImportError
