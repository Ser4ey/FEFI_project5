import os
import unittest

from database.cards_api import CardsAPI


class TestCardsAPI(unittest.TestCase):
    def setUp(self):
        self.db = CardsAPI('test.db')


    def tearDown(self):
        if os.path.exists('test.db'):
            os.remove('test.db')
        else:
            print("The file does not exist")


    def test_get_cards(self):
        self.db.add_card(1, "test_card1")
        self.db.add_card(1, "test_card2")
        self.db.add_card(2, "test_card3")

        result = self.db.get_cards()
        self.assertEqual(len(result), 3)


    def test_get_cards_by_column_id(self):
        self.db.add_card(1, "test_card1")
        self.db.add_card(1, "test_card2")
        self.db.add_card(2, "test_card3")
        self.db.add_card(2, "test_card4")

        result = self.db.get_cards_by_column_id(1)
        self.assertEqual(len(result), 2)

        result = self.db.get_cards_by_column_id(3)
        self.assertEqual(len(result), 0)



    def test_add_card(self):
        self.db.add_card(1, "test_card1")
        self.db.add_card(1, "test_card2")
        self.db.add_card(2, "test_card3")

        result = self.db.get_cards_by_column_id(1)
        self.assertEqual(len(result), 2)

        result = self.db.get_cards_by_column_id(2)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0][2], "test_card3")


    def test_del_card(self):
        self.db.add_card(1, "test_card1")
        self.db.add_card(1, "test_card2")
        self.db.add_card(2, "test_card3")

        self.db.del_card(1)
        result = self.db.get_cards()

        self.assertEqual(len(result), 2)
        self.assertEqual(result[0][2], "test_card2")


    def test_change_card_info(self):
        self.db.add_card(1, "test_card1")
        self.db.add_card(2, "test_card2")

        self.db.change_card_info(1, "card1", "text1", 1)
        result = self.db.get_cards_by_column_id(1)
        self.assertEqual(result[0][3], "text1")


    def test_change_card_sequence_number(self):
        self.db.add_card(1, "test_card1")
        self.db.add_card(1, "test_card2")
        self.db.add_card(1, "test_card3")
        self.db.add_card(1, "test_card4")
        self.db.add_card(1, "test_card5")

        self.db.change_card_sequence_number(3, 5)

        result = self.db.get_cards()

        self.assertEqual(result[2][-1], 5)
        self.assertEqual(result[3][-1], 3)
        self.assertEqual(result[4][-1], 4)


    def test_get_card_by_card_id(self):
        self.db.add_card(1, "test_card1")
        self.db.add_card(1, "test_card2")
        self.db.add_card(1, "test_card3")

        result1 = self.db.get_card_by_card_id(4)
        self.assertIsNone(result1)

        result2 = self.db.get_card_by_card_id(2)
        self.assertEqual(result2[2], "test_card2")


if __name__ == '__main__':
    unittest.main()

