from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QPushButton, QLabel, QDialog, QComboBox, QSpinBox

from UI.uieffects import blur_background, setup_ui_form
from interfaces import AppInterface


class UIPosDialog(QDialog):
    def __init__(self, text, theme, desk_id=None, parent=None):
        super(UIPosDialog, self).__init__(parent)
        self.theme = theme
        setup_ui_form(self, "pos_dialog_ui_form")
        blur_background(self)
        self.columns = AppInterface.UserInterface.get_columns_by_desk_id(desk_id)
        self._init_widgets(text)

    def _init_widgets(self, text):
        self.label = self.findChild(QLabel, "headerText")
        self.label.setText(text)

        self.accept_button = self.findChild(QPushButton, "okButton")
        self.accept_button.clicked.connect(self.accept)

        self.cancel_button = self.findChild(QPushButton, "cancelButton")
        self.cancel_button.clicked.connect(lambda: self.hide())

        self.position_box = self.findChild(QSpinBox, "positionBox")

    def get_new_position(self):
        return self.position_box.value()

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
