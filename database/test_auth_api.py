import os
import unittest

from database import AuthAPI


class TestAuthAPI(unittest.TestCase):
    def setUp(self):
        self.db = AuthAPI('test.db')

    def tearDown(self):
        if os.path.exists('test.db'):
            os.remove('test.db')
        else:
            print("The file does not exist")

    def test_user_set_password(self):
        self.assertFalse(self.db.is_user_set_password())
        self.assertTrue(self.db.add_new_password('123'))
        self.assertTrue(self.db.is_user_set_password())


