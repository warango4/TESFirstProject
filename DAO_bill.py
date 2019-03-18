class DAO_bill:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def read_bills(self):
        get_bills = "SELECT * FROM bills;"
        query = self.db_connection.execute(get_bills)
        bills = []
        for b in query:
            bills.append(b)
        return bills
    
    def update_bill(self, id_bill, column, upd):
        upd_detail = 0
        if column == 0:
            col = "date"
        elif column == 1:
            col = "user"
            upd = int(upd)
        elif column == 2:
            col = "status"
        elif column == 3:
            col = "cost"
        elif column == 4:
            col = "details"
            upd_detail = 1
        
        query_update = "UPDATE bills SET %s = '%s' WHERE id = %d" % (col, upd, id_bill)

        if upd_detail == 1:
            cost = 0
            details = upd.split(" ")
            for d in details:
                query_get_details = "SELECT cost FROM details WHERE id = %s " % (d)
                cursor = self.db_connection.execute(query_get_details)
                for row in cursor:
                    cost += int(row[0])
                    break
            
            upd_cost = ("UPDATE bills SET cost = '%d' WHERE id = %d" % (cost, id_bill))
            self.db_connection.execute(upd_cost)
            self.db_connection.commit()

        self.db_connection.execute(query_update)
        self.db_connection.commit()

    def delete_bill(self, id_bill):
        query_delete_bill = "DELETE FROM bills WHERE id = %d ;" % (id_bill)
        self.db_connection.execute(query_delete_bill)
        self.db_connection.commit()

    def create_bill(self, bill):
        self.db_connection.execute("PRAGMA foreign_keys = ON;")
        query_not_existing_table = "CREATE TABLE IF NOT EXISTS bills("\
                            "id int PRIMARY KEY NOT NULL, "\
                            "date TEXT NOT NULL, user int NOT NULL, "\
                            "status TEXT NOT NULL, cost int NOT NULL, "\
                            "details text NOT NULL, "\
                            "FOREIGN KEY (user) REFERENCES user(id));"
        self.db_connection.execute(query_not_existing_table)
        self.db_connection.commit()
        query = self.db_connection.execute("SELECT id FROM bills ORDER BY id DESC LIMIT 1;")
        last_id = None
        for row in query:
            last_id = int(row[0])
            break
        if last_id != None: id_bill = last_id + 1
        else: id_bill = 0
        
        cost = 0
        details = bill.details.split("-")
        for d in details:
            if len(d) > 0:
                query_detail = "SELECT cost FROM details WHERE id = %s;" % (d)
                cursor = self.db_connection.execute(query_detail)
                for row in cursor:
                    cost += int(row[0])
                    break
        
        self.db_connection.execute("INSERT INTO bills (id, date, user, status, cost, details) \
            VALUES (?, ?, ?, ?, ?, ?);", (id_bill, bill.date, bill.user, bill.status, cost, bill.details))
        self.db_connection.commit()
