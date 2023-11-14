from interfaces.exceptions.user_interface_exceptions import UserInterfaceExceptions
from database import DeskAPI, ColumnsAPI, CardsAPI


# TODO: Gleb
class UserInterface:
    def __init__(self):
        self.DeskAPI = DeskAPI()
        self.ColumnsAPI = ColumnsAPI()
        self.CardsAPI = CardsAPI()


    def get_desks(self) -> list:
        '''Возвращает все доски пользователя.
            Формат: [
            {
                'desk_id': 0,
                'desk_name': 'some name'
            },
            {
                'desk_id': 1,
                'desk_name': 'Task99'
            }
        ]'''

        all_desks = self.DeskAPI.get_desks()
        all_desk_id = [desk[0] for desk in all_desks]
        all_desk_name = [desk[1] for desk in all_desks]

        zxc = []
        for i in range(len(all_desks)):
            desk_dict = {"desk_id": all_desk_id[i], "desk_name": all_desk_name[i]}

            zxc.append(desk_dict)
        return zxc


    def get_desk_by_desk_id(self, desk_id: int) -> dict | None:
        '''Возвращает все доски пользователя.
        Формат:
        {
            'desk_id': 0,
            'desk_name': 'some name'
        } или None
        '''

        if type(desk_id) != int:
            raise UserInterfaceExceptions.InvalidDeskIdType()

        desk = self.DeskAPI.get_desk_by_id(desk_id)
        if len(desk) != 0:
            desk_dict = {"desk_id": desk[0][0], "desk_name": desk[0][1]}
            return desk_dict

        if len(desk) == 0:
            return None


    def create_desk(self, desk_name: str) -> bool:
        '''Создаёт доску с именем desk_name'''

        if type(desk_name) != str:
            raise UserInterfaceExceptions.InvalidDeskNameType()

        if desk_name.strip() == "":
            raise UserInterfaceExceptions.InvalidDeskNameContent()

        self.DeskAPI.add_desk(desk_name)

        return True

    def del_desk(self, desk_id: int) -> bool:
        '''Удаляем колонку по desk_id + нужно удалить все колонки и карточки, которые принадлежат этой доске'''
        if type(desk_id) != int:
            raise UserInterfaceExceptions.InvalidDeskIdType()

        if self.get_desk_by_desk_id(desk_id) is None:
            raise UserInterfaceExceptions.DeskNotExist()

        zxc = self.DeskAPI.del_desk_by_id(desk_id)

        return zxc


    def change_desk_name(self, desk_id: int, desk_name: str) -> bool:
        '''Меняет имя у доски с id=desk_id на desk_name'''
        if type(desk_id) != int:
            raise UserInterfaceExceptions.InvalidDeskIdType()

        if type(desk_name) != str:
            raise UserInterfaceExceptions.InvalidDeskNameType()

        if desk_name.strip() == "":
            raise UserInterfaceExceptions.InvalidDeskNameContent()

        if self.get_desk_by_desk_id(desk_id) is None:
            raise UserInterfaceExceptions.DeskNotExist()

        zxc = self.DeskAPI.rename_desk(desk_id, desk_name)

        return zxc

    def get_columns_by_desk_id(self, desk_id: int) -> list:
        '''Возвращает все колонки пользователя по desk_id.
            Формат: [
            {
                'column_id': 0,
                'desk_id': 12,
                'column_name': 'Колонка 33',
                'sequence_number': 0
            },
            {
                'column_id': 1,
                'desk_id': 12,
                'column_name': 'Колонка 44',
                'sequence_number': 1
            },
        ]'''

        if type(desk_id) != int:
            raise UserInterfaceExceptions.InvalidDeskIdType()

        if self.get_desk_by_desk_id(desk_id) is None:
            raise UserInterfaceExceptions.DeskNotExist()

        all_columns = self.ColumnsAPI.get_columns_by_desk_id(desk_id)
        all_columns_id = [column[0] for column in all_columns]
        all_desk_id = [column[1] for column in all_columns]
        all_columns_name = [column[2] for column in all_columns]
        all_sequence_number = [column[3] for column in all_columns]

        zxc = []
        for i in range(len(all_columns)):
            desk_dict = {"column_id": all_columns_id[i], "desk_id": all_desk_id[i], "column_name": all_columns_name[i], "sequence_number": all_sequence_number[i]}
            zxc.append(desk_dict)

        return zxc

    def get_column_by_column_id(self, column_id: int) -> dict | None:  # TODO
        '''Получаем информацию о колонку по column_id
        Формат:
            {
                'desk_id': 0,
                'desk_name': 'some name'
            } или None
        '''

        if type(column_id) != int:
            print("!")
            raise UserInterfaceExceptions.InvalidColumnIdType()

        column = self.ColumnsAPI.get_columns_by_column_id(column_id)
        zxc = {}
        if column:
            zxc = {"column_id": column[0], "desk_id": column[1], "column_name": column[2], "sequence_number": column[3]}
            return zxc

        if len(zxc) == 0:
            return None


    def change_column_name(self, column_id: int, column_name: str) -> bool:
        '''Меняем имя колонки по column_id'''
        if type(column_id) != int:
            raise UserInterfaceExceptions.InvalidColumnIdType()

        if type(column_name) != str:
            raise UserInterfaceExceptions.InvalidColumnNameContent()

        if column_name.strip() == "":
            raise UserInterfaceExceptions.InvalidColumnNameContent()

        if self.get_column_by_column_id(column_id) is None:
            raise UserInterfaceExceptions.ColumnNotExist()

        self.ColumnsAPI.rename_column(column_id, column_name)
        return True


    def del_column(self, column_id: int) -> bool:
        '''Удаляем колонку + нужно удалить все карточки в колонке'''
        if type(column_id) != int:
            print("!")
            raise UserInterfaceExceptions.InvalidColumnIdType()

        if self.get_column_by_column_id(column_id) is None:
            print("!!")
            raise UserInterfaceExceptions.ColumnNotExist()

        self.ColumnsAPI.del_column(column_id)

        return True

    def add_column_to_desk(self, desk_id: int, column_name: str) -> bool:
        '''Добавляем колонку в таблицу'''
        if type(desk_id) != int:
            raise UserInterfaceExceptions.InvalidDeskIdType()

        if type(column_name) != str:
            raise UserInterfaceExceptions.InvalidColumnNameContent()

        if column_name.strip() == "":
            raise UserInterfaceExceptions.InvalidColumnNameContent()

        if self.get_desk_by_desk_id(desk_id) is None:
            raise UserInterfaceExceptions.DeskNotExist()

        self.ColumnsAPI.add_column(desk_id, column_name)
        return True

    def change_column_position_in_desk(self, desk_id: int, column_id: int, new_sequence_number: int) -> bool:
        '''Меняем номер колонки в таблице '''
        if type(desk_id) != int:
            raise UserInterfaceExceptions.InvalidDeskIdType()

        if self.get_desk_by_desk_id(desk_id) is None:
            raise UserInterfaceExceptions.DeskNotExist()

        if type(column_id) != int:
            raise UserInterfaceExceptions.InvalidColumnIdType()

        if self.get_column_by_column_id(column_id) is None:
            raise UserInterfaceExceptions.ColumnNotExist()

        if type(new_sequence_number) != int:
            raise UserInterfaceExceptions.InvalidSequenceNumberType()

        columns_count = len(self.ColumnsAPI.get_columns_by_desk_id(desk_id))

        if new_sequence_number < 1:
            new_sequence_number = 1

        elif new_sequence_number > columns_count:
            new_sequence_number = columns_count

        self.ColumnsAPI.change_column_sequence_number(column_id, new_sequence_number)

        return True

    def get_cards_by_column_id(self, column_id: int) -> list:
        '''Получаем карточки в колонке по column_id'''
        if type(column_id) != int:
            raise UserInterfaceExceptions.InvalidColumnIdType()

        if self.get_column_by_column_id(column_id) is None:
            raise UserInterfaceExceptions.ColumnNotExist()

        all_cards = self.CardsAPI.get_cards_by_column_id(column_id)
        all_card_id = [card[0] for card in all_cards]
        all_column_id = [card[1] for card in all_cards]
        all_card_title = [card[2] for card in all_cards]
        all_card_text = [card[3] for card in all_cards]
        all_card_status = [card[4] for card in all_cards]
        all_sequence_number = [card[5] for card in all_cards]

        zxc = []
        for i in range(len(all_cards)):
            card_dict = {"card_id": all_card_id[i], "column_id": all_column_id[i], "card_title": all_card_title[i], "card_text": all_card_text[i], "card_status": all_card_status[i], "sequence_number": all_sequence_number[i]}
            zxc.append(card_dict)

        return zxc

    def add_card_to_column(self, card_title: str, column_id: int) -> bool:
        '''Добавляем карточку в колонку'''
        if type(column_id) != int:
            raise UserInterfaceExceptions.InvalidColumnIdType()

        if self.get_column_by_column_id(column_id) is None:
            raise UserInterfaceExceptions.ColumnNotExist()

        if type(card_title) != str:
            raise UserInterfaceExceptions.InvalidCardTitleType()

        if card_title.strip() == "":
            raise UserInterfaceExceptions.InvalidCardTitleContent()

        self.CardsAPI.add_card(column_id, card_title)

        return True

    def get_card_by_card_id(self, card_id: int) -> dict | None:
        '''Получаем информацию о карточке по card_id
        Формат возвращаемых данных:
        {
            'card_id': 0,
            'column_id': 2,
            'card_title': 'Заголовок',
            'card_text': 'Много-многоножка',
            'card_status': 1,
            'sequence_number': 0
        }
        '''

        if type(card_id) != int:
            print("!")
            raise UserInterfaceExceptions.InvalidCardIdType()

        card = self.CardsAPI.get_card_by_card_id(card_id)
        zxc = {}
        if card:
            zxc = {"card_id": card[0], "column_id": card[1], "card_title": card[2], "card_text": card[3], "card_status": card[4], "sequence_number": card[5]}
            return zxc

        if len(zxc) == 0:
            return None


    def change_card_info(self, card_id, card_title: str = None, card_text: str = None, card_status: int = None) -> bool:
        if type(card_id) != int:
            raise UserInterfaceExceptions.InvalidCardIdType()

        if self.get_card_by_card_id(card_id) is None:
            raise UserInterfaceExceptions.CardNotExist()

        if not (card_title is None):
            if type(card_title) != str:
                raise UserInterfaceExceptions.InvalidCardTitleType()

            if card_title.strip() == "":
                raise UserInterfaceExceptions.InvalidCardTitleContent()

            self.CardsAPI.change_card_info(card_id=card_id, title=card_title)

        if not (card_text is None):
            if type(card_text) != str:
                raise UserInterfaceExceptions.InvalidCardTextType()

            # обновляем текст карточки
            self.CardsAPI.change_card_info(card_id=card_id, text=card_text)

        if not (card_status is None):
            if type(card_status) != int:
                raise UserInterfaceExceptions.InvalidCardStatusType()

            self.CardsAPI.change_card_info(card_id=card_id, status=card_status)

        return True

    def move_card(self, card_id: int, column_id: int, new_sequence_number: int) -> bool:
        '''Перемещает карточку. Карточки можно перемещать не только в рамках одной колонки, но и между колонками.'''
        if type(card_id) != int:
            raise UserInterfaceExceptions.InvalidCardIdType()

        if self.get_card_by_card_id(card_id) is None:
            raise UserInterfaceExceptions.CardNotExist()

        if type(column_id) != int:
            raise UserInterfaceExceptions.InvalidColumnIdType()

        if self.get_column_by_column_id(column_id) is None:
            raise UserInterfaceExceptions.ColumnNotExist()

        if type(new_sequence_number) != int:
            raise UserInterfaceExceptions.InvalidSequenceNumberType()

        card = self.CardsAPI.get_card_by_card_id(card_id)
        count_cards = len(self.get_cards_by_column_id(column_id))

        if new_sequence_number < 1:
            new_sequence_number = 1
        elif new_sequence_number > count_cards:
            new_sequence_number = count_cards

        if card[1] == column_id:
            self.CardsAPI.change_card_sequence_number(card_id, new_sequence_number)

        else:
            self.CardsAPI.add_card(column_id, card[2])
            new_card_id = self.CardsAPI.get_cards_by_column_id(column_id)[-1][0]

            self.CardsAPI.change_card_sequence_number(new_card_id, new_sequence_number)
            self.CardsAPI.del_card(card_id)

        return True

    def del_card(self, card_id: int) -> bool:
        '''Удалить карточку + смещаем все карточки ниже вверх'''
        if type(card_id) != int:
            raise UserInterfaceExceptions.InvalidCardIdType()

        if self.get_card_by_card_id(card_id) is None:
            raise UserInterfaceExceptions.CardNotExist()

        self.CardsAPI.del_card(card_id)

        return True

