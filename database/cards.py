import sqlite3
import data.config


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
        parameters = (title, column_id, sequence_number)
        self.execute(sql, parameters=parameters, commit=True)
        return True


    def select_all_cards(self):
        sql = 'SELECT * FROM Cards'
        return self.execute(sql, fetchall=True)


    def select_cards_by_column_id(self, column_id):  # TODO
        sql = 'SELECT * FROM Cards WHERE column_id=?'
        return self.execute(sql, (column_id,), fetchall=True)


    def select_card_by_card_id(self, card_id):
        sql = 'SELECT * FROM Cards WHERE id=?'
        return self.execute(sql, (card_id,), fetchone=True)

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

    def update_any_info_about_card(self, card_id, field_to_change, new_data):
        result = self.select_card(id=card_id)
        if not result:
            return f'Карты {card_id} не существует, проверьте правильность id'

        sql = f"UPDATE Cards SET {field_to_change}=? WHERE id=?"
        self.execute(sql, parameters=(new_data, card_id), commit=True)
        return

    def get_last_sequence_number_by_desk_id(self, column_id):
        sql = 'SELECT MAX(sequence_number) FROM Cards WHERE column_id=?'
        result = self.execute(sql, (column_id,), fetchone=True)

        return result[0]


    def del_card_by_card_id(self, card_id):
        zxc = self.select_card(id=card_id)

        if len(zxc) != 0:
            self.execute('DELETE FROM Cards WHERE id=?', (card_id,), commit=True)
            return True
        else:
            return False

    def change_card_sequence_number(self, card_id, new_sequence_number):
        sql = 'SELECT sequence_number FROM Cards WHERE id=?'
        card_sequence_number = self.select_card(id=card_id)[-1]
        card_columnn_id = self.select_card(id=card_id)[1]

        if card_sequence_number < new_sequence_number:
            sql = 'UPDATE Cards SET sequence_number=sequence_number-1 WHERE sequence_number > ? and sequence_number <= ? and column_id=?'
            self.execute(sql, (card_sequence_number, new_sequence_number, card_columnn_id,), commit=True)
            self.update_any_info_about_card(card_id, 'sequence_number', new_sequence_number)
            return True

        elif card_sequence_number > new_sequence_number:
            sql = 'UPDATE Cards SET sequence_number=sequence_number+1 WHERE sequence_number >= ? and sequence_number < ? and column_id=?'
            self.execute(sql, (new_sequence_number, card_sequence_number, card_columnn_id), commit=True)
            self.update_any_info_about_card(card_id, 'sequence_number', new_sequence_number)
            return True

        else:
            return True


