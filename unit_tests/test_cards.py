import os
import unittest

from database.cards import CardsDB


class TestCardsDB(unittest.TestCase):
    def setUp(self):
        self.db = CardsDB('test.db')


    def tearDown(self):
        self.db.connection.close()
        if os.path.exists('test.db'):
            os.remove('test.db')
        else:
            print("The file does not exist")


    def test_create_table_of_cards(self):
        self.db.create_table_of_cards()
        result = self.db.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Cards'", fetchone=True)

        self.assertEqual(result[0], 'Cards')


    def test_add_card(self):
        self.db.add_card("test_card1", 1, 1)
        result = self.db.select_all_cards()

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0][1], 1)
        self.assertEqual(result[0][2], 'test_card1')
        self.assertEqual(result[0][-1], 1)

    def test_select_all_cards(self):
        self.db.add_card("test_card1", 1, 1)
        self.db.add_card("test_card2", 1, 2)
        self.db.add_card("test_card3", 2, 1)

        result = self.db.select_all_cards()

        self.assertEqual(len(result), 3)

        self.assertEqual(result[0][1], 1)
        self.assertEqual(result[0][2], 'test_card1')
        self.assertEqual(result[0][-1], 1)

        self.assertEqual(result[1][1], 1)
        self.assertEqual(result[1][2], 'test_card2')
        self.assertEqual(result[1][-1], 2)

        self.assertEqual(result[2][1], 2)
        self.assertEqual(result[2][2], 'test_card3')
        self.assertEqual(result[2][-1], 1)


    def test_select_cards_by_column_id(self):
        self.db.add_card("test_card1", 1, 1)
        self.db.add_card("test_card2", 1, 2)
        self.db.add_card("test_card3", 2, 1)

        result = self.db.select_cards_by_column_id(1)

        self.assertEqual(len(result), 2)

        self.assertEqual(result[0][1], 1)
        self.assertEqual(result[0][2], 'test_card1')
        self.assertEqual(result[0][-1], 1)

        self.assertEqual(result[1][1], 1)
        self.assertEqual(result[1][2], 'test_card2')
        self.assertEqual(result[1][-1], 2)


    def test_select_card(self):
        self.db.add_card("test_card1", 1, 1)
        self.db.add_card("test_card2", 1, 2)
        self.db.add_card("test_card3", 2, 1)

        result1 = self.db.select_card(title="test_card4")
        self.assertIsNone(result1)

        result2 = self.db.select_card(title="test_card2")

        self.assertEqual(len(result2), 6)
        self.assertEqual(result2[1], 1)
        self.assertEqual(result2[-1], 2)


    def test_select_cards(self):
        self.db.add_card("test_card1", 1, 1)
        self.db.add_card("test_card2", 1, 2)
        self.db.add_card("test_card3", 2, 1)

        result1 = self.db.select_cards(column_id=3)
        self.assertEqual(len(result1), 0)

        result2 = self.db.select_cards(title="test_card2")
        self.assertEqual(len(result2), 1)
        self.assertEqual(result2[0][1], 1)
        self.assertEqual(result2[0][2], "test_card2")
        self.assertEqual(result2[0][-1], 2)

        result3 = self.db.select_cards(column_id=1)
        self.assertEqual(len(result3), 2)
        self.assertEqual(result3[0][1], 1)
        self.assertEqual(result3[0][2], 'test_card1')
        self.assertEqual(result3[0][-1], 1)


    def test_count_cards(self):
        self.db.add_card("test_card1", 1, 1)
        self.db.add_card("test_card2", 1, 2)
        self.db.add_card("test_card3", 2, 1)

        result = self.db.count_cards()
        self.assertEqual(result, 3)


    def test_update_any_info_about_card(self):
        self.db.add_card("test_card1", 1, 1)
        self.db.add_card("test_card2", 1, 2)
        self.db.add_card("test_card3", 2, 1)

        self.db.update_any_info_about_card(1, "title", "test_card_new")
        result = self.db.select_card(id=1)
        self.assertEqual(result[2], "test_card_new")


    def test_get_last_sequence_number_by_desk_id(self):
        self.db.add_card("test_card1", 1, 1)
        self.db.add_card("test_card2", 1, 2)
        self.db.add_card("test_card3", 2, 1)

        result1 = self.db.get_last_sequence_number_by_desk_id(3)
        self.assertIsNone(result1)

        result2 = self.db.get_last_sequence_number_by_desk_id(1)
        self.assertEqual(result2, 2)


    def test_del_card_by_card_id(self):
        self.db.add_card("test_card1", 1, 1)
        self.db.add_card("test_card2", 1, 2)
        self.db.add_card("test_card3", 2, 1)

        self.db.del_card_by_card_id(1)

        result = self.db.select_card(id=1)
        self.assertIsNone(result)


    def test_change_card_sequence_number(self):
        self.db.add_card("test_card1", 1, 1)
        self.db.add_card("test_card2", 1, 2)
        self.db.add_card("test_card3", 1, 3)
        self.db.add_card("test_card4", 1, 4)
        self.db.add_card("test_card5", 1, 5)

        self.db.change_card_sequence_number(3, 5)
        card3 = self.db.select_card(id=3)
        card4 = self.db.select_card(id=4)
        card5 = self.db.select_card(id=5)

        self.assertEqual(card3[-1], 5)
        self.assertEqual(card4[-1], 3)
        self.assertEqual(card5[-1], 4)


if __name__ == '__main__':
    unittest.main()

