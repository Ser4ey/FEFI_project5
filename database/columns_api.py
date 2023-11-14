import data.config
from database.columns import ColumnsDB


class ColumnsAPI:
    def __init__(self, path_to_db=data.config.path_to_db):
        self.column_db = ColumnsDB(path_to_db)

    def get_columns(self):
        return self.column_db.select_all_columns()


    def get_columns_by_desk_id(self, desk_id):
        return self.column_db.select_columns_by_desk_id(desk_id=desk_id)


    def get_columns_by_column_id(self, column_id):
            return self.column_db.select_column_by_column_id(column_id)


    def add_column(self, desk_id, column_name):
        last_sequence_number = self.column_db.get_last_sequence_number_by_desk_id(desk_id=desk_id)

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
            columns_to_update = []
            self.column_db.del_column_by_column_id(column_id)
            deleted_column_id = zxc[1]  # desk_id удаленной строки, чтобы потом пересчитать sequence_number у этой доски
            columns = self.column_db.select_columns_by_desk_id(desk_id=deleted_column_id)

            for i in range(len(columns)):
                if columns[i][3] > zxc[3]:
                    self.column_db.update_any_info_about_column(columns[i][0], 'sequence_number', columns[i][3] - 1)
                    columns_to_update.append(columns[i])

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


    def change_column_sequence_number(self, column_id, new_sequence_number):
        return self.column_db.change_column_sequence_number(column_id, new_sequence_number)