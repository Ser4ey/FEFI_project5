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

        if column_id == 'доски с таким id не существует':
            print("!!")
            return None

        # column = self.ColumnsAPI.

    def change_column_name(self, column_id: int, column_name: str) -> bool:
        '''Меняем имя колонки по column_id'''
        if type(column_id) != int:
            print("!")
            raise UserInterfaceExceptions.InvalidColumnIdType()

        if type(column_name) != str:
            print("!!")
            raise UserInterfaceExceptions.InvalidColumnNameContent()

        if column_name.strip() == "":
            print("!!!")
            raise UserInterfaceExceptions.InvalidColumnNameContent()

        if self.get_column_by_column_id(column_id) is None:
            print("!!!!")
            raise UserInterfaceExceptions.ColumnNotExist()

        return True

    def del_column(self, column_id: int) -> bool:
        '''Удаляем колонку + нужно удалить все карточки в колонке'''
        if type(column_id) != int:
            raise UserInterfaceExceptions.InvalidColumnIdType()

        if self.get_column_by_column_id(column_id) is None:
            raise UserInterfaceExceptions.ColumnNotExist()

        return True

    def add_column_to_desk(self, desk_id: int, column_name: str) -> bool:
        '''Добавляем колонку в таблицу'''
        if type(desk_id) != int:
            raise UserInterfaceExceptions.InvalidDeskIdType()

        if type(column_name) != str:
            raise UserInterfaceExceptions.InvalidColumnNameContent()

        if column_name.strip() == "":
            raise UserInterfaceExceptions.InvalidColumnNameContent()

        if self.get_deck_by_desk_id(desk_id) is None:
            raise UserInterfaceExceptions.DeskNotExist()

        return True

    def change_column_position_in_desk(self, desk_id: int, column_id: int, new_sequence_number: int) -> bool:
        '''Меняем номер колонки в таблице '''
        if type(desk_id) != int:
            raise UserInterfaceExceptions.InvalidDeskIdType()

        if self.get_deck_by_desk_id(desk_id) is None:
            raise UserInterfaceExceptions.DeskNotExist()

        if type(column_id) != int:
            raise UserInterfaceExceptions.InvalidColumnIdType()

        if self.get_column_by_column_id(column_id) is None:
            raise UserInterfaceExceptions.ColumnNotExist()

        if type(new_sequence_number) != int:
            raise UserInterfaceExceptions.InvalidSequenceNumberType()

        return True

    def get_cards_by_column_id(self, column_id: int) -> list:
        '''Получаем карточки в колонке по column_id'''
        if type(column_id) != int:
            raise UserInterfaceExceptions.InvalidColumnIdType()

        if self.get_column_by_column_id(column_id) is None:
            raise UserInterfaceExceptions.ColumnNotExist()

        return [
            {
                'card_id': 0,
                'column_id': 2,
                'card_title': 'Заголовок',
                'card_text': 'Много-многоножка',
                'card_status': 1,
                'sequence_number': 0
            },
            {
                'card_id': 1,
                'column_id': 2,
                'card_title': 'Заголовок 2',
                'card_text': 'Лакричный жук',
                'card_status': 2,
                'sequence_number': 1
            }
        ]

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
            raise UserInterfaceExceptions.InvalidCardIdType()

        if card_id == 'не существует':
            return None
        return {
                'card_id': 0,
                'column_id': 2,
                'card_title': 'Заголовок',
                'card_text': 'Много-многоножка',
                'card_status': 1,
                'sequence_number': 0
            }

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

            # обновляем заголовок карточки

        if not (card_text is None):
            if type(card_text) != str:
                raise UserInterfaceExceptions.InvalidCardTextType()

            # обновляем текст карточки

        if not (card_status is None):
            if type(card_status) != int:
                raise UserInterfaceExceptions.InvalidCardStatusType()

            # обновляем текст карточки

        return True

    def move_card(self, card_id: int, column_id: int, new_sequence_number: int) -> bool:
        '''перемещает карточку. Карточки можно перемещать не только в раммках одной колонки, но и между колонками.'''
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

        return True

    def del_card(self, card_id: int) -> bool:
        '''Удалить карточку + смещаем все карточки ниже вверх'''
        if type(card_id) != int:
            raise UserInterfaceExceptions.InvalidCardIdType()

        if self.get_card_by_card_id(card_id) is None:
            raise UserInterfaceExceptions.CardNotExist()

        return True

