from FEFI_project5.database.cards import CardsDB

class CardsAPI:
    def __init__(self):
        self.card_db = CardsDB()

    def get_cards(self):
        return self.card_db.select_all_cards()
        '''Список всех карточек'''


    def get_cards_by_desk_id(self, desk_id):
        sql = 'SELECT * FROM Cards, Columns WHERE Cards.column_id = Columns.id and Columns.desk_id=?'
        cards = self.card_db.execute(sql, (desk_id,), fetchall=True)
        # zxc = []
        # for i in range(len(cards)):
        #     if cards[i][7] == desk_id:
        #         zxc.append(cards[i])
        print(len(cards))
        return cards
        '''Список всех карточек принадлежащих desk_id'''
        # return [('card_id', 'column_id', 'card_title', 'card_text', 'card_status', 'sequence_number'), ()]


    def get_cards_by_column_id(self, column_id):  # TODO
        sql = 'SELECT * FROM Cards WHERE column_id=?'
        return self.card_db.execute(sql, (column_id,), fetchall=True)
        # return self.card_db.select_card(column_id=column_id)
        '''Список всех карточек принадлежащих column_id'''


    def add_card(self, column_id, card_name):
        last_sequence_number = 'SELECT MAX(sequence_number) FROM Cards WHERE column_id  =?'
        last_sequence_number = self.card_db.execute(last_sequence_number, (column_id,), fetchone=True)[0]

        if last_sequence_number is None:
            last_sequence_number = 0 + 1
        else:
            last_sequence_number += 1

        self.card_db.add_card(title=card_name, column_id=column_id, sequence_number=last_sequence_number)
        return True

    def del_card(self, card_id):
        zxc = self.card_db.select_card(id=card_id)

        if zxc is not None:
            self.card_db.execute('DELETE FROM Cards WHERE id=?', (card_id,), commit=True)

            deleted_card_id = zxc[1]
            cards_to_update = self.card_db.execute('SELECT * FROM Cards WHERE column_id=? and sequence_number > ?', (deleted_card_id, zxc[-1]), fetchall=True)

            for card in cards_to_update:
                self.card_db.update_any_info_about_card(card[0], 'sequence_number', card[5]-1)
            return True
        else:
            return False


    def chage_card_info(self, card_id, name=None, title=None, text=None, status=None):
        zxc = self.card_db.select_card(id=card_id)

        if zxc is not None:
            if name is not None:
                # self.card_db.update_any_info_about_card(id=card_id, )
                pass
            if title is not None:
                self.card_db.update_any_info_about_card(card_id, 'title', title)
            if text is not None:
                self.card_db.update_any_info_about_card(card_id, 'text', text)
            if status is not None:
                self.card_db.update_any_info_about_card(card_id, 'status', status)
            return True
        else:
            return False


    def change_card_sequence_number(self, card_id, new_sequence_number):
        '''
        Нужно менять номера для всех съехавших колонок
        0
        1 (ставим на 3)
        2
        3
        4
        ->
        0 (0)
        2 (1) - номер съхал на 1 вниз
        3 (2) - номер съхал на 1 вниз
        1 (3)
        4 (4)

        0
        1
        2
        3 (ставим на 1)
        4
        ->
        0 (0)
        3 (1) - номер съхал на 1 вверх
        1 (2) - номер съхал на 1 вверх
        2 (3)
        4 (4)

        :param desk_id:
        :param new_sequence_number:
        :return:
        '''
