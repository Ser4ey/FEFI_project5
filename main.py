from database.cards import CardsDB
from database.cards_api import CardsAPI

from database.columns import ColumnsDB
from database.columns_api import ColumnsAPI

from database.desks import DesksDB
from database.desk_api import DeskAPI


from interfaces.user_interface import UserInterface
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

print(desk_api_test.del_desk_by_id(6))

# print(desk_api_test.rename_desk(2, 'new_misha2'))

# print(desk_api_test.get_desk_by_id(1))



column_api_test = ColumnsAPI() # OK

# print(column_api_test.get_columns())

# print(column_api_test.get_columns_by_desk_id(1))

# for i in range(5, 6):
#     print(column_api_test.add_column(1, f'misha1_{i+1}'))
# print(column_api_test.add_column(5, 'misha5_5'))
# print(column_api_test.add_column(6, "misha6_5"))

# print(column_api_test.del_column(2))

# print(column_api_test.rename_column(12, 'misha1_3'))

# print(column_api_test.change_column_sequence_number(2, 2))

# print(column_api_test.get_columns_by_column_id(1))


column_db_test = ColumnsDB()

# print(column_db_test.del_column_by_column_id(20))


card_api_test = CardsAPI() # OK

# print(card_api_test.get_cards())

# print(card_api_test.get_cards_by_column_id(2))

# print(card_api_test.add_card(14, '14_5'))

# print(card_api_test.del_card(15))

# print(card_api_test.change_card_info(8, text='zxczxczxc'))

# print(card_api_test.change_card_sequence_number(28, 1))

# print(card_api_test.get_card_by_card_id(8))


user_interface_test = UserInterface()

# print(user_interface_test.change_column_name(2, "new_misha2_1"))

# print(user_interface_test.del_column(1))

# print(user_interface_test.add_column_to_desk(1, "new_misha1_6"))

# print(user_interface_test.add_column_to_desk(5, "misha5_6"))

# print(user_interface_test.change_column_position_in_desk(5, 12, 6))

# print(user_interface_test.add_card_to_column("1_4", 11))
# print(user_interface_test.add_card_to_column("1_4", 11))

# print(user_interface_test.get_card_by_card_id(8))

# print(user_interface_test.change_card_info(20, card_title="123"))

# print(user_interface_test.get_card_by_card_id(20))

# print(user_interface_test.change_card_info(8, card_status=1))

# print(user_interface_test.move_card(24, 14, 3))

# print(user_interface_test.del_card(100))