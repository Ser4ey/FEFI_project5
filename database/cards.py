import sqlite3
import data.config
# import FEFI_project5.data.config

class CardsDB:
    def __init__(self, path_to_db=data.config.path_to_db):
        self.path_to_db = path_to_db
        self.create_table_of_cards()

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = tuple()

        connection = self.connection
        # connection.set_trace_callback(logger)
        cursor = connection.cursor()
        cursor.execute(sql, parameters)
        data = None

        if commit:
            connection.commit()
        if fetchone:
            data = cursor.fetchone()
        if fetchall:
            data = cursor.fetchall()
        connection.close()

        return data

    def create_table_of_cards(self):
        sql = '''
            CREATE TABLE IF NOT EXISTS Cards (
            id integer PRIMARY KEY AUTOINCREMENT,
            column_id integer,
            title text,
            text text,
            status integer,
            sequence_number integer,
            FOREIGN KEY (column_id) REFERENCES Columns(id)
        );
        '''
        self.execute(sql, commit=True)

    def add_card(self, title, column_id, sequence_number):
        sql = "INSERT INTO Cards(title, column_id, sequence_number) VALUES(?, ?, ?)"
        parameters = (title,column_id, sequence_number)
        self.execute(sql, parameters=parameters, commit=True)
        return True


    def select_all_cards(self):
        sql = 'SELECT * FROM Cards'
        return self.execute(sql, fetchall=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        # используется для создания sql команды с нужными параметрами для команды ниже
        sql += ' AND '.join([
            f"{item} = ?" for item in parameters.keys()
        ])
        return sql, tuple(parameters.values())

    def select_card(self, **kwargs):
        sql = 'SELECT * FROM Cards WHERE '
        sql, parameters = self.format_args(sql, kwargs)
        return self.execute(sql, parameters, fetchone=True)
        # пример использования команды select_desk(id=131, name='JoJo')

    def select_cards(self, **kwargs):
        sql = 'SELECT * FROM Cards WHERE '
        sql, parameters = self.format_args(sql, kwargs)
        return self.execute(sql, parameters, fetchall=True)
        # пример использования команды select_desk(id=131, name='JoJo')

    def count_cards(self):
        # return int(self.execute("SELECT COUNT(*) FROM Columns;", fetchone=True))
        return self.execute("SELECT COUNT(*) FROM Cards;", fetchone=True)[0]

    def update_any_info_about_card(self, card_id, field_to_change, new_data):  # TODO
        result = self.select_card(id=card_id)
        if not result:
            return f'Карты {card_id} не существует, проверьте правильность id'

        sql = f"UPDATE Cards SET {field_to_change}=? WHERE id=?"
        self.execute(sql, parameters=(new_data, card_id), commit=True)
        return
        # функция удаления (нужно написать удаление по id)

# a = CardsDB()
# a.add_card('1', 99, 8)
# a.add_card('1', 2, 99)
# a.add_card('1', 2, 77)
#
# print(a.select_cards(column_id=99))