import os
import unittest

from interfaces import AppInterface
from interfaces.exceptions import UserInterfaceExceptions
from database import DeskAPI, ColumnsAPI, CardsAPI


# TODO: Gleb
class TestUserInterface(unittest.TestCase):
    def setUp(self):
        self.UserInterface = AppInterface.UserInterface
        self.UserInterface.DeskAPI = DeskAPI('test.db')
        self.UserInterface.ColumnsAPI = ColumnsAPI('test.db')
        self.UserInterface.CardsAPI = CardsAPI('test.db')

    def tearDown(self):
        if os.path.exists('test.db'):
            os.remove('test.db')
        else:
            print("The file does not exist")

    def test_some(self):
        self.assertFalse(2 == 3)
        self.assertTrue(2+3 > 1)

    def test_del_desk(self):
        self.UserInterface.DeskAPI.add_desk("new_desk")

        desk = self.UserInterface.get_desk_by_desk_id(1)
        self.assertIsNotNone(desk)

        self.UserInterface.add_column_to_desk(1, "column1")
        self.UserInterface.add_column_to_desk(1, "column2")

        self.assertEqual(len(self.UserInterface.get_columns_by_desk_id(1)), 2)
        self.UserInterface.del_desk(1)

        with self.assertRaises(UserInterfaceExceptions.DeskNotExist):
            self.UserInterface.get_columns_by_desk_id(1)

        columns = self.UserInterface.ColumnsAPI.get_columns_by_desk_id(1)
        self.assertEqual(len(columns), 0)

    def test_del_desk2(self):
        self.UserInterface.DeskAPI.add_desk("new_desk")
        self.UserInterface.add_column_to_desk(1, "column1")

        self.assertEqual(len(self.UserInterface.get_columns_by_desk_id(1)), 1)
        self.UserInterface.add_card_to_column("new_card", 1)
        self.assertEqual(len(self.UserInterface.get_cards_by_column_id(1)), 1)

        self.UserInterface.del_desk(1)
        with self.assertRaises(UserInterfaceExceptions.DeskNotExist):
            self.UserInterface.get_columns_by_desk_id(1)
        with self.assertRaises(UserInterfaceExceptions.ColumnNotExist):
            self.UserInterface.get_cards_by_column_id(1)

        columns = self.UserInterface.ColumnsAPI.get_columns_by_desk_id(1)
        self.assertEqual(len(columns), 0)

        cards = self.UserInterface.CardsAPI.get_cards_by_column_id(1)
        self.assertEqual(len(cards), 0)



        columns = self.UserInterface.ColumnsAPI.get_columns_by_desk_id(1)
        self.assertEqual(len(columns), 0)

if __name__ == '__main__':
    unittest.main()

