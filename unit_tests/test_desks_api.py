import os
import unittest

from database.desk_api import DeskAPI


class TestCardsAPI(unittest.TestCase):
    def setUp(self):
        self.db = DeskAPI('test.db')

    def tearDown(self):
        if os.path.exists('test.db'):
            os.remove('test.db')
        else:
            print("The file does not exist")

    def test_get_desks(self):
        self.db.add_desk("test_card1")
        self.db.add_desk("test_card2")
        self.db.add_desk("test_card3")

        result = self.db.get_desks()
        self.assertEqual(len(result), 3)
        self.assertEqual(result[0][1], "test_card1")


    def test_get_desk_by_id(self):
        self.db.add_desk("test_card1")
        self.db.add_desk("test_card2")

        result1 = self.db.get_desk_by_id(3)
        self.assertEqual(result1, [])

        result2 = self.db.get_desk_by_id(1)
        self.assertEqual(result2[0][1], "test_card1")


    def test_add_desk(self):
        self.db.add_desk("test_card1")
        self.db.add_desk("test_card2")
        self.db.add_desk("test_card3")

        result = self.db.get_desks()
        self.assertEqual(len(result), 3)
        self.assertEqual(result[0][1], "test_card1")


    def test_rename_desk(self):
        self.db.add_desk("test_card1")
        self.db.add_desk("test_card2")
        self.db.add_desk("test_card3")

        self.db.rename_desk(1, "test_card_new")

        result = self.db.get_desk_by_id(1)
        self.assertEqual(result[0][1], "test_card_new")


if __name__ == '__main__':
    unittest.main()

