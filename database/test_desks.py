import os
import unittest

from database.desks import DesksDB


class TestCardsDB(unittest.TestCase):
    def setUp(self):
        self.db = DesksDB('test.db')

        self.db.execute('''
            CREATE TABLE IF NOT EXISTS Columns(
                id integer PRIMARY KEY AUTOINCREMENT,
                desk_id integer,
                name text,
                sequence_number integer,
                FOREIGN KEY (desk_id) REFERENCES Desks(id),
                unique (desk_id, name)
        );
        ''', commit=True)

        self.db.execute('''
            CREATE TABLE IF NOT EXISTS Cards (
            id integer PRIMARY KEY AUTOINCREMENT,
            column_id integer,
            title text,
            text text,
            status integer,
            sequence_number integer,
            FOREIGN KEY (column_id) REFERENCES Columns(id)
        );
        ''', commit=True)

    def tearDown(self):
        self.db.connection.close()
        if os.path.exists('test.db'):
            os.remove('test.db')
        else:
            print("The file does not exist")

    def test_create_table_of_desks(self):
        self.db.create_table_of_desks()
        result = self.db.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Desks'", fetchone=True)

        self.assertEqual(result[0], 'Desks')


    def test_add_desk(self):
        self.db.add_desk("test_desk1")

        result = self.db.select_all_desks()
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0][0], 1)
        self.assertEqual(result[0][1], "test_desk1")


    def test_select_desk(self):
        self.db.add_desk("test_desk_1")
        self.db.add_desk("test_desk_2")
        self.db.add_desk("test_desk_3")

        result1 = self.db.select_desk(id=4)
        self.assertEqual(result1, [])

        result2 = self.db.select_desk(id=1)
        self.assertEqual(result2[0][1], "test_desk_1")


    def test_count_desks(self):
        self.db.add_desk("test_desk_1")
        self.db.add_desk("test_desk_2")
        self.db.add_desk("test_desk_3")

        result = self.db.count_desks()
        self.assertEqual(result, 3)


    def test_update_any_info_about_desk(self):
        self.db.add_desk("test_desk_1")
        self.db.add_desk("test_desk_2")

        self.db.update_any_info_about_desk(1, "name", "test_desk_new")

        result = self.db.select_desk(id=1)
        self.assertEqual(result[0][1], "test_desk_new")


    def test_del_desk(self):
        self.db.add_desk("test_desk_1")
        self.db.add_desk("test_desk_2")

        self.db.execute("INSERT INTO Columns (desk_id, name, sequence_number) VALUES  (?, ?, ?)", (1, 'column_1', 1), (2, 'column_2', 1), commit=True)

        self.db.execute("INSERT INTO Cards (column_id, title, sequence_number) VALUES (?, ?, ?)", (1, 'card_1', 1), (2, 'card_2', 1), commit=True)


        self.db.del_desk(1)
        result = self.db.select_all_desks()
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0][1], "test_desk_2")



if __name__ == '__main__':
    unittest.main()

