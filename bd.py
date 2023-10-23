import sqlite3
import data.config


class DesksDB:
    '''Низкоуровневый класс для работы с бд Desks (росто ф)'''
    def __init__(self, path_to_db=data.config.path_to_db):
        self.path_to_db = path_to_db
        self.create_table_of_desks()

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

    def create_table_of_desks(self):
        sql = """
            CREATE TABLE IF NOT EXISTS Desks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name varchar,
                sequence_number integer,
            );
            """
        self.execute(sql, commit=True)

    def add_desk(self, name, sequence_number):
        sql = "INSERT INTO Desks(name, sequence_number) VALUES(?, ?)"
        parameters = (name, sequence_number)
        self.execute(sql, parameters=parameters, commit=True)
        return True

    def select_all_desks(self):
        sql = 'SELECT * FROM Desks'
        return self.execute(sql, fetchall=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        # используется для создания sql команды с нужными параметрами для команды ниже
        sql += ' AND '.join([
            f"{item} = ?" for item in parameters.keys()
        ])
        return sql, tuple(parameters.values())

    def select_desk(self, **kwargs):
        sql = 'SELECT * FROM Desks WHERE '
        sql, parameters = self.format_args(sql, kwargs)
        return self.execute(sql, parameters, fetchone=True)
        # пример использования команды select_desk(id=131, name='JoJo')

    def select_desks(self, **kwargs):
        '''Получаем все доски по условию'''
        sql = 'SELECT * FROM Desks WHERE '
        sql, parameters = self.format_args(sql, kwargs)
        return self.execute(sql, parameters, fetchall=True)
        # пример использования команды select_desk(id=131, name='JoJo')

    def count_desks(self):
        return int(self.execute("SELECT COUNT(*) FROM Desks;", fetchone=True))

    def update_any_info_about_desk(self, desk_id, thing_to_change, new_data):
        result = self.select_desk(desk_id=desk_id)
        if not result:
            return f'Доски {desk_id} не существует, проверьте правильность id'

        sql = f"UPDATE Desks SET {thing_to_change}=? WHERE id=?"
        self.execute(sql, parameters=(new_data, desk_id), commit=True)
        return

    # функция удаления (нужно написать удаление по id)


class ColumnsDB:
    '''CREATE TABLE Columns (
	id integer PRIMARY KEY AUTOINCREMENT,
	desk_id integer,
	name text,
	sequence_number integer
    );
    '''
    pass


class CardsDB:
    '''
    CREATE TABLE Cards (
	id integer PRIMARY KEY AUTOINCREMENT,
	column_id integer,
	title text,
	text text,
	status integer,
	sequence_number integer
);
    '''


class DeskDBAPI:
    def __init__(self):
        self.desk_db = DesksDB()

        self.number_of_desks = self.desk_db.count_desks() # текущее количество досок

    def get_desks(self):
        return [('desk_id1', 'desk_name1', 'sequence_number1'), ('desk_id2', 'desk_name2', 'sequence_number2')]

    def get_desk_by_id(self, desk_id):
        return ('desk_id', 'desk_name', 'sequence_number')

    def add_desk(self, desk_name):
        '''Добавляем доску (в конец)
           Проверка на уникальное имя
           Важно задать правильный sequence_number '''
        return True # - успех

    def del_desk(self, desk_id):
        '''
        Удаляем доску
        Проверка на наличие
        Нужно поменять sequence_number для всех съхавших досок
        :param desk_id:
        :return:
        '''
        return True # - успех

    def rename_desk(self, desk_id, new_name):
        '''Меняем имя у доски
           Проверка на уникальное имя
           Проверка, что доска существует'''
        return True  # - успех

    def change_desk_sequence_number(self, desk_id, new_sequence_number):
        '''
        Нужно менять номера для всех съехавших досок
        0
        1 (ставим на 3)
        2
        3
        4
        ->
        0 (0)
        2 (1) - номер съхал на 1 вниз
        3 (2) - номер съхал на 1 вниз
        1 (3)
        4 (4)

        0
        1
        2
        3 (ставим на 1)
        4
        ->
        0 (0)
        3 (1) - номер съхал на 1 вверх
        1 (2) - номер съхал на 1 вверх
        2 (3)
        4 (4)

        :param desk_id:
        :param new_sequence_number:
        :return:
        '''


class ColumnsDBAPI:
    def __init__(self):
        self.column_db = ColumnsDB()

    def get_columns(self):
        '''Список всех колонок'''
        return [('column_id', 'desk_id', 'column_name', 'sequence_number'), ()]

    def get_columns_by_desk_id(self, desk_id):
        '''Список всех колонок принадлежащих desk_id'''
        return [('column_id', 'desk_id', 'column_name', 'sequence_number'), ()]

    def add_column(self, desk_id, column_name):
        '''Добавляем колонку (в конец)
           Важно задать правильный sequence_number '''
        return True  # - успех

    def del_column(self, column_id):
        '''
        Удаляем колонку
        Проверка на наличие
        Нужно поменять sequence_number для всех съхавших колонок
        :param desk_id:
        :return:
        '''
        return True  # - успех

    def rename_column(self, column_id, new_name):
        '''Меняем имя у колонки
           Проверка на уникальное имя
           Проверка, что колонка существует'''
        return True  # - успех

    def change_column_sequence_number(self, column_id, new_sequence_number):
        '''
        Нужно менять номера для всех съехавших колонок
        0
        1 (ставим на 3)
        2
        3
        4
        ->
        0 (0)
        2 (1) - номер съхал на 1 вниз
        3 (2) - номер съхал на 1 вниз
        1 (3)
        4 (4)

        0
        1
        2
        3 (ставим на 1)
        4
        ->
        0 (0)
        3 (1) - номер съхал на 1 вверх
        1 (2) - номер съхал на 1 вверх
        2 (3)
        4 (4)

        :param desk_id:
        :param new_sequence_number:
        :return:
        '''


class CardsDBAPI:
    def __init__(self):
        self.card_db = CardsDB()

    def get_cards(self):
        '''Список всех карточек'''
        return [('card_id', 'column_id', 'card_title', 'card_text', 'card_status', 'sequence_number'), ()]

    def get_cards_by_desk_id(self, desk_id):
        '''Список всех карточек принадлежащих desk_id'''
        return [('card_id', 'column_id', 'card_title', 'card_text', 'card_status', 'sequence_number'), ()]

    def get_cards_by_column_id(self, column_id):
        '''Список всех карточек принадлежащих column_id'''
        return [('card_id', 'column_id', 'card_title', 'card_text', 'card_status', 'sequence_number'), ()]

    def add_card(self, column_id, card_name):
        '''Добавляем карточку в колонку (в конец)
           Важно задать правильный sequence_number '''
        return True  # - успех

    def del_card(self, card_id):
        '''
        Удаляем карточку
        Проверка на наличие
        Нужно поменять sequence_number для всех съхавших колонок
        '''
        return True  # - успех

    def chage_card_info(self, card_id, name=None, title=None, text=None, status=None):
        '''
        Проверить на наличие
        Меняем всё что не None'''
        return True  # - успех

    def change_card_sequence_number(self, card_id, new_sequence_number):
        '''
        Нужно менять номера для всех съехавших колонок
        0
        1 (ставим на 3)
        2
        3
        4
        ->
        0 (0)
        2 (1) - номер съхал на 1 вниз
        3 (2) - номер съхал на 1 вниз
        1 (3)
        4 (4)

        0
        1
        2
        3 (ставим на 1)
        4
        ->
        0 (0)
        3 (1) - номер съхал на 1 вверх
        1 (2) - номер съхал на 1 вверх
        2 (3)
        4 (4)

        :param desk_id:
        :param new_sequence_number:
        :return:
        '''
