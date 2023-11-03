import sys

from PyQt6 import uic, QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt6.QtGui import QFontDatabase, QIcon
from PyQt6.QtCore import Qt

import ctypes
from ctypes.wintypes import DWORD, ULONG
from ctypes import windll, c_bool, c_int, POINTER, Structure

class UserInterface(QMainWindow):
    def __init__(self, ui_type):
        super().__init__()
        self.ui_type = ui_type

        # Create a central widget to hold the UI
        self.central_widget = self.create_central_widget()
        self.setCentralWidget(self.central_widget)

        # Load the initial UI
        self.load_ui(ui_type)

        # Create a button to change the UI
        self.change_ui_button = QPushButton('Change UI', self)
        self.change_ui_button.clicked.connect(self.change_ui)
        self.central_widget.layout().addWidget(self.change_ui_button)

    def create_central_widget(self):
        # Create a central widget with a layout
        central_widget = QWidget(self)
        layout = QVBoxLayout()
        central_widget.setLayout(layout)
        return central_widget

    def load_ui(self, ui_type):
        # Load the UI into the central widget
        uic.loadUi(f'ui_forms/{ui_type}.ui', self.central_widget)
        # Perform any additional actions related to the UI

    def change_ui(self):
        # Clear the current UI
        self.clear_ui()

        # Load a new UI (it can be of a different type)
        if self.ui_type == 'auth':
            self.load_ui('new_pass')
            self.ui_type = 'new_pass'
        else:
            self.load_ui('auth')
            self.ui_type = 'auth'

    def clear_ui(self):
        # Remove all child widgets and elements from the central widget
        layout = self.central_widget.layout()
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = UserInterface('auth')
    window.show()
    sys.exit(app.exec())