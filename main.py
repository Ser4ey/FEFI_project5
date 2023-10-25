from database.cards import CardsDB
from database.columns import ColumnsDB
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

tdesk = DeskAPI()
