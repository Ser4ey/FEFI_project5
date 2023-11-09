import data.config
from database.auth import AuthDB


class AuthAPI:
    def __init__(self, path_to_db=data.config.path_to_db):
        self.auth_db = AuthDB(path_to_db)

    def is_user_set_password(self):
        return bool(self.auth_db.count_passwords())

    def add_new_password(self, password):
        if self.is_user_set_password():
            # print(f'У пользователя уже установлен пароль')
            return False
        self.auth_db.add_password(password)
        return True

    def check_password(self, password):
        if self.auth_db.select_password(password=password) is None:
            return False # пароль не верен
        return True # пароль верен

    def change_password(self, current_password, new_password):
        password = self.auth_db.select_password(password=current_password)
        if password is None:
            # print(f'Неверный пароль')
            return False

        password_id = password[0]
        self.auth_db.update_password(password_id, new_password)
        return True


if __name__ == '__main__':
    a1 = AuthAPI()
    r = a1.check_password(12)
    print(r)
    # a1.change_password(777, 98765)

