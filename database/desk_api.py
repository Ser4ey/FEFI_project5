from database.desks import DesksDB


class DeskAPI:
    def __init__(self):
        self.desk_db = DesksDB()


    def get_desks(self):
        return self.desk_db.select_all_desks()


    def get_desk_by_id(self, desk_id):
        return self.desk_db.select_desk(id=desk_id)


    def add_desk(self, desk_name):
        try:
            self.desk_db.add_desk(name=desk_name)
            return True
        except:
            return False

    def del_desk_by_id(self, desk_id):
        return self.desk_db.del_desk(desk_id)


    def rename_desk(self, desk_id, new_name):
        existing_desk = self.desk_db.select_desk(id=desk_id)
        if existing_desk:
            try:
                self.desk_db.update_any_info_about_desk(desk_id, "name", new_name)
            except:
                return False

            return True
        else:
            return False