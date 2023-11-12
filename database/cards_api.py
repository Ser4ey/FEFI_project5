import data.config
from database.cards import CardsDB


class CardsAPI:
    def __init__(self, path_to_db=data.config.path_to_db):
        self.card_db = CardsDB(path_to_db)

    def get_cards(self):
        return self.card_db.select_all_cards()


    def get_cards_by_column_id(self, column_id):
        return self.card_db.select_cards_by_column_id(column_id=column_id)


    def add_card(self, column_id, card_name):
        last_sequence_number = self.card_db.get_last_sequence_number_by_desk_id(column_id=column_id)

        if last_sequence_number is None:
            last_sequence_number = 0 + 1
        else:
            last_sequence_number += 1

        self.card_db.add_card(title=card_name, column_id=column_id, sequence_number=last_sequence_number)
        return True


    def del_card(self, card_id):
        zxc = self.card_db.select_card(id=card_id)

        if zxc is not None:
            cards_to_update = []
            self.card_db.del_card_by_card_id(card_id)
            deleted_card_id = zxc[1]
            cards = self.card_db.select_cards_by_column_id(deleted_card_id)

            for i in range(len(cards)):
                if cards[i][-1] > zxc[-1]:
                    self.card_db.update_any_info_about_card(cards[i][0], 'sequence_number', cards[i][-1] - 1)
                    cards_to_update.append(cards[i])

            return True
        else:
            return False


    def change_card_info(self, card_id, title=None, text=None, status=None):
        zxc = self.card_db.select_card(id=card_id)

        if zxc is not None:
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
        return self.card_db.change_card_sequence_number(card_id, new_sequence_number)