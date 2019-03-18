# Data access object pattern
# To separate business layer from persistence layer 

class DAO_user:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def read_users(self):
        get_users = "SELECT * FROM users"
        query = self.db_connection.execute(get_users)
        users = []
        for c in query:
            users.append(c)
        return users

    def update_user(self, id_user, column, upd):
        stringCol = ""
        if column == 0:
            stringCol = "name"
        elif column == 1:
            stringCol = "lastname"
        elif column == 2:
            stringCol = "gender"
        elif column == 3:
            stringCol = "bd"
        else:
            stringCol = "civilStatus"
        query = "update users SET %s = '%s' WHERE id = %d" % (stringCol, upd, id_user)
        self.db_connection.execute(query)
        self.db_connection.commit()

    def delete_user(self, id_user):
        query_delete_user = "DELETE FROM users WHERE id = %d ;" % (id_user)
        self.db_connection.execute(query_delete_user)
        self.db_connection.commit()

    def create_user(self, user):
        query_not_existing_table = "CREATE TABLE IF NOT EXISTS users("\
                            "id int PRIMARY KEY NOT NULL,"\
                            "name TEXT NOT NULL, lastname TEXT NOT NULL,"\
                            "gender TEXT NOT NULL, bd TEXT NOT NULL,"\
                            "civilStatus TEXT NOT NULL);"
        self.db_connection.execute(query_not_existing_table)
        self.db_connection.commit()

        cursor = self.db_connection.execute("SELECT id FROM users ORDER BY id DESC LIMIT 1;")

        last_id = None

        for row in cursor:
            last_id = int(row[0])
            break
        if last_id != None:
            next_id = last_id + 1
        else:
            next_id = 0    

        self.db_connection.execute("INSERT INTO users (id, name, lastname, gender, \
                        bd, civilStatus) VALUES (?,?,?,?,?,?);" , (next_id,
                        user.name, user.lastname, user.gender, user.bd,
                        user.civilStatus))
        self.db_connection.commit()

