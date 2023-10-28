from interfaces.user_interface import UserInterface
from interfaces.auth_interface import AuthInterface


class AppInterface:
    '''Высокоуровневый интерфейс, содержащий все интерфейсы программы'''
    AuthInterface = AuthInterface()
    UserInterface = UserInterface()


