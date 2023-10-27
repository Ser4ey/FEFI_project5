from database.desks import DesksDB


class DeskAPI:
    def __init__(self):
        self.desk_db = DesksDB()

    def get_desks(self):
        return self.desk_db.select_all_desks()
        # return [('desk_id1', 'desk_name1', 'sequence_number1'), ('desk_id2', 'desk_name2', 'sequence_number2')]

    def get_desk_by_id(self, desk_id):
        return self.desk_db.select_desk(id=desk_id)
        # return ('desk_id', 'desk_name', 'sequence_number')

    def add_desk(self, desk_name):
        '''Добавляем доску (в конец)
           Проверка на уникальное имя
           Важно задать правильный sequence_number'''
        try:
            self.desk_db.add_desk(name=desk_name)
            return True # - успех
        except Exception as error:
            print(error)
            return False


    def del_desk(self, desk_id):
        '''
        Удаляем доску
        Проверка на наличие
        Нужно поменять sequence_number для всех съхавших досок
        :param desk_id:
        :return: bool
        '''
        zxc = self.desk_db.select_desk(id=desk_id)
        if zxc is not None:
            self.desk_db.execute("DELETE FROM Desks WHERE id=?", (desk_id,), commit=True)
            return True
        else:
            return False


    def rename_desk(self, desk_id, new_name):
        '''Меняем имя у доски
           Проверка на уникальное имя
           Проверка, что доска существует'''

        existing_desk = self.desk_db.select_desk(id=desk_id)

        if existing_desk:
            try:
                self.desk_db.update_any_info_about_desk(desk_id, "name", new_name)
            except:
                return False
            return True
        else:
            return False