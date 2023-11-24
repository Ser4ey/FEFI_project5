import os
import unittest

from database.desk_api import DeskAPI
from database.columns_api import ColumnsAPI
from database.cards_api import CardsAPI


class TestCardsAPI(unittest.TestCase):
    def setUp(self):
        self.db = DeskAPI('test.db')
        self.columns_db = ColumnsAPI('test.db')
        self.cards_db = CardsAPI('test.db')

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

    def test_del_desk_from_Ser4ey(self):
        self.db.add_desk("test_card1")
        self.db.add_desk("test_card2")
        self.db.add_desk("test_card3")

        self.columns_db.add_column(1, "column1")
        self.columns_db.add_column(1, "column2")
        self.assertEqual(len(self.columns_db.column_db.select_all_columns()), 2)

        self.cards_db.add_card(1, "card1")
        self.cards_db.add_card(1, "card2")
        self.cards_db.add_card(2, "card3")
        self.assertEqual(len(self.cards_db.card_db.select_all_cards()), 3)

        self.db.del_desk_by_id(2)
        self.db.del_desk_by_id(3)
        self.db.del_desk_by_id(1)

        self.assertEqual(len(self.columns_db.column_db.select_all_columns()), 0)
        self.assertEqual(len(self.cards_db.card_db.select_all_cards()), 0)
        self.assertEqual(len(self.db.desk_db.select_all_desks()), 0)


if __name__ == '__main__':
    unittest.main()

