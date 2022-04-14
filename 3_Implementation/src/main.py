""" imported csv file from local storage """
import csv

# Define global variables
INTERN_FIELDS = ['psnumber', 'name', 'age', 'email', 'phone']
INTERN_ATTEN = ['psnumber', 'name']
INTERN_DATABASE = 'intern.csv'
INTERN_ATTENDANCE = 'attendance.csv'


class Menu:

    @staticmethod
    def display_menu():
        """ this function tells about first menu """

        print("--------------------------------------")
        print(" Welcome to L&T Intern Management System")
        print("---------------------------------------")
        print("1. Intern")
        print("2. Employee")
        print("3. Exit")
        print("---------------------------------------")

    @staticmethod
    def display_menu1():
        """ student menu """
        print("1. Attendance")
        print("2. Quit")

    @staticmethod
    def display_menu2():
        """ employee menu """
        print("1. Add New Intern")
        print("2. View Intern")
        print("3. Search Intern")
        print("4. Update Intern")
        print("5. Delete Intern")
        print("6. View Attendance")
        print("7. Quit")


obj3 = Menu()


class Employee:

    @staticmethod
    def login():
        """ login details """
        print("------------------------")
        print("Enter your user id(admin) : ")
        user = input().lower()
        print("Enter password please(1234) :")
        password = int(input())
        print("------------------------")
        if user == "admin" and password == 1234:
            return obj3.display_menu2()
        else:
            print("Please enter correct userid/password")
        print("------------------------")

    @staticmethod
    def view_interns():
        """ View intern details """
        global INTERN_FIELDS
        global INTERN_DATABASE

        print("\n--- Intern Records ---")

        with open(INTERN_DATABASE, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            for x in INTERN_FIELDS:
                print(x, end="\t | \t")
            print("\n-----------------------------------------------------------------")

            for row in reader:
                for item in row:
                    print(item, end="\t | \t")
                print("\n")

        input("Press any key to continue")

    @staticmethod
    def update_intern():
        """ Update Intern details """
        global INTERN_FIELDS
        global INTERN_DATABASE

        print("--- Update intern ---")
        psnumber = input("Enter psnumber to update: ")
        index_intern = None
        updated_data = []
        with open(INTERN_DATABASE, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            counter = 0
            for row in reader:
                if len(row) > 0:
                    if psnumber == row[0]:
                        index_intern = counter
                        print("intern Found: at index ", index_intern)
                        intern_data = []
                        for field in INTERN_FIELDS:
                            value = input("Enter " + field + ": ")
                            intern_data.append(value)
                        updated_data.append(intern_data)
                    else:
                        updated_data.append(row)
                    counter += 1

        # Check if the record is found or not
        if index_intern is not None:
            with open(INTERN_DATABASE, "w", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerows(updated_data)
        else:
            print("psnumber not found in our database")

        input("Press any key to continue")

    @staticmethod
    def delete_intern():
        """ Delete Intern Details """
        global INTERN_FIELDS
        global INTERN_DATABASE

        print("--- Delete intern ---")
        psnumber = input("Enter psnumber to delete: ")
        intern_found = False
        updated_data = []
        with open(INTERN_DATABASE, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            counter = 0
            for row in reader:
                if len(row) > 0:
                    if psnumber != row[0]:
                        updated_data.append(row)
                        counter += 1
                    else:
                        intern_found = True

        if intern_found is True:
            with open(INTERN_DATABASE, "w", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerows(updated_data)
            print("psnumber  ", psnumber, "deleted successfully")
        else:
            print("psnumber not found in our database")

        input("Press any key to continue")

    @staticmethod
    def view_attendance():
        """ To View Attendance """
        global INTERN_ATTEN
        global INTERN_ATTENDANCE

        print("--- Attendance Records ---")

        with open(INTERN_ATTENDANCE, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            for y in INTERN_ATTEN:
                print(y, end='\t |')
            print("\n---------------------------")

            for row in reader:
                for item in row:
                    print(item, end="\t |")
                print("\n")

        input("Press any key to continue")

    @staticmethod
    def search_intern():
        """ Searching Intern details """
        global INTERN_FIELDS
        global INTERN_DATABASE

        print("--- Search intern ---")
        psnumber = input("Enter psnumber to search: ")
        with open(INTERN_DATABASE, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) > 0:
                    if psnumber == row[0]:
                        print("----- intern Found -----")
                        print("psnumber: ", row[0])
                        print("Name: ", row[1])
                        print("Age: ", row[2])
                        print("Email: ", row[3])
                        print("Phone: ", row[4])
                        break
            else:
                print("psnumber not found in our database")
        input("Press any key to continue")

    @staticmethod
    def add_intern():
        """ Adding new intern Details """
        print("-------------------------")
        print("Add Intern Information")
        print("-------------------------")
        global INTERN_FIELDS
        global INTERN_DATABASE

        intern_data = []
        for field in INTERN_FIELDS:
            value = input("Enter " + field + ": ")
            intern_data.append(value)

        with open(INTERN_DATABASE, "a", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerows([intern_data])

        print("Data saved successfully")
        input("Press any key to continue")
        return


obj1 = Employee()


class Intern:

    @staticmethod
    def attendance_intern():
        """ To Mark Attendance of Intern """
        print("-------------------------")
        print(" Mark your attendance ")
        print("-------------------------")
        global INTERN_ATTEN
        global INTERN_ATTENDANCE

        intern_data = []
        for field in INTERN_ATTEN:
            value = input("Enter " + field + ": ")
            intern_data.append(value)

        with open(INTERN_ATTENDANCE, "a", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerows([intern_data])

        print("Data saved successfully")
        input("Press any key to continue")
        return


obj2 = Intern()

while True:
    obj3.display_menu()
    choice = input("Enter your choice: ")
    if choice == '1':
        obj3.display_menu1()
        choice = input("Enter your choice: ")
        if choice == '1':
            obj2.attendance_intern()
        else:
            break
    elif choice == '2':
        obj1.login()
        choice = input("Enter your choice: ")
        if choice == '1':
            obj1.add_intern()
        elif choice == '2':
            obj1.view_interns()
        elif choice == '3':
            obj1.search_intern()
        elif choice == '4':
            obj1.update_intern()
        elif choice == '5':
            obj1.delete_intern()
        elif choice == '6':
            obj1.view_attendance()
        else:
            break
    elif choice == '3':
        exit()
    else:
        break

print("------------------------------------")
print(" Thank you for using our L&T system ")
print("------------------------------------")
