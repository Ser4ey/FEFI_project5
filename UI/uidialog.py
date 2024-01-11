from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QPushButton, QLineEdit, QLabel, QDialog

from UI.uieffects import blur_background, setup_ui_form


class UIDialog(QDialog):
    def __init__(self, text, theme, parent=None):
        super(UIDialog, self).__init__(parent)
        self.theme = theme
        setup_ui_form(self, "dialog_ui_form")
        blur_background(self)
        self._init_widgets(text)

    def _init_widgets(self, text):
        self.label = self.findChild(QLabel, "headerText")
        self.label.setText(text)

        self.accept_button = self.findChild(QPushButton, "okButton")
        self.accept_button.clicked.connect(self.accept)

        self.cancel_button = self.findChild(QPushButton, "cancelButton")
        self.cancel_button.clicked.connect(lambda: self.hide())

        self.new_name_input = self.findChild(QLineEdit, "nameInput")

    def get_new_name(self):
        return self.new_name_input.text()

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.old_pos = event.pos()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.old_pos = None

    def mouseMoveEvent(self, event):
        try:

            if not self.old_pos:
                return
            delta = event.pos() - self.old_pos
            self.move(self.pos() + delta)

        except Exception:
            pass
