from database.columns import  ColumnsDB

class ColumnsAPI:
    def __init__(self):
        self.column_db = ColumnsDB()

    def get_columns(self):
        '''Список всех колонок'''
        return self.column_db.select_all_columns()

    def get_columns_by_desk_id(self, desk_id):  # TODO
        sql = 'SELECT * FROM Columns WHERE desk_id=?'
        return self.column_db.execute(sql, (desk_id,), fetchall=True)
        '''Список всех колонок принадлежащих desk_id'''
        # return self.column_db.select_column(desk_id=desk_id)

    def add_column(self, desk_id, column_name):
        last_sequence_number = 'SELECT MAX(sequence_number) FROM Columns WHERE desk_id=?'
        last_sequence_number = self.column_db.execute(last_sequence_number,(desk_id,), fetchone=True)[0]

        if last_sequence_number is None:
            last_sequence_number = 0 + 1
        else:
            last_sequence_number += 1
        try:
            self.column_db.add_column(desk_id=desk_id, name=column_name, sequence_number=last_sequence_number)
        except:
            return False

        return True


    def del_column(self, column_id):
        zxc = self.column_db.select_column(id=column_id)

        if zxc is not None:
            self.column_db.execute("DELETE FROM Columns WHERE id=?", (column_id,), commit=True)

            deleted_column_id = zxc[1]  # desk_id удаленной строки, чтобы потом пересчитать sequence_number у этой доски
            columns_to_update = self.column_db.execute('SELECT * FROM Columns WHERE desk_id=? and sequence_number > ?', (deleted_column_id, zxc[3]), fetchall=True)

            for column in columns_to_update:
                self.column_db.update_any_info_about_column(column[0], 'sequence_number', column[3]-1)
            return True
        else:
            return False


    def rename_column(self, column_id, new_name):
        existing_column = self.column_db.select_column(id=column_id)

        if existing_column is not None:
            try:
                self.column_db.update_any_info_about_column(column_id, 'name', new_name)
            except:
                return False
            return True
        else:
            return False


    def change_column_sequence_number(self, column_id, new_sequence_number):  #  TODO
        # Получите текущий номер последовательности для выбранной колонки
        column = self.column_db.select_column(id=column_id)

        if column is not None:
            current_sequence_number = column[3]

            # Определите, на сколько позиций съедут другие колонки
            shift = new_sequence_number - current_sequence_number

            # Обновите sequence_number выбранной колонки на новое значение
            self.column_db.update_any_info_about_column(column_id, 'sequence_number', new_sequence_number)

            # Обновите sequence_number для остальных колонок с тем же desk_id
            # в соответствии с их новыми позициями
            columns_to_update = self.column_db.execute(
                "SELECT id, sequence_number FROM Columns WHERE desk_id=? AND id != ?", (column[1], column_id),
                fetchall=True)

            for col in columns_to_update:
                updated_sequence_number = col[1] + shift
                self.column_db.update_any_info_about_column(col[0], 'sequence_number', updated_sequence_number)

            return True
        else:
            return False  # Колонка с указанным column_id не найдена

        '''
        Нужно менять номера для всех съехавших колонок
        1
        2 (ставим на 4)
        3
        4
        5
        ->
        1 (1)
        3 (2) - номер съхал на 1 вниз
        4 (3) - номер съхал на 1 вниз
        2 (4)
        5 (5)

        0
        1
        2
        3 (ставим на 1)
        4
        ->
        0 (0)
        3 (1) - номер съхал на 1 вверх
        1 (2) - номер съхал на 1 вверх
        2 (3)
        4 (4)

        :param desk_id:
        :param new_sequence_number:
        :return:
        '''