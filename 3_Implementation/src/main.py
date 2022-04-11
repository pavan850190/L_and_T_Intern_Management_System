import csv

# Define global variables
intern_fields = ['psnumber', 'name', 'age', 'email', 'phone']
intern_atten = ['psnumber', 'name']
intern_database = 'intern.csv'
intern_attendance = 'attendance.csv'


def display_menu():
    print("--------------------------------------")
    print(" Welcome to L&T Intern Management System")
    print("---------------------------------------")
    print("1. Intern")
    print("2. Employee")
    print("---------------------------------------")


def display_menu1():
    print("1. Attendance")
    print("2. Quit")


def display_menu2():
    print("1. Add New Intern")
    print("2. View Intern")
    print("3. Search Intern")
    print("4. Update Intern")
    print("5. Delete Intern")
    print("6. View Attendance")
    print("7. Quit")


class employee:

    def add_intern(self):
        print("-------------------------")
        print("Add Intern Information")
        print("-------------------------")
        global intern_fields
        global intern_database

        intern_data = []
        for field in intern_fields:
            value = input("Enter " + field + ": ")
            intern_data.append(value)

        with open(intern_database, "a", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows([intern_data])

        print("Data saved successfully")
        input("Press any key to continue")
        return

    def view_interns(self):
        global intern_fields
        global intern_database

        print("--- Intern Records ---")

        with open(intern_database, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            for x in intern_fields:
                print(x, end='\t |')
            print("\n-----------------------------------------------------------------")

            for row in reader:
                for item in row:
                    print(item, end="\t |")
                print("\n")

        input("Press any key to continue")

    def search_intern(self):
        global intern_fields
        global intern_database

        print("--- Search intern ---")
        psnumber = input("Enter psnumber no. to search: ")
        with open(intern_database, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
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
                print("psnumber No. not found in our database")
        input("Press any key to continue")

    def update_intern(self):
        global intern_fields
        global intern_database

        print("--- Update intern ---")
        psnumber = input("Enter psnumber no. to update: ")
        index_intern = None
        updated_data = []
        with open(intern_database, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            counter = 0
            for row in reader:
                if len(row) > 0:
                    if psnumber == row[0]:
                        index_intern = counter
                        print("intern Found: at index ", index_intern)
                        intern_data = []
                        for field in intern_fields:
                            value = input("Enter " + field + ": ")
                            intern_data.append(value)
                        updated_data.append(intern_data)
                    else:
                        updated_data.append(row)
                    counter += 1

        # Check if the record is found or not
        if index_intern is not None:
            with open(intern_database, "w", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerows(updated_data)
        else:
            print("psnumber No. not found in our database")

        input("Press any key to continue")

    def delete_intern(self):
        global intern_fields
        global intern_database

        print("--- Delete intern ---")
        psnumber = input("Enter psnumber no. to delete: ")
        intern_found = False
        updated_data = []
        with open(intern_database, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            counter = 0
            for row in reader:
                if len(row) > 0:
                    if psnumber != row[0]:
                        updated_data.append(row)
                        counter += 1
                    else:
                        intern_found = True

        if intern_found is True:
            with open(intern_database, "w", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerows(updated_data)
            print("psnumber no. ", psnumber, "deleted successfully")
        else:
            print("psnumber No. not found in our database")

        input("Press any key to continue")

    def view_attendance(self):
        global intern_atten
        global intern_attendance

        print("--- Attendance Records ---")

        with open(intern_attendance, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            for y in intern_atten:
                print(y, end='\t |')
            print("\n---------------------------")

            for row in reader:
                for item in row:
                    print(item, end="\t |")
                print("\n")

        input("Press any key to continue")


obj1 = employee()


class intern():

    def attendance_intern(self):
        print("-------------------------")
        print("Mark your attendance")
        print("-------------------------")
        global intern_atten
        global intern_attendance

        intern_data = []
        for field in intern_atten:
            value = input("Enter " + field + ": ")
            intern_data.append(value)

        with open(intern_attendance, "a", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows([intern_data])

        print("Data saved successfully")
        input("Press any key to continue")
        return


obj2 = intern()

while True:
    display_menu()
    choice = input("Enter your choice: ")
    if choice == '1':
        display_menu1()
        choice = input("Enter your choice: ")
        if choice == '1':
            obj2.attendance_intern()
        else:
            break
    elif choice == '2':
        display_menu2()
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
    else:
        break

print("-------------------------------")
print(" Thank you for using our L&T system")
print("-------------------------------")
