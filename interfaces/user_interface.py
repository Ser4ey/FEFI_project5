from interfaces.exceptions.user_interface_exceptions import UserInterfaceExceptions


# TODO: Gleb
class UserInterface:
    def __init__(self):
        pass

    def get_decks(self) -> list:
        '''Возвращает все доски пользователя.
            Формат: [
            {
                'deck_id': 0,
                'desk_name': 'some name'
            },
            {
                'deck_id': 1,
                'desk_name': 'Task99'
            }
        ]'''
        return [
            {
                'deck_id': 0,
                'desk_name': 'some name'
            },
            {
                'deck_id': 1,
                'desk_name': 'Task99'
            }
        ]

    def get_deck_by_desk_id(self, desk_id: int) -> dict | None:
        '''Возвращает все доски пользователя.
        Формат:
        {
            'deck_id': 0,
            'desk_name': 'some name'
        } или None
        '''
        if type(desk_id) != int:
            raise UserInterfaceExceptions.InvalidDeskIdType()

        if desk_id == 'доски с таким id не существует':
            return None

        return {
                'deck_id': 0,
                 'desk_name': 'some name'
                }

    def create_desk(self, desk_name: str) -> bool:
        '''Создаёт доску с именем desk_name'''
        if type(desk_name) != str:
            raise UserInterfaceExceptions.InvalidDeskNameType()

        if desk_name.strip() == "":
            raise UserInterfaceExceptions.InvalidDeskNameContent()

        return True

    def del_desk(self, desk_id: int) -> bool:
        '''Удоляем колонку по desk_id + нужно удалить все колонки и карточки, которые принадлежат этой доске'''
        if type(desk_id) != int:
            raise UserInterfaceExceptions.InvalidDeskIdType()

        if self.get_deck_by_desk_id(desk_id) is None:
            raise UserInterfaceExceptions.DeskNotExist()
        return True

    def change_desk_name(self, desk_id: int, desk_name: str) -> bool:
        '''Меняет имя у доски с id=desk_id на desk_name'''
        if type(desk_id) != int:
            raise UserInterfaceExceptions.InvalidDeskIdType()

        if type(desk_name) != str:
            raise UserInterfaceExceptions.InvalidDeskNameType()

        if desk_name.strip() == "":
            raise UserInterfaceExceptions.InvalidDeskNameContent()

        if self.get_deck_by_desk_id(desk_id) is None:
            raise UserInterfaceExceptions.DeskNotExist()

        return True

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

        if self.get_deck_by_desk_id(desk_id) is None:
            raise UserInterfaceExceptions.DeskNotExist()

        return [
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
        ]

    def get_column_by_column_id(self, column_id: int) -> dict | None:
        '''Получаем информацию о колонку по column_id
        Формат:
            {
                'deck_id': 0,
                'desk_name': 'some name'
            } или None
        '''

        if type(column_id) != int:
            raise UserInterfaceExceptions.InvalidColumnIdType()

        if column_id == 'доски с таким id не существует':
            return None

        return {
                'column_id': 7,
                'desk_id': 12,
                'column_name': 'Колонка 33',
                'sequence_number': 32
            }

    def change_column_name(self, column_id, column_name):
        '''Меняем имя колонки по column_id'''
        return

    def get_cards_by_column_id(self, column_id):
        '''Получаем карточки в колонке по column_id'''
        return

    def del_column(self, column_id):
        '''Удоляем колонку'''
        return

    def add_column_to_desk(self, desk_id, column_name):
        '''Добавляем колонку в таблицу'''
        return

    def change_column_position_in_desk(self):
        '''Меняем номер колонки в таблице '''
        return

    def add_card_to_column(self, card_title, card_status, column_id):
        '''Добавляем карточку в колонку'''
        return

    def get_cards_from_column(self, column_id):
        '''Получаем список всех карточек в колонке'''
        return

    def get_card_info(self, card_id):
        ''''''
        return

    def change_card_info(self, card_id, title='', text='', status=''):
        return

    def move_card(self, card_id, ):
        '''перемещает карточку в новый столбец'''
        return

    def del_card(self, card_id):
        '''Удалить карточку'''
        return
