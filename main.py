from sys import exit

from bill import Bill
from DAO_bill import DAO_bill
from DAO_detail_classif import DAO_detail_classif
from DAO_user import DAO_user
from db_connect import DB_connection
from detail_classif import Details_classif
from detail import Detail
from user import User

from prettytable import PrettyTable

def main():
    DB_connection()
    database = DB_connection.getConnection().connection

    while True:
        print("What you can do: \n \
            1. Customers\n \
            2. Item classifications \n \
            3. Items \n \
            4. Bill \n \
            5. Finish")
        todo = input("What do you want to do?:")
        if todo == "1": Users(database)
        elif todo == "2": Classifications(database)
        elif todo == "3": details(database)
        elif todo == "4": bills(database)
        elif todo == "5": exit()
        else: print("Please enter valid option ")

class Users:
    def __init__(self, db_connection):
        self.daouser = DAO_user(db_connection)
        self.userSect()

    def userSect(self):
        print("What you can do: \n \
              1. Create new customer \n \
              2. Update customer \n \
              3. Delete customer \n \
              4. Watch all customers")
        todo = input("What do you want to do?")

        if todo == "1":
            name = input("Name: ")
            lastname = input("Lastname: ")
            gender = input("Gender: ")
            bd = input("Birth date: ")
            civilStatus = input("Civil status: ")
            new_user = User(name, lastname, gender, bd, civilStatus)
            self.daouser.create_user(new_user)
            self.printAllUsers()
        elif todo == "2":
            self.printAllUsers()
            id_user = int(input("Enter id of customer you want to update: "))
            column = int(input("Enter column to update: 0 (Name), 1 (Lastname),\
                 2 (Gender), 3 (Date of birth), 4 (Civil status): "))
            upd = input("What is the new value you want to give to it? ")
            self.daouser.update_user(id_user, column, upd)
            print("User updated successfully")
        elif todo == "3":
            self.printAllUsers()
            to_delete = int(input("Enter id of customer to delete: "))
            self.daouser.delete_user(to_delete)
            print("User deleted successfully")
        elif todo == "4":
            self.printAllUsers()
        else:
            print("Please enter valid option")
        
    
    def printAllUsers(self):
        table = PrettyTable(["Id", "Name", "Lastname", "Gender", "Date of birth", "Civil status"])
        all_users = self.daouser.read_users()
        for u in all_users:
            table.add_row(u)
        print(table)
    

class Classifications:
    def __init__(self, db_connection):
        self.daoclassif = DAO_detail_classif(db_connection)
        self.classifSect()
    
    def classifSect(self):
        print("What you can do: \n \
              1. Create new classification \n \
              2. Update classification \n \
              3. Delete classification \n \
              4. Watch all classifications")
        todo = input("What do you want to do?")
        if todo == "1":
            desc = input("Description: ")
            new_classif = Details_classif(desc)
            self.daoclassif.create_classification(new_classif)
            self.printAllClassifs()
        elif todo == "2":
            self.printAllClassifs()
            id_classif = int(input("Enter id of classification you want to update: "))
            upd = input("Enter new description ")
            self.daoclassif.update_classifications(id_classif, upd)
            print("Classification updated successfully")
        elif todo == "3":
            self.printAllClassifs()
            to_delete = int(input("Enter id of classification to delete: "))
            self.daoclassif.delete_classification(to_delete)
            print("Classification deleted successfully")
    
    def printAllClassifs(self):
        pass

def details(db_conn):
    pass

def bills(db_conn):
    pass

if __name__ == '__main__':
    main()