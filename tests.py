import unittest
import mock
from mock_import import mock_import


class TestMockImport(unittest.TestCase):

    def test_mock_import_empty(self):
        """
        Basic test case of mock_import
        """
        try:
            with mock_import():
                import no_such_module
                no_such_module.not_such_function()
        except (ImportError, AttributeError):
            self.fail('mock_import failed')

        @mock_import()
        def some_method():
            import no_such_module2
            no_such_module2.not_such_function()

        try:
            some_method()
        except (ImportError, AttributeError):
            self.fail('mock_import failed')

    def test_mock_import_scoping(self):
        """
        Use module outside of scope should raise a name error.
        """
        with mock_import():
            import no_such_module

        self.assertIsInstance(no_such_module, mock.MagicMock)

        with self.assertRaises(ImportError):
            import no_such_module

    def test_mock_import_outside_scope(self):
        """
        Import module outside of scope should raise an import error.
        """
        with self.assertRaises(ImportError):
            with mock_import():
                pass
            import no_such_module

    def test_mock_import_do_not_mock(self):
        """
        Importing non-existing module explicitly
        asked not to mock, should raise import error
        """
        with self.assertRaises(ImportError):
            with mock_import(do_not_mock='no_such_module'):
                import no_such_module
        with self.assertRaises(ImportError):
            with mock_import(do_not_mock='no_such_module'):
                import no_such_module.inner_module

        try:
            with mock_import(do_not_mock='no_such_module'):
                import no_such
                import no_such_module_not
                import no_such_module_not.inner_module
        except ImportError:
            self.fail('mock_import do_not_mock failed')

    def test_mock_import_do_not_mock_list(self):
        """
        Importing non-existing module explicitly
        asked not to mock, by list, should raise import error
        """
        do_not_mock = ['no_such_module1', 'no_such_module2']
        with self.assertRaises(ImportError):
            with mock_import(do_not_mock=do_not_mock):
                import no_such_module1

        with self.assertRaises(ImportError):
            with mock_import(do_not_mock=do_not_mock):
                import no_such_module2

        with self.assertRaises(ImportError):
            with mock_import(do_not_mock=do_not_mock):
                import no_such_module1.inner

        try:
            with mock_import(do_not_mock=do_not_mock):
                import no_such
                import no_such_module1_not
                import no_such_module2_not
                import no_such_module1_not.inner_module
                import no_such_module2_not.inner_module
        except ImportError:
            self.fail('mock_import do_not_mock failed')

    def test_mock_import_kwargs(self):
        with mock_import(not_such_function=mock.MagicMock(return_value=1)):
            import no_such_module
            return_value = no_such_module.not_such_function()
            self.assertEqual(return_value, 1)
