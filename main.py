from sys import exit

from bill import Bill
from DAO_bill import DAO_bill
from DAO_detail_classif import DAO_detail_classif
from DAO_detail import DAO_detail
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
        todo = input("What do you want to do?: ")
        if todo == "1": Users(database)
        elif todo == "2": Classifications(database)
        elif todo == "3": Details(database)
        elif todo == "4": Bills(database)
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
        todo = input("What do you want to do? ")

        if todo == "1":
            name = input("Name: ")
            lastname = input("Lastname: ")
            gender = input("Gender: ")
            bd = input("Date of birth: ")
            civilStatus = input("Civil status: ")
            new_user = User(name, lastname, gender, bd, civilStatus)
            self.daouser.create_user(new_user)
            self.printAllUsers()
        elif todo == "2":
            self.printAllUsers()
            id_user = int(input("Enter id of customer you want to update: "))
            column = int(input("Enter column to update: 0 (Name), 1 (Lastname), 2 (Gender), 3 (Date of birth), 4 (Civil status): "))
            upd = input("What is the new value you want to give to it? ")
            self.daouser.update_user(id_user, column, upd)
            print("User updated successfully")
        elif todo == "3":
            self.printAllUsers()
            to_delete = int(input("Enter id of customer to delete: "))
            self.daouser.delete_user(to_delete)
            print("User deleted successfully")
        elif todo == "4": self.printAllUsers()
        else: print("Please enter valid option")
        
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
        todo = input("What do you want to do? ")
        if todo == "1":
            desc = input("Description: ")
            new_classif = Details_classif(desc)
            self.daoclassif.create_classification(new_classif)
            self.printAllClassifs()
        elif todo == "2":
            self.printAllClassifs()
            id_classif = int(input("Enter id of classification you want to update: "))
            upd = input("Enter new description: ")
            self.daoclassif.update_classifications(id_classif, upd)
            print("Classification updated successfully ")
        elif todo == "3":
            self.printAllClassifs()
            to_delete = int(input("Enter id of classification to delete: "))
            self.daoclassif.delete_classification(to_delete)
            print("Classification deleted successfully ")
        elif todo == "4": self.printAllClassifs()
        else: print("Please enter valid option ")

    def printAllClassifs(self):
        table = PrettyTable(["Id", "Description"])
        classifs = self.daoclassif.read_classifications()
        for c in classifs:
            table.add_row(c)
        print(table)

class Details:
    def __init__(self, db_connection):
        self.daodetails = DAO_detail(db_connection)
        self.detailsSect()

    def detailsSect(self):
        print("What you can do: \n \
              1. Create new item \n \
              2. Update item \n \
              3. Delete item \n \
              4. Watch all items")
        todo = input("What do you want to do? ")
        if todo == "1":
            detail_type = int(input("Item type: "))
            desc = input("Description: ")
            cost = int(input("Cost: "))
            new_detail = Detail(detail_type, desc, cost)
            self.daodetails.create_detail(new_detail)
            self.printAllDetails()
        elif todo == "2":
            self.printAllDetails()
            id_detail = int(input("Enter id of detail you want to update"))
            column = ("Enter column to change: 0 (Type), 1 (Description), 2 (Cost): ")
            upd = input("What is the new value you want to give to it?: ")
            self.daodetails.update_details(id_detail, column, upd)
            print("Detail updated successfully")
        elif todo == "3":
            self.printAllDetails()
            to_delete = int(input("Enter id of detail to delete: "))
            self.daodetails.delete_detail(to_delete)
            print("Detail deleted successfully ")
        elif todo == "4": self.printAllDetails
        else: print("Please enter valid option ")

    def printAllDetails(self):
        table = PrettyTable(["Id", "Type", "Description", "Cost"])
        details = self.daodetails.read_details()
        for d in details:
            table.add_row(d)
        print(table)


class Bills:
    def __init__(self, db_connection):
        self.daobill = DAO_bill(db_connection)
        self.billsSect()

    def billsSect(self):
        print("What you can do: \n \
              1. Create new bill \n \
              2. Update bill \n \
              3. Delete bill \n \
              4. Watch all bills")
        todo = input("What do you want to do? ")
        if todo == "1":
            date = input("Date: ")
            user = input("Customer id: ")
            status = input("Status: ")
            details = input("Number of details ")
            dets = ""
            for d in range(int(details)):
                helper = input("Enter detail id: ") + "-"
                dets += helper
            new_bill = Bill(date, user, status, dets)
            self.daobill.create_bill(new_bill)
            self.printAllBills()
        elif todo == "2":
            self.printAllBills()
            id_bill = int(input("Enter id of bill you want to update "))
            column = int(input("Enter column to change: 0 (Date), 1 (Customer),\
                 2 (Status), 3 (Cost), 4 (Details): "))
            if column == "4":
                details = int(input("Number of items you are going to add: "))
                dets = ""
                for d in range(details):
                    helper = input("Enter detail id ")
                    dets += helper
                    if d != details - 1:
                        dets += "-"
                upd = dets
            else: upd = input("What is the new value you want to give to it?: ")
            self.daobill.update_bill(id_bill, column, upd)
            print("Bill updated successfully ")
        elif todo == "3":
            self.printAllBills()
            to_delete = int(input("Enter id of bill to delete "))
            self.daobill.delete_bill(to_delete)
            print("Bill deleted successfully ")
        elif todo == "4": self.printAllBills()
        else: print("Please enter valid option")

    def printAllBills(self):
        table = PrettyTable(["Id bill", "Date", "Id Customer", "Status", "Cost", "Id Details"])
        bills = self.daobill.read_bills()
        for b in bills:
            table.add_row(b)
        print(table)

if __name__ == '__main__':
    main()