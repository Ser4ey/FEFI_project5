import sys

from PyQt6 import uic, QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QStackedWidget, QLineEdit, QLabel
from PyQt6.QtGui import QFontDatabase, QIcon
from PyQt6.QtCore import Qt

import ctypes
from ctypes.wintypes import DWORD, ULONG
from ctypes import windll, c_bool, c_int, POINTER, Structure

from interfaces import AppInterface
from interfaces.exceptions import AuthInterfaceExceptions


class AccentPolicy(Structure):
    _fields_ = [
        ('AccentState', DWORD),
        ('AccentFlags', DWORD),
        ('GradientColor', DWORD),
        ('AnimationId', DWORD),
    ]


class WINCOMPATTRDATA(Structure):
    _fields_ = [
        ('Attribute', DWORD),
        ('Data', POINTER(AccentPolicy)),
        ('SizeOfData', ULONG),
    ]


SetWindowCompositionAttribute = windll.user32.SetWindowCompositionAttribute
SetWindowCompositionAttribute.restype = c_bool
SetWindowCompositionAttribute.argtypes = [c_int, POINTER(WINCOMPATTRDATA)]

new_user = 0
auth = 1
set_pass = 2
change_pass = 3
desks = 4
card = 5

icons_path = "UI/icons"
fonts_path = "UI/fonts"
styles_path = "UI/styles"

class GUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.pinned = False
        self.theme = 'dark_theme'
        self.setFixedSize(1024, 768)
        self.blur_background()
        self.setup_ui_form()
        app_icon = QIcon(f"{icons_path}/app_icon.png")
        self.setWindowIcon(app_icon)
        self.stacked_widget = self.findChild(QStackedWidget, 'pageStack')

        if AppInterface.AuthInterface.is_password_set():
            self.stacked_widget.setCurrentIndex(auth)
        else:
            self.stacked_widget.setCurrentIndex(new_user)

        self.connect_buttons()

    def blur_background(self):
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        accent_policy = AccentPolicy()
        accent_policy.AccentState = 3

        win_comp_attr_data = WINCOMPATTRDATA()
        win_comp_attr_data.Attribute = 19
        win_comp_attr_data.SizeOfData = ctypes.sizeof(accent_policy)
        win_comp_attr_data.Data = ctypes.pointer(accent_policy)

        SetWindowCompositionAttribute(c_int(int(self.winId())), ctypes.pointer(win_comp_attr_data))

    def setup_ui_form(self):
        with open(f"{styles_path}/{self.theme}.css") as style:
            uic.loadUi('UI/ui_form.ui', self)
            QFontDatabase.addApplicationFont(f"{fonts_path}/Comfortaa/Comfortaa-Medium.ttf")
            self.setStyleSheet(style.read())
            self.show()
            self.add_menu()

    def add_menu(self):
        self.pin_button = self.findChild(QPushButton, 'pinButton')
        self.theme_button = self.findChild(QPushButton, 'themeButton')
        self.exit_button = self.findChild(QPushButton, 'exitButton')
        self.min_button = self.findChild(QPushButton, 'minButton')

        self.pin_button.clicked.connect(self.pin_toggle)
        self.theme_button.clicked.connect(self.theme_toggle)
        self.exit_button.clicked.connect(self.exit_app)
        self.min_button.clicked.connect(self.min_app)

    def connect_buttons(self):
        self.setpass_button = self.findChild(QPushButton, 'setPassButton')
        self.setpass_button.clicked.connect(self.set_pass)

        self.skippass_button = self.findChild(QPushButton, 'skipPassButton')
        self.skippass_button.clicked.connect(self.skip_pass)

        self.cancel_button = self.findChild(QPushButton, 'cancelButton')
        self.cancel_button.clicked.connect(self.set_pass_cancel)

        self.ok_button = self.findChild(QPushButton, 'okButton')
        self.ok_button.clicked.connect(self.set_pass_confirm)

        self.changepass_button = self.findChild(QPushButton, 'changePassButton')
        self.changepass_button.clicked.connect(self.change_pass)

        self.login_button = self.findChild(QPushButton, 'loginButton')
        self.login_button.clicked.connect(self.login)

        self.cancel_button2 = self.findChild(QPushButton, 'cancelButton_2')
        self.cancel_button2.clicked.connect(self.change_pass_cancel)

        self.ok_button2 = self.findChild(QPushButton, 'okButton_2')
        self.ok_button2.clicked.connect(self.change_pass_confirm)

    def set_pass(self):
        self.stacked_widget.setCurrentIndex(set_pass)

    def set_pass_confirm(self):
        pass_input = self.findChild(QLineEdit, 'passInput')
        pass_input_valid = self.findChild(QLineEdit, 'passInput_valid')
        warning_str = self.findChild(QLabel, 'hintText_3')

        try:
            if pass_input.text() == pass_input_valid.text() and len(
                    pass_input.text()) > 1 and AppInterface.AuthInterface.set_user_password(pass_input.text()):
                self.stacked_widget.setCurrentIndex(auth)
                warning_str.setText("")
                pass_input.clear()
                pass_input_valid.clear()

            elif pass_input.text() != pass_input_valid.text():
                warning_str.setText("Пароли не совпадают!")
                pass_input.clear()
                pass_input_valid.clear()

            elif len(pass_input.text()) < 2:
                warning_str.setText("Слишком короткий пароль!")
                pass_input.clear()
                pass_input_valid.clear()

        except AuthInterfaceExceptions.PasswordAlreadySet:
                warning_str.setText("Пароль уже установлен!")
                pass_input.clear()
                pass_input_valid.clear()

    def set_pass_cancel(self):
        pass_input = self.findChild(QLineEdit, 'passInput')
        pass_input_valid = self.findChild(QLineEdit, 'passInput_valid')
        warning_str = self.findChild(QLabel, 'hintText_3')

        warning_str.setText("")
        pass_input.clear()
        pass_input_valid.clear()
        self.stacked_widget.setCurrentIndex(new_user)

    def skip_pass(self):
        self.stacked_widget.setCurrentIndex(desks)

    def change_pass(self):
        self.stacked_widget.setCurrentIndex(change_pass)
        warning_str = self.findChild(QLabel, 'hintText')
        warning_str.setText("")
        pass_input = self.findChild(QLineEdit, 'passInput_2')
        pass_input.clear()

    def change_pass_confirm(self):
        pass_input = self.findChild(QLineEdit, 'oldpassInput')
        new_pass_input = self.findChild(QLineEdit, 'newpassInput')
        new_pass_input_valid = self.findChild(QLineEdit, 'newpassInput_valid')
        warning_str = self.findChild(QLabel, 'hintText_2')

        try:
            if new_pass_input.text() == new_pass_input_valid.text() and len(new_pass_input.text()) > 1 and AppInterface.AuthInterface.change_user_password(pass_input.text(), new_pass_input.text()):
                self.stacked_widget.setCurrentIndex(auth)
                warning_str.setText("")
                pass_input.clear()
                new_pass_input.clear()
                new_pass_input_valid.clear()

            elif new_pass_input.text() != new_pass_input_valid.text():
                warning_str.setText("Пароли не совпадают!")
                pass_input.clear()
                new_pass_input.clear()
                new_pass_input_valid.clear()

            elif len(new_pass_input.text()) < 2:
                warning_str.setText("Слишком короткий пароль!")
                pass_input.clear()
                new_pass_input.clear()
                new_pass_input_valid.clear()


        except AuthInterfaceExceptions.PasswordNotSet:
                warning_str.setText("Пароль еще не установлен!")
                pass_input.clear()
                new_pass_input.clear()
                new_pass_input_valid.clear()

        except AuthInterfaceExceptions.IncorrectPassword:
                warning_str.setText("Неверный пароль!")
                pass_input.clear()
                new_pass_input.clear()
                new_pass_input_valid.clear()

    def change_pass_cancel(self):
        pass_input = self.findChild(QLineEdit, 'oldpassInput')
        new_pass_input = self.findChild(QLineEdit, 'newpassInput')
        new_pass_input_valid = self.findChild(QLineEdit, 'newpassInput_valid')
        warning_str = self.findChild(QLabel, 'hintText_2')

        warning_str.setText("")
        pass_input.clear()
        new_pass_input.clear()
        new_pass_input_valid.clear()
        self.stacked_widget.setCurrentIndex(auth)

    def login(self):
        pass_input = self.findChild(QLineEdit, 'passInput_2')
        warning_str = self.findChild(QLabel, 'hintText')

        if AppInterface.AuthInterface.check_password(pass_input.text()):
            self.stacked_widget.setCurrentIndex(desks)
            warning_str.setText("")
            pass_input.clear()
        else:
            self.stacked_widget.setCurrentIndex(auth)
            warning_str.setText("Неверный пароль!")
            pass_input.clear()

    def pin_toggle(self):
        self.pinned = not self.pinned
        self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint, self.pinned)
        self.pin_button.setIcon(
            QIcon(f"{icons_path}/pin_icon_active.png" if self.pinned else f"{icons_path}/pin_icon.png"))
        self.show()

    def theme_toggle(self):
        self.theme = 'light_theme' if self.theme == 'dark_theme' else 'dark_theme'
        with open(f"{styles_path}/{self.theme}.css") as style:
            self.setStyleSheet(style.read())
            self.theme_button.setIcon(QIcon(f"{icons_path}/{self.theme}.png"))
        self.show()

    def exit_app(self):
        app.quit()

    def min_app(self):
        self.showMinimized()

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.old_pos = event.pos()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.old_pos = None

    def mouseMoveEvent(self, event):
        if not self.old_pos:
            return

        delta = event.pos() - self.old_pos
        self.move(self.pos() + delta)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GUI()
    window.show()
    sys.exit(app.exec())
