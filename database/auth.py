import sqlite3
import data.config


class AuthDB:
    def __init__(self, path_to_db=data.config.path_to_db):
        self.path_to_db = path_to_db
        self.create_auth_table()

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

    def create_auth_table(self):
        sql = '''
            CREATE TABLE IF NOT EXISTS Auth (
            id integer PRIMARY KEY AUTOINCREMENT,
            password text
        );
        '''
        self.execute(sql, commit=True)

    def add_password(self, password):
        sql = "INSERT INTO Auth(password) VALUES(?)"
        parameters = (password, )
        self.execute(sql, parameters=parameters, commit=True)
        return True

    def select_all_passwords(self):
        sql = 'SELECT * FROM Auth'
        return self.execute(sql, fetchall=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        # используется для создания sql команды с нужными параметрами для команды ниже
        sql += ' AND '.join([
            f"{item} = ?" for item in parameters.keys()
        ])
        return sql, tuple(parameters.values())

    def select_password(self, **kwargs):
        sql = 'SELECT * FROM Auth WHERE '
        sql, parameters = self.format_args(sql, kwargs)
        return self.execute(sql, parameters, fetchone=True)
        # пример использования команды select_desk(id=131, name='JoJo')

    def count_passwords(self):
        # return int(self.execute("SELECT COUNT(*) FROM Columns;", fetchone=True))
        return self.execute("SELECT COUNT(*) FROM Auth;", fetchone=True)[0]

    def update_password(self, password_id, new_password):
        sql = f"UPDATE Auth SET password=? WHERE id=?"
        self.execute(sql, parameters=(new_password, password_id), commit=True)
        return


if __name__ == '__main__':
    a1 = AuthDB()
    # a1.add_password('6789')
    print(a1.select_all_passwords())
    print(a1.count_passwords())
