import os
import unittest

from database.columns_api import ColumnsAPI
from database.cards_api import CardsAPI


class TestColumnsAPI(unittest.TestCase):
    def setUp(self):
        self.db = ColumnsAPI('test.db')
        self.cards_db = CardsAPI('test.db')

    def tearDown(self):
        if os.path.exists('test.db'):
            os.remove('test.db')
        else:
            print("The file does not exist")


    def test_get_columns(self):
        self.db.add_column(1, "test_column_1")
        self.db.add_column(1, "test_column_2")
        self.db.add_column(2, "test_column_3")

        result = self.db.get_columns()
        self.assertEqual(len(result), 3)
        self.assertEqual(result[0][2], "test_column_1")


    def test_get_columns_by_desk_id(self):
        self.db.add_column(1, "test_column_1")
        self.db.add_column(1, "test_column_2")
        self.db.add_column(2, "test_column_3")

        result1 = self.db.get_columns_by_desk_id(3)
        self.assertEqual(result1, [])

        result2 = self.db.get_columns_by_desk_id(1)
        self.assertEqual(len(result2), 2)
        self.assertEqual(result2[0][2], "test_column_1")


    def test_add_column(self):
        self.db.add_column(1, "test_column_1")
        self.db.add_column(1, "test_column_2")
        self.db.add_column(2, "test_column_3")

        result1 = self.db.get_columns_by_desk_id(1)
        self.assertEqual(len(result1), 2)
        self.assertEqual(result1[0][2], "test_column_1")

        result2 = self.db.get_columns_by_desk_id(2)
        self.assertEqual(len(result2), 1)
        self.assertEqual(result2[0][2], "test_column_3")


    def test_del_column(self):
        self.db.add_column(1, "test_column_1")

        self.cards_db.add_card(1, "test_card_data")
        # self.db.column_db.execute("INSERT INTO Cards (column_id, card_data) VALUES (?, ?)", (1, "test_card_data"), commit=True)

        self.db.del_column(1)
        result = self.db.get_columns()
        self.assertEqual(len(result), 0)

        result = self.cards_db.get_cards_by_column_id(1)
        self.assertEqual(len(result), 0)


    def test_rename_column(self):
        self.db.add_column(1, "test_column_1")
        self.db.add_column(1, "test_column_2")

        result = self.db.get_columns_by_desk_id(1)

        self.db.rename_column(1, "test_column_new")
        result = self.db.get_columns_by_column_id(1)
        self.assertEqual(result[2], "test_column_new")


    def test_change_column_sequence_number(self):
        self.db.add_column(1, "test_column_1")
        self.db.add_column(1, "test_column_2")
        self.db.add_column(1, "test_column_3")
        self.db.add_column(1, "test_column_4")
        self.db.add_column(1, "test_column_5")

        self.db.change_column_sequence_number(3, 5)

        result = self.db.get_columns()

        self.assertEqual(result[2][-1], 5)
        self.assertEqual(result[3][-1], 3)
        self.assertEqual(result[4][-1], 4)


    def test_get_columns_by_column_id(self):
        self.db.add_column(1, "test_column_1")
        self.db.add_column(1, "test_column_2")

        result1 = self.db.get_columns_by_column_id(3)
        self.assertIsNone(result1)

        result2 = self.db.get_columns_by_column_id(2)
        self.assertEqual(result2[2], "test_column_2")


if __name__ == '__main__':
    unittest.main()

