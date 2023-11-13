from database.cards import CardsDB
from database.cards_api import CardsAPI

from database.columns import ColumnsDB
from database.columns_api import ColumnsAPI

from database.desks import DesksDB
from database.desk_api import DeskAPI

class App:
    def __init__(self):
        self._decks = []

    @property
    def decks(self):
        return self._decks

    def add_deck(self):
        pass

    def del_desk(self):
        pass


class Deck:
    def __init__(self):
        self.columns = []
        self.__name = 'desk1'

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        # меняем имя в бд
        self.__name = str(new_name)


class Column:
    def __init__(self):
        self.cards = []


class Card:
    def __init__(self):
        pass


desk_api_test = DeskAPI()  # OK

# print(desk_api_test.get_desks())

# for i in range(1, 7):
#     print(desk_api_test.get_desk_by_id(i))

# print(desk_api_test.add_desk('misha7'))

# print(desk_api_test.del_desk_by_id(3))

# print(desk_api_test.rename_desk(2, 'new_misha2'))



column_api_test = ColumnsAPI() # OK
# print(column_api_test.get_columns())

# print(column_api_test.get_columns_by_desk_id(1))

# for i in range(5, 6):
#     print(column_api_test.add_column(1, f'misha1_{i+1}'))
# print(column_api_test.add_column(5, 'misha5_1'))
# print(column_api_test.add_column(2, 'misha2_1'))
# print(column_api_test.del_column(7))

# print(column_api_test.rename_column(12, 'misha1_3'))

# print(column_api_test.change_column_sequence_number(2, 2))



card_api_test = CardsAPI() # OK

# print(card_api_test.get_cards())

# print(card_api_test.get_cards_by_column_id(2))

# print(card_api_test.add_card(1, '1_5'))

# print(card_api_test.del_card(1))

# print(card_api_test.change_card_info(8, text='zxczxczxc'))

# print(card_api_test.change_card_sequence_number(28, 1))