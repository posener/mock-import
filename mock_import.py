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


def _match(module_name, name_to_ignore):
    """
    check if `module_name` should be ignored

    :param str|unicode module_name: name that is being imported
    :param str|unicode name_to_ignore: name that should not be mocked
    :return: True if the `module_name` should not be mocked
    :rtype: bool
    """
    return (
        module_name == name_to_ignore or
        module_name.startswith(name_to_ignore + '.')
    )


def mock_import(do_not_mock=None, do_mock=None, **mock_kwargs):
    """
    Mocks import statements by ignoring ImportErrors
    and replacing the missing module with a Mock.

    :param str|unicode|list[str|unicode] do_not_mock: names of modules
        that should exists, and an ImportError could be raised for.
    :param str|unicode|list[str|unicode] do_mock: in case this parameter is
        specified only modules from `do_mock` will be mocked.
    :param mock_kwargs: kwargs for MagicMock object.
    :return: patch object
    """

    do_not_mock = _to_list(do_not_mock)

    def try_import(module_name, *args, **kwargs):
        try:
            return _builtins_import(module_name, *args, **kwargs)
        except:    # intentionally catch all exceptions
            if any((_match(module_name, prefix) for prefix in do_not_mock)):
                # This is a module we need to import,
                # so we raise the exception instead of mocking it
                raise
            if do_mock and not any((_match(module_name, prefix) for prefix in do_mock)):
                raise
            # Mock external module so we can peacefully create our client
            return mock.MagicMock(**mock_kwargs)

    return mock.patch('six.moves.builtins.__import__', try_import)
