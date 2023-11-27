from PyQt6.QtCore import QSize, QCoreApplication
from PyQt6.QtGui import QIcon, QCursor, QPixmap
from PyQt6.QtWidgets import QMainWindow, QPushButton, QStackedWidget, QLineEdit, QLabel, QWidget, \
    QVBoxLayout, QScrollArea, QDialog, QHBoxLayout, QLayout, QTextEdit, QCheckBox

from UI.uieffects import *
from UI.uiconstants import UIConst
from UI.uidialog import UIDialog
from interfaces import AppInterface
from interfaces.exceptions import AuthInterfaceExceptions


class UIMain(QMainWindow):
    def __init__(self):
        super().__init__()
        self.pinned = False
        self.theme = 'dark_theme'
        self.setFixedSize(1024, 768)
        blur_background(self)
        self.desks_buttons = []
        self.card_buttons = []
        self.columns = []
        self.active_desk_id = 0
        self.active_column_id = 0
        self.active_card_id = 0
        setup_ui_form(self, "ui_form")
        self.add_menu()
        app_icon = QIcon(f"{UIConst.icons_path}/app_icon.png")
        self.setWindowIcon(app_icon)
        self.stacked_widget = self.findChild(QStackedWidget, 'pageStack')

        if AppInterface.AuthInterface.is_password_set():
            self.stacked_widget.setCurrentIndex(UIConst.auth_page)
        else:
            self.stacked_widget.setCurrentIndex(UIConst.new_user_page)

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

        self.logout_button = self.findChild(QPushButton, 'logoutButton')
        self.logout_button.clicked.connect(self.logout)

        self.cancel_button2 = self.findChild(QPushButton, 'cancelButton_2')
        self.cancel_button2.clicked.connect(self.change_pass_cancel)

        self.ok_button2 = self.findChild(QPushButton, 'okButton_2')
        self.ok_button2.clicked.connect(self.change_pass_confirm)

        self.desks_scroll_area = self.findChild(QScrollArea, "desksArea")
        self.desks_scroll_content = QWidget()
        self.desks_scroll_layout = QVBoxLayout(self.desks_scroll_content)

        self.desks_scroll_area.setWidgetResizable(True)
        self.desks_scroll_area.setWidget(self.desks_scroll_content)

        self.new_desk_button = self.findChild(QPushButton, 'newdeskButton')
        self.new_desk_button.clicked.connect(self.add_new_desk)

        self.desk_name_button = self.findChild(QPushButton, 'desknameButton')
        self.delete_desk_button = self.findChild(QPushButton, 'deletedeskButton')

        self.desk_name_button.clicked.connect(self.rename_desk)
        self.delete_desk_button.clicked.connect(self.delete_desk)

        self.new_column_button = self.findChild(QPushButton, 'addcolomnButton')
        self.new_column_button.clicked.connect(self.add_new_column)

        self.columns_scroll_area = self.findChild(QScrollArea, "columnsArea")
        self.columns_scroll_content = QWidget()
        self.columns_scroll_layout = QHBoxLayout(self.columns_scroll_content)

        self.columns_scroll_area.setWidgetResizable(True)
        self.columns_scroll_area.setWidget(self.columns_scroll_content)

        self.column_label = self.findChild(QLabel, 'columnLabel')

        self.cards_scroll_area = self.findChild(QScrollArea, "cardsArea")
        self.cards_scroll_content = QWidget()
        self.cards_scroll_layout = QVBoxLayout(self.cards_scroll_content)

        self.cards_scroll_area.setWidgetResizable(True)
        self.cards_scroll_area.setWidget(self.cards_scroll_content)

        self.card_text_edit = self.findChild(QTextEdit, "cardText")

        self.card_name_button = self.findChild(QPushButton, 'cardnameButton')
        self.delete_card_button = self.findChild(QPushButton, 'deletecardButton')
        self.close_card_button = self.findChild(QPushButton, 'closecardButton')
        self.add_new_card_button = self.findChild(QPushButton, 'newcardButton2')
        self.save_card_button = self.findChild(QPushButton, 'savecardButton')
        self.card_status_box = self.findChild(QCheckBox, 'cardstatusBox')

        self.card_name_button.clicked.connect(self.rename_card)
        self.delete_card_button.clicked.connect(self.delete_card)
        self.close_card_button.clicked.connect(self.close_card)
        self.add_new_card_button.clicked.connect(self.add_new_card_from_cards)
        self.save_card_button.clicked.connect(self.save_card_info)
        self.card_status_box.stateChanged.connect(self.change_card_status)

    def set_pass(self):
        self.stacked_widget.setCurrentIndex(UIConst.set_pass_page)

    def set_pass_confirm(self):
        pass_input = self.findChild(QLineEdit, 'passInput')
        pass_input_valid = self.findChild(QLineEdit, 'passInput_valid')
        warning_str = self.findChild(QLabel, 'hintText_3')

        try:
            if pass_input.text() == pass_input_valid.text() and len(
                    pass_input.text()) > 1 and AppInterface.AuthInterface.set_user_password(pass_input.text()):
                self.stacked_widget.setCurrentIndex(UIConst.auth_page)
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
        self.stacked_widget.setCurrentIndex(UIConst.new_user_page)

    def skip_pass(self):
        self.stacked_widget.setCurrentIndex(UIConst.desks_page)

    def change_pass(self):
        self.stacked_widget.setCurrentIndex(UIConst.change_pass_page)
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
            if new_pass_input.text() == new_pass_input_valid.text() and len(
                    new_pass_input.text()) > 1 and AppInterface.AuthInterface.change_user_password(pass_input.text(),
                                                                                                   new_pass_input.text()):
                self.stacked_widget.setCurrentIndex(UIConst.auth_page)
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
        self.stacked_widget.setCurrentIndex(UIConst.auth_page)

    def login(self):
        pass_input = self.findChild(QLineEdit, 'passInput_2')
        warning_str = self.findChild(QLabel, 'hintText')

        if AppInterface.AuthInterface.check_password(pass_input.text()):
            self.stacked_widget.setCurrentIndex(UIConst.desks_page)

            self.load_desks()

            warning_str.setText("")
            pass_input.clear()
        else:
            self.stacked_widget.setCurrentIndex(UIConst.auth_page)
            warning_str.setText("Неверный пароль!")
            pass_input.clear()

    def logout(self):
        if AppInterface.AuthInterface.is_password_set():
            self.stacked_widget.setCurrentIndex(UIConst.auth_page)
        else:
            self.stacked_widget.setCurrentIndex(UIConst.new_user_page)

    def load_desks(self):
        self.desks_buttons = []
        desks = AppInterface.UserInterface.get_desks()

        for i in reversed(range(self.desks_scroll_layout.count())):
            widget_to_remove = self.desks_scroll_layout.itemAt(i).widget()
            self.desks_scroll_layout.removeWidget(widget_to_remove)
            widget_to_remove.setParent(None)

        for desk_info in desks:
            id = desk_info["desk_id"]
            desk_name = desk_info['desk_name']

            desk_button = QPushButton(desk_name)
            desk_button.clicked.connect(lambda _, idx=id: self.open_desk(idx))
            desk_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
            desk_button.setStyleSheet(UIConst.desk_button_style)
            desk_button.setFixedSize(190, 60)

            if "сигм" in desk_name.lower() or "sigm" in desk_name.lower():
                image = QPixmap(f"{UIConst.icons_path}/sigma.png")
                desk_button.setIcon(QIcon(image))
                desk_button.setIconSize(QSize(60, 60))

            self.desks_buttons.append([desk_button, id])

            if id == self.active_desk_id and id != 0:
                for desk_button, button_id in self.desks_buttons:
                    if button_id == self.active_desk_id:
                        desk_button.click()

            if self.active_desk_id == 0:
                self.desks_buttons[0][0].click()

            self.desks_scroll_layout.addWidget(desk_button)

        if not self.desks_buttons:
            self.desk_name_button.setVisible(False)
            self.delete_desk_button.setVisible(False)
            self.columns_scroll_area.setVisible(False)
            self.new_column_button.setVisible(False)
        else:
            self.desk_name_button.setVisible(True)
            self.delete_desk_button.setVisible(True)
            self.columns_scroll_area.setVisible(True)
            self.new_column_button.setVisible(True)

    def open_desk(self, id):
        self.active_desk_id = id

        for desk_button, idx in self.desks_buttons:
            if idx == id:
                desk_button.setStyleSheet(UIConst.desk_active_style)
                self.desk_name_button.setText(desk_button.text())
            else:
                desk_button.setStyleSheet(UIConst.desk_not_active_style)

        self.load_columns(self.active_desk_id)

    def load_columns(self, id):
        self.columns = []

        def clear_layout(layout):
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.setParent(None)
                    widget.deleteLater()
                else:
                    sub_layout = item.layout()
                    if sub_layout is not None:
                        clear_layout(sub_layout)

        clear_layout(self.columns_scroll_layout)

        for column in AppInterface.UserInterface.get_columns_by_desk_id(id):
            id = column["column_id"]
            column_name = column['column_name']

            column_layout = QVBoxLayout()
            column_name_button = QPushButton(column_name)
            column_name_button.setFixedSize(231, 55)
            column_name_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
            column_name_button.setStyleSheet(UIConst.column_name_button_style)
            column_name_button.clicked.connect(lambda _, idx=id: self.rename_column(idx))

            column_delete_button = QPushButton("удалить")
            column_delete_button.setFixedSize(231, 19)
            column_delete_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
            column_delete_button.setStyleSheet(UIConst.column_delete_button_style)
            column_delete_button.clicked.connect(lambda _, idx=id: self.delete_column(idx))

            column_area = QScrollArea()
            column_area.setFixedSize(231, 500)
            column_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
            column_area.setStyleSheet(UIConst.column_scroll_area_style)
            column_scroll_content = QWidget()
            column_scroll_layout = QVBoxLayout(column_scroll_content)
            column_area.setWidgetResizable(True)
            column_area.setWidget(column_scroll_content)
            self.load_cards(column_scroll_layout, id)

            column_add_card_button = QPushButton("+ карточка")
            column_add_card_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
            column_add_card_button.setStyleSheet(UIConst.column_add_card_button_style)
            column_add_card_button.clicked.connect(lambda _, idx=id: self.add_new_card_from_desk(idx))

            column_layout.addWidget(column_name_button)
            column_layout.addWidget(column_delete_button)
            column_layout.addWidget(column_area)
            column_layout.addWidget(column_add_card_button)

            self.columns.append([column_layout, id])
            self.columns_scroll_layout.addLayout(column_layout)

    def load_cards(self, column_scroll_layout, id):
        for column in AppInterface.UserInterface.get_cards_by_column_id(id):
            card_id = column["card_id"]
            card_name = column['card_title']
            card_status = column['card_status']

            card_button = QPushButton(card_name)
            card_button.clicked.connect(
                lambda _, columnid=id, cardid=card_id: self.open_card_from_desk(columnid, cardid))
            card_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
            if card_status == 1:
                card_button.setStyleSheet(UIConst.card_button_red_style)
            elif card_status == 2:
                card_button.setStyleSheet(UIConst.card_button_green_style)
            else:
                card_button.setStyleSheet(UIConst.card_button_none_style)

            card_button.setFixedSize(195, 40)

            column_scroll_layout.addWidget(card_button)

    def add_new_card_from_desk(self, id):
        dialog = UIDialog("Введите имя карточки", self.theme)
        result = dialog.exec()

        if result == QDialog.DialogCode.Accepted and dialog.get_new_name() != "":
            name = dialog.get_new_name()

            try:
                AppInterface.UserInterface.add_card_to_column(name, id)
            except Exception:
                pass

        self.open_desk(self.active_desk_id)

    def add_new_card_from_cards(self):
        dialog = UIDialog("Введите имя карточки", self.theme)
        result = dialog.exec()

        if result == QDialog.DialogCode.Accepted and dialog.get_new_name() != "":
            name = dialog.get_new_name()

            try:
                AppInterface.UserInterface.add_card_to_column(name, self.active_column_id)
            except Exception:
                pass

        self.open_card_from_desk(self.active_column_id, self.active_card_id)

    def open_card_from_desk(self, columnid, cardid):
        if cardid is not None:
            self.active_column_id = columnid
            self.stacked_widget.setCurrentIndex(UIConst.card_page)
            column_info = AppInterface.UserInterface.get_column_by_column_id(columnid)
            cards = AppInterface.UserInterface.get_cards_by_column_id(columnid)
            if cardid == 0:
                self.active_card_id = cards[0]["card_id"]
            else:
                self.active_card_id = cardid
            self.column_label.setText(column_info["column_name"])

            card_info = AppInterface.UserInterface.get_card_by_card_id(self.active_card_id)
            card_name = card_info["card_title"]
            card_text = card_info["card_text"]
            card_status = card_info["card_status"]

            if card_status == 1:
                self.card_name_button.setStyleSheet(UIConst.card_button_red_style)
            elif card_status == 2:
                self.card_name_button.setStyleSheet(UIConst.card_button_green_style)
            else:
                self.card_name_button.setStyleSheet(UIConst.card_button_none_style)

            self.card_text_edit.setText(card_text)
            self.card_name_button.setText(card_name)

            self.card_buttons = []
            for i in reversed(range(self.cards_scroll_layout.count())):
                widgetToRemove = self.cards_scroll_layout.itemAt(i).widget()
                self.cards_scroll_layout.removeWidget(widgetToRemove)
                widgetToRemove.setParent(None)

            for xcard_info in cards:
                xcard_name = xcard_info["card_title"]
                xcard_id = xcard_info["card_id"]
                xcard_status = xcard_info["card_status"]

                card_button = QPushButton(xcard_name)
                card_button.clicked.connect(
                    lambda _, columnidx=columnid, cardidx=xcard_id: self.open_card_from_cards(cardidx))
                card_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
                card_button.setFixedSize(190, 60)

                if xcard_status == 1:
                    card_button.setStyleSheet(UIConst.card_button_red_style)
                elif xcard_status == 2:
                    card_button.setStyleSheet(UIConst.card_button_green_style)
                else:
                    card_button.setStyleSheet(UIConst.card_button_none_style)

                self.card_buttons.append([card_button, xcard_id])

                if xcard_id == self.active_card_id:
                    card_button.click()

                self.cards_scroll_layout.addWidget(card_button)
        else:
            self.close_card()

    def open_card_from_cards(self, cardid):
        self.active_card_id = cardid

        card_info = AppInterface.UserInterface.get_card_by_card_id(cardid)
        card_name = card_info["card_title"]
        card_text = card_info["card_text"]
        card_status = card_info["card_status"]

        if card_status == 1:
            self.card_status_box.setCheckState(Qt.CheckState.PartiallyChecked)
            self.card_status_box.setText("Не выполнено")
            self.card_name_button.setStyleSheet(UIConst.card_button_red_style)
        elif card_status == 2:
            self.card_status_box.setCheckState(Qt.CheckState.Checked)
            self.card_status_box.setText("Выполнено")
            self.card_name_button.setStyleSheet(UIConst.card_button_green_style)
        else:
            self.card_status_box.setCheckState(Qt.CheckState.Unchecked)
            self.card_status_box.setText("Без статуса")
            self.card_name_button.setStyleSheet(UIConst.card_button_none_style)

        self.card_text_edit.setText(card_text)
        self.card_name_button.setText(card_name)

    def rename_card(self):
        dialog = UIDialog("Введите новое имя карточки", self.theme)
        result = dialog.exec()

        if result == QDialog.DialogCode.Accepted and dialog.get_new_name() != "":
            new_name = dialog.get_new_name()

            for cards in self.card_buttons:
                if cards[1] == self.active_card_id:
                    cards[0].setText(new_name)
                    break

            try:
                AppInterface.UserInterface.change_card_info(self.active_card_id, card_title=new_name)
                self.open_card_from_cards(self.active_card_id)
            except Exception:
                pass

    def delete_card(self):
        try:
            AppInterface.UserInterface.del_card(self.active_card_id)
        except Exception:
            pass
        if AppInterface.UserInterface.get_cards_by_column_id(self.active_column_id):
            self.open_card_from_desk(self.active_column_id, 0)
        else:
            self.open_card_from_desk(self.active_column_id, None)

    def close_card(self):
        self.stacked_widget.setCurrentIndex(UIConst.desks_page)
        self.load_desks()

    def save_card_info(self):
        try:
            AppInterface.UserInterface.change_card_info(self.active_card_id, card_text=self.card_text_edit.toPlainText())
        except Exception:
            pass

    def change_card_status(self):
        try:
            state = self.card_status_box.checkState()
            if state == Qt.CheckState.PartiallyChecked:
                self.card_status_box.setText("Не выполнено")
                self.card_name_button.setStyleSheet(UIConst.card_button_red_style)
                AppInterface.UserInterface.change_card_info(self.active_card_id, card_status=1)
                for card_button, idx in self.card_buttons:
                    if idx == self.active_card_id:
                        card_button.setStyleSheet(UIConst.card_button_red_style)

            elif state == Qt.CheckState.Checked:
                self.card_status_box.setText("Выполнено")
                self.card_name_button.setStyleSheet(UIConst.card_button_green_style)
                AppInterface.UserInterface.change_card_info(self.active_card_id, card_status=2)
                for card_button, idx in self.card_buttons:
                    if idx == self.active_card_id:
                        card_button.setStyleSheet(UIConst.card_button_green_style)

            else:
                self.card_status_box.setText("Без статуса")
                self.card_name_button.setStyleSheet(UIConst.card_button_none_style)
                AppInterface.UserInterface.change_card_info(self.active_card_id, card_status=0)
                for card_button, idx in self.card_buttons:
                    if idx == self.active_card_id:
                        card_button.setStyleSheet(UIConst.card_button_none_style)
        except Exception:
            pass

    def add_new_desk(self):
        dialog = UIDialog("Введите имя доски", self.theme)
        result = dialog.exec()

        if result == QDialog.DialogCode.Accepted and dialog.get_new_name() != "":
            name = dialog.get_new_name()

            try:
                AppInterface.UserInterface.create_desk(name)
            except Exception:
                pass

        self.load_desks()

    def add_new_column(self):
        dialog = UIDialog("Введите имя столбца", self.theme)
        result = dialog.exec()

        if result == QDialog.DialogCode.Accepted and dialog.get_new_name() != "":
            name = dialog.get_new_name()

            try:
                AppInterface.UserInterface.add_column_to_desk(self.active_desk_id, name)
            except Exception:
                pass

        self.open_desk(self.active_desk_id)

    def delete_column(self, id):
        try:
            AppInterface.UserInterface.del_column(id)
        except Exception:
            pass

        self.open_desk(self.active_desk_id)

    def rename_column(self, id):
        dialog = UIDialog("Введите новое имя столбца", self.theme)
        result = dialog.exec()

        if result == QDialog.DialogCode.Accepted and dialog.get_new_name() != "":
            new_name = dialog.get_new_name()

            for column in self.columns:
                if column[1] == id:
                    column[0].itemAt(0).widget().setText(new_name)
                    break

            try:
                AppInterface.UserInterface.change_column_name(id, new_name)
            except Exception:
                pass

    def rename_desk(self, id):

        dialog = UIDialog("Введите новое имя доски", self.theme)
        result = dialog.exec()

        if result == QDialog.DialogCode.Accepted and dialog.get_new_name() != "":
            new_name = dialog.get_new_name()

            for desk in self.desks_buttons:
                if desk[1] == id:
                    desk[0].setText(new_name)
                    break
            try:
                self.desk_name_button.setText(new_name)
                AppInterface.UserInterface.change_desk_name(self.active_desk_id, new_name)
                self.load_desks()
            except Exception:
                pass

    def delete_desk(self):
        try:
            AppInterface.UserInterface.del_desk(self.active_desk_id)
            self.active_desk_id = 0
            self.active_column_id = 0
            self.active_card_id = 0
            self.load_desks()
        except Exception:
            pass

    def pin_toggle(self):
        self.pinned = not self.pinned
        self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint, self.pinned)
        self.pin_button.setIcon(
            QIcon(f"{UIConst.icons_path}/pin_icon_active.png" if self.pinned else f"{UIConst.icons_path}/pin_icon.png"))
        self.show()

    def theme_toggle(self):
        self.theme = 'light_theme' if self.theme == 'dark_theme' else 'dark_theme'
        with open(f"{UIConst.styles_path}/{self.theme}.css") as style:
            self.setStyleSheet(style.read())
            self.theme_button.setIcon(QIcon(f"{UIConst.icons_path}/{self.theme}.png"))
        self.show()

    def exit_app(self):
        QCoreApplication.quit()

    def min_app(self):
        self.showMinimized()

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
