import os
import unittest

from database.desk_api import DeskAPI


# TODO: Gleb
class TestCardsAPI(unittest.TestCase):
    def setUp(self):
        self.db = DeskAPI('test.db')

    def tearDown(self):
        if os.path.exists('test.db'):
            os.remove('test.db')
        else:
            print("The file does not exist")

    def test_some(self):
        self.assertEqual(2+2, 4)
        self.assertNotEqual(2+2, 5)


if __name__ == '__main__':
    unittest.main()
