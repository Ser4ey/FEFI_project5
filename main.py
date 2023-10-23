import database.cards, database.columns, database.desks

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

# a = Deck()
# print(a.__name)
# print(a.__dict__)

# test_card = database.cards.CardsDB()
# test_card.add_card("test3", 3)

# test_desk = database.desks.DesksDB()
# print(test_desk.update_any_info_about_desk(8, "name", 'MISHA!'))

# test_column = database.columns.ColumnsDB()
#
# print(test_column.update_any_info_about_column(4, 'name', 'test5'))