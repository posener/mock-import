import mock
import six


__all__ = ['mock_import']


_builtins_import = six.moves.builtins.__import__


def _to_list(str_none_or_list):
    if str_none_or_list is None:
        str_none_or_list = []
    elif isinstance(str_none_or_list, str):
        str_none_or_list = [str_none_or_list]
    return str_none_or_list


def mock_import(do_not_mock=None, **mock_kwargs):
    """
    Mocks import statement, and disable ImportError if a module
    could not be imported.
    :param do_not_mock: a list of prefixes of modules that should
        exists, and an ImportError could be raised for.
    :param mock_kwargs: kwargs for MagicMock object.
    :return: patch object
    """

    do_not_mock = _to_list(do_not_mock)

    def try_import(module_name, *args, **kwargs):
        try:
            return _builtins_import(module_name, *args, **kwargs)
        except:
            if any((module_name == prefix or module_name.startswith(prefix + '.')
                    for prefix in do_not_mock)):
                # This is a module we need to import, so we don't mock it
                # and raise the exception
                raise
            # Mock external module so we can peacefully create our client
            return mock.MagicMock(**mock_kwargs)

    return mock.patch('six.moves.builtins.__import__', try_import)
