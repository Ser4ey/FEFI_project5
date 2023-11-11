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






