import sqlite3
import data.config

class ColumnsDB:
    def __init__(self, path_to_db=data.config.path_to_db):
        self.path_to_db = path_to_db
        self.create_table_of_columns()

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

    def create_table_of_columns(self):
        sql = '''
            CREATE TABLE IF NOT EXISTS Columns(
                id integer PRIMARY KEY AUTOINCREMENT,
                desk_id integer,
                name text,
                sequence_number integer,
                FOREIGN KEY (desk_id) REFERENCES Desks(id),
                unique (desk_id, name)
        );
        '''
        self.execute(sql, commit=True)

    def add_column(self, desk_id, name, sequence_number):
        sql = "INSERT INTO Columns(desk_id, name, sequence_number) VALUES(?, ?, ?)"
        parameters = (desk_id, name, sequence_number)
        self.execute(sql, parameters=parameters, commit=True)
        return True


    def select_all_columns(self):
        sql = 'SELECT * FROM Columns'
        return self.execute(sql, fetchall=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        # используется для создания sql команды с нужными параметрами для команды ниже
        sql += ' AND '.join([
            f"{item} = ?" for item in parameters.keys()
        ])
        return sql, tuple(parameters.values())

    def select_column(self, **kwargs):
        sql = 'SELECT * FROM Columns WHERE '
        sql, parameters = self.format_args(sql, kwargs)
        return self.execute(sql, parameters, fetchone=True)
        # пример использования команды select_desk(id=131, name='JoJo')

    def count_columns(self):
        # return int(self.execute("SELECT COUNT(*) FROM Columns;", fetchone=True))
        return self.execute("SELECT COUNT(*) FROM Columns;", fetchone=True)[0]

    def update_any_info_about_column(self, column_id, thing_to_change, new_data):  # TODO
        result = self.select_column(id=column_id)
        if not result:
            return f'Колонки {column_id} не существует, проверьте правильность id'

        sql = f"UPDATE Columns SET {thing_to_change}=? WHERE id=?"
        self.execute(sql, parameters=(new_data, column_id), commit=True)
        return


columns_test = ColumnsDB()
# columns_test.create_table_of_columns()
# columns_test.add_column('test3', 2)
# print(columns_test.select_column(id=2, name='test2'))
# print(columns_test.count_columns())
# print(columns_test.update_any_info_about_column(1, 'name', 'test!'))