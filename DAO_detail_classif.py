class DAO_detail_classif:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def read_classifications(self):
        get_classifs = "SELECT * FROM classifications"
        query = self.db_connection.execute(get_classifs)
        classifications = []
        for c in query:
            classifications.append(c)
        return classifications
    
    def update_classifications(self, id_classif, upd):
        query = "UPDATE classifications SET desc = '%s' WHERE id = %d"\
                % (upd, id_classif)
        self.db_connection.execute(query)
        self.db_connection.commit()

    def delete_classification(self, id_classif):
        query = "DELETE FROM classifications WHERE id = %d ;" % (id_classif)
        self.db_connection.execute(query)
        self.db_connection.commit()

    def create_classification(self, classif):
        query_not_existing_table = "CREATE TABLE IF NOT EXISTS classifications("\
                            "id int PRIMARY KEY NOT NULL,"\
                            "desc TEXT NOT NULL);"

        self.db_connection.execute(query_not_existing_table)
        self.db_connection.commit()

        query_select_classif = self.db_connection.execute("SELECT id FROM classifications ORDER BY id DESC LIMIT 1;")

        last_id = None
        for row in query_select_classif:
            last_id = int(row[0])
            break
        if last_id != None:
            next_id = last_id + 1
        else:
            next_id = 0

        self.db_connection.execute("INSERT INTO classifications (id, desc) VALUES (?,?);", (next_id, classif.desc))
        self.db_connection.commit()