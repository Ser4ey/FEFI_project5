import sys

from PyQt6 import uic, QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt6.QtGui import QFontDatabase, QIcon
from PyQt6.QtCore import Qt

import ctypes
from ctypes.wintypes import DWORD, ULONG
from ctypes import windll, c_bool, c_int, POINTER, Structure


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


class UserInterface(QMainWindow):
    def __init__(self, ui_type):
        super().__init__()
        self.pinned = False
        self.theme = 'dark_theme'
        self.ui_type = ui_type
        self.setFixedSize(1024, 768)
        self.blur_background()
        self.setup_ui_form(self.ui_type)

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

    def setup_ui_form(self, ui_type):
        with open(f"styles/{self.theme}.css") as style:
            uic.loadUi(f'ui_forms/{ui_type}.ui', self)
            QFontDatabase.addApplicationFont("fonts/Comfortaa/Comfortaa-Medium.ttf")
            self.setStyleSheet(style.read())
            self.show()
            self.add_menu()
            self.connect_buttons()

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
        if self.ui_type == 'new_user':
            self.setpass_button = self.findChild(QPushButton, 'setPassButton')
            self.skippass_button = self.findChild(QPushButton, 'skipPassButton')

            self.setpass_button.clicked.connect(self.set_pass)
            self.skippass_button.clicked.connect(self.skip_pass)

        if self.ui_type == 'set_pass':
            self.ok_button = self.findChild(QPushButton, 'okButton')
            self.cancel_button = self.findChild(QPushButton, 'cancelButton')

            self.ok_button.clicked.connect(self.set_pass_complete)
            self.cancel_button.clicked.connect(self.set_pass_cancel)

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

    def pin_toggle(self):
        self.pinned = not self.pinned
        self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint, self.pinned)
        self.pin_button.setIcon(QIcon("icons/pin_icon_active.png" if self.pinned else "icons/pin_icon.png"))
        self.show()

    def theme_toggle(self):
        self.theme = 'light_theme' if self.theme == 'dark_theme' else 'dark_theme'
        with open(f"styles/{self.theme}.css") as style:
            self.setStyleSheet(style.read())
            self.theme_button.setIcon(QIcon(f"icons/{self.theme}.png"))
        self.show()

    def exit_app(self):
        app.quit()

    def min_app(self):
        self.showMinimized()

    # TODO
    def set_pass(self):
        self.ui_type = 'set_pass'
        self.setup_ui_form('set_pass')

    # TODO
    def set_pass_complete(self):
        self.ui_type = 'auth'
        self.setup_ui_form('auth')

    # TODO
    def set_pass_cancel(self):
        self.ui_type = 'new_user'
        self.setup_ui_form('new_user')

    # TODO
    def skip_pass(self):
        self.ui_type = 'auth'
        self.setup_ui_form('auth')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = UserInterface('new_user')
    window.show()
    sys.exit(app.exec())
