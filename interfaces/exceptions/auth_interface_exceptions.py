class AuthInterfaceExceptions:
    class InvalidPasswordType(Exception):
        pass

    class PasswordAlreadySet(Exception):
        pass

    class PasswordNotSet(Exception):
        pass

    class IncorrectPassword(Exception):
        pass



