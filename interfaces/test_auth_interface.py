import os
import unittest

from interfaces import AppInterface
from interfaces.exceptions import AuthInterfaceExceptions
from database import AuthAPI


class TestAuthInterface(unittest.TestCase):
    def setUp(self):
        self.AuthInterface = AppInterface.AuthInterface
        new_AuthAPI_db = AuthAPI('test.db')

        self.AuthInterface.auth_db_api = new_AuthAPI_db

    def tearDown(self):
        if os.path.exists('test.db'):
            os.remove('test.db')
        else:
            print("The file does not exist")

    def test_is_password_set(self):
        self.assertFalse(self.AuthInterface.is_password_set())
        self.AuthInterface.set_user_password('123')
        self.assertTrue(self.AuthInterface.is_password_set())

    def test_set_user_password(self):
        self.AuthInterface.set_user_password('123')
        passwords = self.AuthInterface.auth_db_api.auth_db.select_all_passwords()

        self.assertEqual(passwords[0][1], '123')
        self.assertEqual(self.AuthInterface.auth_db_api.auth_db.count_passwords(), 1)

    def test_set_user_password_exceptions(self):
        with self.assertRaises(AuthInterfaceExceptions.InvalidPasswordType):
            self.AuthInterface.set_user_password(234)

        self.AuthInterface.set_user_password('123')
        with self.assertRaises(AuthInterfaceExceptions.PasswordAlreadySet):
            self.AuthInterface.set_user_password('123')

    def test_check_password(self):
        self.AuthInterface.set_user_password('123')

        self.assertTrue(self.AuthInterface.check_password('123'))
        self.assertFalse(self.AuthInterface.check_password('404'))

    def test_check_password_exceptions(self):
        with self.assertRaises(AuthInterfaceExceptions.InvalidPasswordType):
            self.AuthInterface.check_password(123)

        with self.assertRaises(AuthInterfaceExceptions.PasswordNotSet):
            self.AuthInterface.check_password("123")

    def test_change_user_password(self):
        with self.assertRaises(AuthInterfaceExceptions.InvalidPasswordType):
            self.AuthInterface.change_user_password(123, 123)
        with self.assertRaises(AuthInterfaceExceptions.InvalidPasswordType):
            self.AuthInterface.change_user_password('123', 123)
        with self.assertRaises(AuthInterfaceExceptions.InvalidPasswordType):
            self.AuthInterface.change_user_password(123, '123')

        with self.assertRaises(AuthInterfaceExceptions.PasswordNotSet):
            self.AuthInterface.change_user_password('old one', 'new one')

        self.AuthInterface.set_user_password('qwerty123')
        with self.assertRaises(AuthInterfaceExceptions.IncorrectPassword):
            self.AuthInterface.change_user_password('not qwery', '68L3g2yebiA1')

        self.AuthInterface.change_user_password('qwerty123', 'I77G')

        self.assertEqual(self.AuthInterface.auth_db_api.auth_db.count_passwords(), 1)

        self.assertIsNotNone(self.AuthInterface.auth_db_api.auth_db.select_password(password='I77G'))
        self.assertEqual(self.AuthInterface.auth_db_api.auth_db.select_password(password='I77G')[1], 'I77G')







