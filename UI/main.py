
import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt6.QtGui import QFontDatabase
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

class MainUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1024, 768)
        self.setBlurBehindWindow()
        self.load_ui()
        self.connect_buttons()


    def setBlurBehindWindow(self):
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_NoSystemBackground)

        accent_policy = AccentPolicy()
        accent_policy.AccentState = 3  # ACCENT_ENABLE_BLURBEHIND

        win_comp_attr_data = WINCOMPATTRDATA()
        win_comp_attr_data.Attribute = 19  # WCA_ACCENT_POLICY
        win_comp_attr_data.SizeOfData = ctypes.sizeof(accent_policy)
        win_comp_attr_data.Data = ctypes.pointer(accent_policy)

        SetWindowCompositionAttribute(c_int(int(self.winId())), ctypes.pointer(win_comp_attr_data))

    def load_ui(self):
        with open("style.css") as style:
            uic.loadUi('change_pass.ui', self)
            QFontDatabase.addApplicationFont("fonts/Comfortaa/Comfortaa-Medium.ttf")
            self.setStyleSheet(style.read())
            self.show()

    def connect_buttons(self):
        self.pinned = False  # The pinned state

        self.exit_button = self.findChild(QPushButton, 'exitButton')
        self.pin_button = self.findChild(QPushButton, 'pinButton')
        # self.set_pass_button = self.findChild(QPushButton, 'setPassButton')
        # self.skip_pass_button = self.findChild(QPushButton, 'skipPassButton')

        self.exit_button.clicked.connect(self.exit_app)
        self.pin_button.clicked.connect(self.pin_app)
        # self.set_pass_button.clicked.connect(self.set_password)
        # self.skip_pass_button.clicked.connect(self.skip_password)

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

    def exit_app(self):
        app.quit()

    def pin_app(self):
        self.pinned = not self.pinned
        self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint, self.pinned)
        self.show()

    def set_password(self):
        app.quit()

    def skip_password(self):
        app.quit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainUI()
    sys.exit(app.exec())