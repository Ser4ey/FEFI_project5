from interfaces import AppInterface
from interfaces.exceptions import AuthInterfaceExceptions, UserInterfaceExceptions

if __name__ == '__main__':
    print(AppInterface.AuthInterface.is_password_set())
    try:
        AppInterface.AuthInterface.set_user_password('3.11.2023')
    except AuthInterfaceExceptions.PasswordAlreadySet:
        print(f'Пароль уже установлен')

    print(AppInterface.AuthInterface.check_password('3.11.2023'))

