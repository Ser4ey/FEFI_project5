from database.auth_api import AuthAPI
from interfaces.exceptions.auth_interface_exceptions import AuthInterfaceExceptions


class AuthInterface:
    def __init__(self):
        self.auth_db_api = AuthAPI()

    def is_password_set(self) -> bool:
        '''Установлен ли пароль у пользователя'''
        return self.auth_db_api.is_user_set_password()

    def set_user_password(self, password: str) -> bool:
        '''Устанавливает пользователю пароль. Нужно использовать только для установки пароля в 1 первый раз'''
        if type(password) != str:
            raise AuthInterfaceExceptions.InvalidPasswordType()

        if self.is_password_set():
            raise AuthInterfaceExceptions.PasswordAlreadySet()

        return self.auth_db_api.add_new_password(password)

    def check_password(self, password: str) -> bool:
        '''Проверяет правильность пароля'''
        if type(password) != str:
            raise AuthInterfaceExceptions.InvalidPasswordType()

        if not self.is_password_set():
            raise AuthInterfaceExceptions.PasswordNotSet()

        return self.auth_db_api.check_password(password)

    def change_user_password(self, old_password: str, new_password: str) -> bool:
        '''Меняет пароль пользователю'''
        if type(old_password) != str or type(new_password) != str:
            raise AuthInterfaceExceptions.InvalidPasswordType()

        if not self.is_password_set():
            raise AuthInterfaceExceptions.PasswordNotSet()
        if not self.check_password(old_password):
            raise AuthInterfaceExceptions.IncorrectPassword()

        return self.auth_db_api.change_password(old_password, new_password)



