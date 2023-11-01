import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt6.QtGui import QFontDatabase, QIcon
from PyQt6.QtCore import Qt, QRect

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

class MainUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.pinned = False  # The pinned state
        self.theme = True  # Theme style
        self.setFixedSize(1024, 768)
        self.blur_background()
        self.load_ui()
        self.connect_buttons()

    def blur_background(self):
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        accent_policy = AccentPolicy()
        accent_policy.AccentState = 3  # ACCENT_ENABLE_BLURBEHIND

        win_comp_attr_data = WINCOMPATTRDATA()
        win_comp_attr_data.Attribute = 19  # WCA_ACCENT_POLICY
        win_comp_attr_data.SizeOfData = ctypes.sizeof(accent_policy)
        win_comp_attr_data.Data = ctypes.pointer(accent_policy)

        SetWindowCompositionAttribute(c_int(int(self.winId())), ctypes.pointer(win_comp_attr_data))

    def load_ui(self):
        with open("styles/dark_theme.css") as style:
            uic.loadUi('ui_forms/auth.ui', self)
            QFontDatabase.addApplicationFont("fonts/Comfortaa/Comfortaa-Medium.ttf")
            self.setStyleSheet(style.read())
            self.show()

    def connect_buttons(self):
        self.pin_button = self.findChild(QPushButton, 'pinButton')
        self.theme_button = self.findChild(QPushButton, 'themeButton')
        self.exit_button = self.findChild(QPushButton, 'exitButton')
        self.min_button = self.findChild(QPushButton, 'minButton')


        self.pin_button.clicked.connect(self.pin_toggle)
        self.theme_button.clicked.connect(self.theme_toggle)
        self.exit_button.clicked.connect(self.exit_app)
        self.min_button.clicked.connect(self.min_app)

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
        if self.pinned:
            self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint, True)
            self.pin_button.setIcon(QIcon("icons/pin_icon_active.png"))
        else:
            self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint, False)
            self.pin_button.setIcon(QIcon("icons/pin_icon.png"))
        self.show()

    def theme_toggle(self):
        self.theme = not self.theme
        if self.theme:
            with open("styles/dark_theme.css") as style:
                self.setStyleSheet(style.read())
                self.theme_button.setIcon(QIcon("icons/lighttheme.png"))
        else:
            with open("styles/light_theme.css") as style:
                self.setStyleSheet(style.read())
                self.theme_button.setIcon(QIcon("icons/darktheme.png"))
        self.show()

    def exit_app(self):
        app.quit()

    def min_app(self):
        self.showMinimized()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainUI()
    sys.exit(app.exec())