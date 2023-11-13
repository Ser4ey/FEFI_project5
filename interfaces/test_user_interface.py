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

    # def test_some_exception(self):
    #     with self.assertRaises(UserInterfaceExceptions.InvalidDeskIdType):
    #         self.UserInterface.get_deck_by_desk_id('not int')


if __name__ == '__main__':
    unittest.main()

