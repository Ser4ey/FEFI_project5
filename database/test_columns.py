import os
import unittest

from database.columns import ColumnsDB


class TestCardsDB(unittest.TestCase):
    def setUp(self):
        self.db = ColumnsDB('test.db')
        self.db.execute('''
            CREATE TABLE IF NOT EXISTS Cards(
                id integer PRIMARY KEY AUTOINCREMENT,
                column_id integer,
                card_data text,
                FOREIGN KEY (column_id) REFERENCES Columns(id)
            );
        ''', commit=True)


    def tearDown(self):
        self.db.connection.close()
        if os.path.exists('test.db'):
            os.remove('test.db')
        else:
            print("The file does not exist")


    def test_create_table_of_columns(self):
        self.db.create_table_of_columns()

        result = self.db.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Columns'", fetchone=True)

        self.assertEqual(result[0], 'Columns')


    def test_add_column(self):
        self.db.add_column(1, "test_column1", 1)

        result = self.db.select_all_columns()

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0][1], 1)
        self.assertEqual(result[0][2], "test_column1")
        self.assertEqual(result[0][-1], 1)


    def test_select_all_columns(self):
        self.db.add_column(1, "test_column1", 1)
        self.db.add_column(1, "test_column2", 2)
        self.db.add_column(2, "test_column3", 1)

        result = self.db.select_all_columns()

        self.assertEqual(len(result), 3)

        self.assertEqual(result[0][1], 1)
        self.assertEqual(result[0][2], "test_column1")
        self.assertEqual(result[0][-1], 1)

        self.assertEqual(result[1][1], 1)
        self.assertEqual(result[1][2], "test_column2")
        self.assertEqual(result[1][-1], 2)

        self.assertEqual(result[2][1], 2)
        self.assertEqual(result[2][2], "test_column3")
        self.assertEqual(result[2][-1], 1)


    def test_select_column(self):
        self.db.add_column(1, "test_column1", 1)
        self.db.add_column(1, "test_column2", 2)
        self.db.add_column(2, "test_column3", 1)

        result1 = self.db.select_column(desk_id=3)
        self.assertIsNone(result1)

        result2 = self.db.select_column(name="test_column1")
        self.assertEqual(result2[2], "test_column1")


    def test_select_columns_by_desk_id(self):
        self.db.add_column(1, "test_column1", 1)
        self.db.add_column(1, "test_column2", 2)
        self.db.add_column(2, "test_column3", 1)

        result1 = self.db.select_columns_by_desk_id(3)
        self.assertEqual(result1, [])

        result2 = self.db.select_columns_by_desk_id(1)
        self.assertEqual(len(result2), 2)
        self.assertEqual(result2[0][2], "test_column1")


    def test_count_columns(self):
        result1 = self.db.count_columns()
        self.assertEqual(result1, 0)

        self.db.add_column(1, "test_column1", 1)
        self.db.add_column(1, "test_column2", 2)
        self.db.add_column(2, "test_column3", 1)

        result2 = self.db.count_columns()
        self.assertEqual(result2, 3)


    def test_update_any_info_about_column(self):
        self.db.add_column(1, "test_column1", 1)
        self.db.add_column(1, "test_column2", 2)
        self.db.add_column(2, "test_column3", 1)

        self.db.update_any_info_about_column(1, "name", "test_column_new")

        result = self.db.select_column(name="test_column_new")
        self.assertEqual(result[1], 1)
        self.assertEqual(result[2], "test_column_new")
        self.assertEqual(result[-1], 1)


    def test_get_last_sequence_number_by_desk_id(self):
        self.db.add_column(1, "test_column1", 1)
        self.db.add_column(1, "test_column2", 2)
        self.db.add_column(2, "test_column3", 1)

        result1 = self.db.get_last_sequence_number_by_desk_id(3)
        self.assertIsNone(result1)

        result2 = self.db.get_last_sequence_number_by_desk_id(1)
        self.assertEqual(result2, 2)


    def test_del_column_by_column_id(self):
        self.db.add_column(1, "test_column1", 1)
        self.db.execute("INSERT INTO Cards (column_id, card_data) VALUES (?, ?)", (1, "test_card_data"), commit=True)

        result = self.db.del_column_by_column_id(1)
        self.assertEqual(result, True)


    def test_change_column_sequence_number(self):
        self.db.add_column(1, "test_column1", 1)
        self.db.add_column(1, "test_column2", 2)
        self.db.add_column(1, "test_column3", 3)
        self.db.add_column(1, "test_column4", 4)
        self.db.add_column(1, "test_column5", 5)

        self.db.change_column_sequence_number(3, 5)

        column3 = self.db.select_column(id=3)
        column4 = self.db.select_column(id=4)
        column5 = self.db.select_column(id=5)

        self.assertEqual(column3[-1], 5)
        self.assertEqual(column4[-1], 3)
        self.assertEqual(column5[-1], 4)


    def test_select_column_by_column_id(self):
        self.db.add_column(1, "test_column1", 1)
        self.db.add_column(1, "test_column2", 2)
        self.db.add_column(2, "test_column3", 1)

        result1 = self.db.select_column_by_column_id(4)
        self.assertIsNone(result1)

        result2 = self.db.select_column_by_column_id(1)
        self.assertEqual(result2[0], 1)


if __name__ == '__main__':
    unittest.main()

