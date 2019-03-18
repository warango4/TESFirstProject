class DAO_detail:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def read_details(self):
        get_details = "SELECT * FROM details ORDERED BY type ASC;"
        query = self.db_connection.execute(get_details)
        details = []
        for d in query:
            details.append(d)
        return details

    def update_details(self, id_detail, column, upd):
        if column == 0:
            col = "type"
        elif column == 1:
            col = "desc"
        elif column == 2:
            col = "cost"
            upd = int(upd)
        upd_detail = "UPDATE details SET %s = %s WHERE id = %d ;" % (col, upd, id_detail)

        self.db_connection.execute(upd_detail)
        self.db_connection.commit()

    def delete_detail(self, id_detail):
        query_delete_detail = "DELETE FROM details WHERE id = %d ;" % (id_detail)
        self.db_connection.execute(query_delete_detail)
        self.db_connection.commit()

    def create_detail(self, detail):
        self.db_connection.execute("PRAGMA foreign_keys = ON;")
        query_not_existing_table = "CREATE TABLE IF NOT EXISTS details("\
                            "id int PRIMARY KEY NOT NULL,"\
                            "type int TEXT NOT NULL,"\
                            "desc TEXT NOT NULL, cost int NOT NULL,"\
                            "FOREIGN KEY (type) REFERENCES classifications(id));"

        self.db_connection.execute(query_not_existing_table)
        self.db_connection.commit()

        query = self.db_connection.execute("SELECT id FROM details ORDER BY id \
                                DESC LIMIT 1;")

        last_id = None
        for row in query:
            last_id = int(row[0])
            break
        if last_id != None:
            next_id = last_id + 1
        else:
            next_id = 0

        self.db_connection.execute("INSERT into details (id, type, desc, cost) VALUES (?, ?, ?, ?);",\
            (next_id, detail.type, detail.desc, detail.cost))
        self.db_connection.commit()