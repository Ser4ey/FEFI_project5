class AuthInterfaceExceptions:
    class PasswordAlreadySet(Exception):
        pass

    class PasswordNotSet(Exception):
        pass

    class IncorrectPassword(Exception):
        pass



