from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QPushButton, QLabel, QDialog, QComboBox

from UI.uieffects import blur_background, setup_ui_form
from interfaces import AppInterface


class UIMoveDialog(QDialog):
    def __init__(self, text, theme, desk_id=None, column_id=None, parent=None):
        super(UIMoveDialog, self).__init__(parent)
        self.theme = theme
        setup_ui_form(self, "move_dialog_ui_form")
        blur_background(self)
        self.columns = AppInterface.UserInterface.get_columns_by_desk_id(desk_id)
        self._init_widgets(text, column_id)

    def _init_widgets(self, text, column_id):
        self.label = self.findChild(QLabel, "headerText")
        self.label.setText(text)

        self.accept_button = self.findChild(QPushButton, "okButton")
        self.accept_button.clicked.connect(self.accept)

        self.cancel_button = self.findChild(QPushButton, "cancelButton")
        self.cancel_button.clicked.connect(lambda: self.hide())

        self.column_label = self.findChild(QLabel, "columnLabel")
        self.column_box = self.findChild(QComboBox, "columnBox")

        current_column = [column['column_name'] for column in self.columns if column['column_id'] == column_id][0]
        column_names = [column['column_name'] for column in self.columns]
        self.column_box.addItems(column_names)
        self.column_box.setCurrentText(current_column)

    def get_new_column(self):
        new_column_name = self.column_box.currentText()
        new_column_id = [column['column_id'] for column in self.columns
                         if column['column_name'] == new_column_name][0]
        return new_column_id

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
