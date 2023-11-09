import os
import unittest

from database.auth import AuthDB


class TestAuthDB(unittest.TestCase):
    def setUp(self):
        # self.db = AuthDB(':memory:')  # Use an in-memory database for testing
        self.db = AuthDB('test.db')  # Use an in-memory database for testing

    def tearDown(self):
        self.db.connection.close()
        if os.path.exists('test.db'):
            os.remove('test.db')
        else:
            print("The file does not exist")

    def test_create_auth_table(self):
        self.db.create_auth_table()
        result = self.db.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Auth'", fetchone=True)
        # print(result)
        self.assertEqual(result[0], 'Auth')

    def test_add_password(self):
        self.db.add_password('test_password')
        result = self.db.select_all_passwords()
        # print(result)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0][1], 'test_password')

    def test_select_password(self):
        result = self.db.select_password(password='some_password')
        self.assertIsNone(result)

        self.db.add_password('test_password')
        result = self.db.select_password(password='test_password')
        self.assertEqual(result[1], 'test_password')

    def test_count_passwords(self):
        self.assertEqual(self.db.count_passwords(), 0)
        self.db.add_password('test_password')
        self.assertEqual(self.db.count_passwords(), 1)

    def test_update_password(self):
        self.db.add_password('test_password')
        self.db.update_password(1, 'new_password')
        result = self.db.select_password(id=1)
        self.assertEqual(result[1], 'new_password')

    def test_update_invalid_password(self):
        self.db.update_password(0, 'new_password')
        result = self.db.select_password(id=0)
        self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main()

