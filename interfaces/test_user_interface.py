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

    def test_del_desk_from_Ser4ey(self):
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

    def test_del_desk2_from_Ser4ey(self):
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

    def test_change_desk_name_from_Ser4ey(self):
        self.UserInterface.DeskAPI.add_desk("new_desk")
        self.UserInterface.add_column_to_desk(1, "column1")

        self.assertEqual(self.UserInterface.get_column_by_column_id(1)['column_name'], 'column1')

        self.UserInterface.change_column_name(1, 'hahaha')

        self.assertEqual(self.UserInterface.get_column_by_column_id(1)['column_name'], 'hahaha')

        self.assertEqual(len(self.UserInterface.ColumnsAPI.get_columns()), 1)

    def test_change_column_position_in_desk_from_Ser4ey(self):
        self.UserInterface.DeskAPI.add_desk("new_desk")
        for i in range(1, 10):
            self.UserInterface.add_column_to_desk(1, f"column{i}")

        self.assertEqual(len(self.UserInterface.get_columns_by_desk_id(1)), 9)

        self.UserInterface.change_column_position_in_desk(1, 2, 8)
        columns = self.UserInterface.get_columns_by_desk_id(1)
        columns.sort(key=lambda x: x['sequence_number'])
        columns = [i['column_id'] for i in columns]
        self.assertEqual(columns, [1, 3, 4, 5, 6, 7, 8, 2, 9])

        self.UserInterface.change_column_position_in_desk(1, 3, 8)
        columns = self.UserInterface.get_columns_by_desk_id(1)
        columns.sort(key=lambda x: x['sequence_number'])
        columns = [i['column_id'] for i in columns]
        self.assertEqual(columns, [1, 4, 5, 6, 7, 8, 2, 3, 9])

        self.UserInterface.change_column_position_in_desk(1, 8, 3)
        columns = self.UserInterface.get_columns_by_desk_id(1)
        columns.sort(key=lambda x: x['sequence_number'])
        columns = [i['column_id'] for i in columns]
        self.assertEqual(columns, [1, 4, 8, 5, 6, 7, 2, 3, 9])

        self.UserInterface.change_column_position_in_desk(1, 9, 1)
        columns = self.UserInterface.get_columns_by_desk_id(1)
        columns.sort(key=lambda x: x['sequence_number'])
        columns = [i['column_id'] for i in columns]
        self.assertEqual(columns, [9, 1, 4, 8, 5, 6, 7, 2, 3])

    def test_move_card_from_Ser4ey(self):
        self.UserInterface.DeskAPI.add_desk("new_desk")
        for i in range(2):
            self.UserInterface.add_column_to_desk(1, f"column{i+1}")

        self.UserInterface.add_card_to_column("card1", 1)
        self.UserInterface.change_card_info(1, card_text='some info about')
        self.assertIsNotNone(self.UserInterface.get_card_by_card_id(1))
        self.assertEqual(self.UserInterface.get_card_by_card_id(1)['card_text'], 'some info about')

        self.UserInterface.add_card_to_column("card2", 2)
        self.UserInterface.add_card_to_column("card3", 2)
        self.UserInterface.add_card_to_column("card4", 2)

        self.assertEqual(len(self.UserInterface.CardsAPI.get_cards_by_column_id(1)), 1)
        self.assertEqual(len(self.UserInterface.CardsAPI.get_cards_by_column_id(2)), 3)
        self.UserInterface.move_card(1, 2, 1)
        self.assertEqual(len(self.UserInterface.CardsAPI.get_cards_by_column_id(1)), 0)
        self.assertEqual(len(self.UserInterface.CardsAPI.get_cards_by_column_id(2)), 4)

        self.assertIsNotNone(self.UserInterface.get_card_by_card_id(1))
        self.assertEqual(self.UserInterface.get_card_by_card_id(1)['card_text'], 'some info about')

        cards = self.UserInterface.get_cards_by_column_id(2)
        cards.sort(key=lambda x: x['sequence_number'])
        cards = [i["card_id"] for i in cards]
        self.assertEqual(cards, [1, 2, 3, 4])

        self.UserInterface.change_card_info(card_id=3, card_status=1)
        self.UserInterface.move_card(3, 1, 1)
        self.assertEqual(len(self.UserInterface.CardsAPI.get_cards_by_column_id(1)), 1)
        self.assertEqual(len(self.UserInterface.CardsAPI.get_cards_by_column_id(2)), 3)

        column1 = self.UserInterface.get_cards_by_column_id(1)
        column2 = self.UserInterface.get_cards_by_column_id(2)

        self.assertEqual(column1[0]['sequence_number'], 1)
        self.assertEqual(column1[0]['card_id'], 3)

        self.assertEqual(self.UserInterface.get_card_by_card_id(4)['sequence_number'], 3)

        self.assertEqual(self.UserInterface.get_card_by_card_id(3)['card_status'], 1)


    def test_get_desks(self):
        result1 = self.UserInterface.get_desks()
        self.assertEqual(len(result1), 0)

        self.UserInterface.DeskAPI.add_desk("test_desk1")
        self.UserInterface.DeskAPI.add_desk("test_desk2")
        self.UserInterface.DeskAPI.add_desk("test_desk3")

        result2 = self.UserInterface.get_desks()
        self.assertEqual(len(result2), 3)


    def test_get_desk_by_desk_id(self):
        self.UserInterface.DeskAPI.add_desk("test_desk1")
        self.UserInterface.DeskAPI.add_desk("test_desk2")

        result1 = self.UserInterface.get_desk_by_desk_id(0)
        self.assertIsNone(result1)

        result2 = self.UserInterface.get_desk_by_desk_id(1)
        self.assertEqual(result2['desk_id'], 1)

        with self.assertRaises(UserInterfaceExceptions.InvalidDeskIdType):
            self.UserInterface.get_desk_by_desk_id("!!!")


    def test_create_desk(self):
        self.UserInterface.create_desk("test_desk1")

        result1 = self.UserInterface.get_desk_by_desk_id(1)
        self.assertEqual(result1['desk_id'], 1)

        with self.assertRaises(UserInterfaceExceptions.InvalidDeskNameType):
            self.UserInterface.create_desk(123)

        with self.assertRaises(UserInterfaceExceptions.InvalidDeskNameContent):
            self.UserInterface.create_desk(" ")


    def test_get_columns_by_desk_id(self):
        self.UserInterface.create_desk("test_desk1")
        self.UserInterface.add_column_to_desk(1, "test_column1")

        result1 = self.UserInterface.get_columns_by_desk_id(1)
        self.assertEqual(result1[0]['desk_id'], 1)

        with self.assertRaises(UserInterfaceExceptions.InvalidDeskIdType):
            self.UserInterface.get_columns_by_desk_id("!!!")

        with self.assertRaises(UserInterfaceExceptions.DeskNotExist):
            self.UserInterface.get_columns_by_desk_id(2)


    def test_get_column_by_column_id(self):
        self.UserInterface.create_desk("test_desk1")
        self.UserInterface.add_column_to_desk(1, "test_column1")

        result1 = self.UserInterface.get_column_by_column_id(1)
        self.assertEqual(result1['column_id'], 1)

        with self.assertRaises(UserInterfaceExceptions.InvalidColumnIdType):
            self.UserInterface.get_column_by_column_id("!!!")


    def test_change_column_name(self):
        self.UserInterface.create_desk("test_desk1")
        self.UserInterface.add_column_to_desk(1, "test_column1")

        self.UserInterface.change_column_name(1, "test_desk1_new")
        result1 = self.UserInterface.get_column_by_column_id(1)
        self.assertEqual(result1['column_name'], "test_desk1_new")

        with self.assertRaises(UserInterfaceExceptions.InvalidColumnIdType):
            self.UserInterface.change_column_name('!!!', "test_desk1_new")

        with self.assertRaises(UserInterfaceExceptions.InvalidColumnNameContent):
            self.UserInterface.change_column_name(1, 000)

        with self.assertRaises(UserInterfaceExceptions.InvalidColumnNameContent):
            self.UserInterface.change_column_name(1, "   ")

        with self.assertRaises(UserInterfaceExceptions.ColumnNotExist):
            self.UserInterface.change_column_name(3, "test_desk1_new")


    def test_del_column(self):
        self.UserInterface.create_desk("test_desk1")
        self.UserInterface.add_column_to_desk(1, "test_column1")
        self.UserInterface.add_card_to_column("test_card1", 1)
        self.UserInterface.add_card_to_column("test_card2", 1)

        self.UserInterface.del_column(1)
        result1 = self.UserInterface.get_column_by_column_id(1)
        self.assertIsNone(result1)
        with self.assertRaises(UserInterfaceExceptions.ColumnNotExist):
            self.UserInterface.get_cards_by_column_id(1)

        with self.assertRaises(UserInterfaceExceptions.InvalidColumnIdType):
            self.UserInterface.del_column("!!!")

        with self.assertRaises( UserInterfaceExceptions.ColumnNotExist):
            self.UserInterface.del_column(3)


    def test_add_column_to_desk(self):
        self.UserInterface.create_desk("test_desk1")
        self.UserInterface.add_column_to_desk(1, "test_column1")

        result1 = self.UserInterface.get_column_by_column_id(1)
        self.assertEqual(result1['column_id'], 1)

        with self.assertRaises(UserInterfaceExceptions.InvalidDeskIdType):
            self.UserInterface.add_column_to_desk("!!!", "test_column1")

        with self.assertRaises(UserInterfaceExceptions.InvalidColumnNameContent):
            self.UserInterface.add_column_to_desk(1, 000)

        with self.assertRaises(UserInterfaceExceptions.InvalidColumnNameContent):
            self.UserInterface.add_column_to_desk(1, "   ")

        with self.assertRaises(UserInterfaceExceptions.DeskNotExist):
            self.UserInterface.add_column_to_desk(2, "test_column1")


    def test_get_cards_by_column_id(self):
        self.UserInterface.create_desk("test_desk1")
        self.UserInterface.add_column_to_desk(1, "test_column1")
        self.UserInterface.add_card_to_column("test_card1", 1)
        self.UserInterface.add_card_to_column("test_card2", 1)

        result1 = self.UserInterface.get_cards_by_column_id(1)
        self.assertEqual(len(result1), 2)
        self.assertEqual(result1[0]['column_id'], 1)

        with self.assertRaises(UserInterfaceExceptions.InvalidColumnIdType):
            self.UserInterface.get_cards_by_column_id("!!!")

        with self.assertRaises(UserInterfaceExceptions.ColumnNotExist):
            self.UserInterface.get_cards_by_column_id(2)


    def test_add_card_to_column(self):
        self.UserInterface.create_desk("test_desk1")
        self.UserInterface.add_column_to_desk(1, "test_column1")
        self.UserInterface.add_card_to_column("test_card1", 1)
        self.UserInterface.add_card_to_column("test_card2", 1)

        result1 = self.UserInterface.get_cards_by_column_id(1)
        self.assertEqual(len(result1), 2)
        self.assertEqual(result1[1]['column_id'], 1)

        with self.assertRaises(UserInterfaceExceptions.InvalidColumnIdType):
            self.UserInterface.add_card_to_column("test_card2", "!!!")

        with self.assertRaises(UserInterfaceExceptions.ColumnNotExist):
            self.UserInterface.add_card_to_column("test_card2", 2)

        with self.assertRaises(UserInterfaceExceptions.InvalidCardTitleType):
            self.UserInterface.add_card_to_column(000, 1)

        with self.assertRaises(UserInterfaceExceptions.InvalidCardTitleContent):
            self.UserInterface.add_card_to_column("   ", 1)


    def test_get_card_by_card_id(self):
        self.UserInterface.create_desk("test_desk1")
        self.UserInterface.add_column_to_desk(1, "test_column1")
        self.UserInterface.add_card_to_column("test_card1", 1)

        result1 = self.UserInterface.get_card_by_card_id(1)
        self.assertEqual(result1['card_id'], 1)

        with self.assertRaises(UserInterfaceExceptions.InvalidCardIdType):
            self.UserInterface.get_card_by_card_id("!!!")


    def test_change_card_info(self):
        self.UserInterface.create_desk("test_desk1")
        self.UserInterface.add_column_to_desk(1, "test_column1")
        self.UserInterface.add_card_to_column("test_card1", 1)


        self.UserInterface.change_card_info(card_id=1, card_title="test_card1_new", card_text="card_text_new", card_status=1)
        result1 = self.UserInterface.get_card_by_card_id(1)
        self.assertEqual(result1['card_title'], "test_card1_new")
        self.assertEqual(result1['card_text'], "card_text_new")
        self.assertEqual(result1['card_status'], 1)

        with self.assertRaises(UserInterfaceExceptions.InvalidCardIdType):
            self.UserInterface.change_card_info(card_id="!!!")

        with self.assertRaises(UserInterfaceExceptions.CardNotExist):
            self.UserInterface.change_card_info(card_id=2)

        with self.assertRaises(UserInterfaceExceptions.InvalidCardTitleType):
            self.UserInterface.change_card_info(card_id=1, card_title=111)

        with self.assertRaises(UserInterfaceExceptions.InvalidCardTitleContent):
            self.UserInterface.change_card_info(card_id=1, card_title="  ")

        with self.assertRaises(UserInterfaceExceptions.InvalidCardTextType):
            self.UserInterface.change_card_info(card_id=1, card_text=111)

        with self.assertRaises(UserInterfaceExceptions.InvalidCardStatusType):
            self.UserInterface.change_card_info(card_id=1, card_status="!!!")


    def test_del_card(self):
        self.UserInterface.create_desk("test_desk1")
        self.UserInterface.add_column_to_desk(1, "test_column1")
        self.UserInterface.add_card_to_column("test_card1", 1)

        self.UserInterface.del_card(1)

        result1 = self.UserInterface.get_card_by_card_id(1)
        self.assertIsNone(result1)


if __name__ == '__main__':
    unittest.main()

