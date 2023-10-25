# сюда нужно импортировать классы бд
# from loader import connect, db_of_users, db_of_desks

class LoginInterface:
    def __init__(self):
        pass

    def is_user_set_password(self):
        '''Установил ли пользователь пароль'''
        return False

    def update_user_password(self, old_password, password):
        '''Меняет пароль пользователю'''
        return

    def check_password(self, password):
        '''Проверяет правильность пароля'''
        return


class UserInterface:
    def __init__(self):
        pass

    def get_decks(self):
        '''Возвращает все доски пользователя.
            Формат: '''
        decks = {
            'desk_id': ['desk_name', '']
        }
        return

    def create_desk(self, desk_name):
        '''Создаёт доску с именем desk_name'''
        return

    def del_desk(self, desk_id):
        '''Удоляем колонку по desk_id'''
        return

    def change_desk_name(self, desk_id, desk_name):
        '''Меняет имя у доски с id desk_id на desk_name'''
        return

    def move_desk(self):
        '''Перемещаем доску'''
        return

    def get_desk_info(self, desk_id):
        '''Получаем всю информацию о доске  '''
        return

    def get_columns_by_desk_id(self, desk_id):
        '''Получаем все колонки в доске по desk_id'''
        return

    def get_column_info(self, column_id):
        '''Получаем информацию о колонку по column_id'''
        return

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