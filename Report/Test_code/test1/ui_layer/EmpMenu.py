from logic_layer.LLAPI import LLAPI
from models.Employee import Employee

# AVAILABLE_LOCATIONS = ["Reykjavík", "Nuuk", "Kulusuk", "Þórshöfn", "Tingwall", "Longyearbyen"]
EMP_ID = 'emp-'
SUP_ID = 'sup-'


class EmpMenu:
    def __init__(self, llapi):
        self.llapi = llapi
        self.options = """
Employee menu
1 - list all employees
2 - create a new employee
3 - edit employee(by id number)
4 - search employee
r - return to previous menu
"""

    def draw_options(self):
        print(self.options)
        return self.prompt_input()

# ------------------------------------------------------------------------------------------------------------------
# Menu Options
    def prompt_input(self):
        while True:
            command = input("Enter your input: ")
            if command == "1": self.filter_by_location()
            elif command == "2": self.create_employee()
            elif command == "3": self.edit_employee()
            elif command == "4": self.search_employee()
            elif command == "r": return "r"
            else: print("invalid option, try again!")
            print(self.options)
# ------------------------------------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------------------------------------
# input parameters and checks
    def input_and_check(self, info_type, check_fun):
        while True:
            value = input(f"Enter employee {info_type}: ")
            if not check_fun(value): print(f"Invalid employee {info_type}")
            else: return value

    def available_locations(self):
        while True:
            print('Available locations to choose from: \n')
            for location in self.llapi.get_locations_name():
                print(location)
            print()
            location = str(input("Enter location: ")).lower().capitalize()
            if location not in self.llapi.get_locations_name():
                print("Invalid location")
            else:
                return location

    def make_emp_or_sup_id(self, check, location):
        while True:
            all_id = self.llapi.all_employees()
            emp_or_sup = input("Make employee or supervisor(e/s): ").lower()
            if emp_or_sup == "e":
                id = EMP_ID + str(len(all_id) + 1).zfill(4)
                return id
            elif emp_or_sup == "s":
                if check == "True":
                    id = SUP_ID + str(len(all_id) + 1).zfill(4)
                    return id
                else: print(f"Invalid ther is alredy a supervisor in {location}")

    def user_options(self, controller):
        location = self.available_locations()
        check = self.llapi.check_location_append_to_list(location)
        id = self.make_emp_or_sup_id(check, location)
        name = self.input_and_check("name", lambda value : self.llapi.is_name_correct(value))
        phone = self.input_and_check("phone", lambda value : self.llapi.is_phone_correct(value))
        address = self.input_and_check("address", lambda value : self.llapi.is_address_correct(value))
        homeline = self.input_and_check("homeline", lambda value : self.llapi.is_phone_correct(value))
        return name, phone, id, address, homeline, location
# ------------------------------------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------------------------------------
# Create Employee
    def create_employee(self):
        print("Welcome to the creation kit!")
        print("Quit by entering (q): ")
        name, phone, id, address, homeline, location = self.user_options("create")
        if name != None and phone != None and id != None and address != None and homeline != None and location != None:
            emp = Employee(name, id, address, homeline, location, phone)
            self.llapi.create_employee(emp)
# ------------------------------------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------------------------------------
# Edit Employee
    def print_emp_as_menu(self, emp):
        edit_options = f"""
        Employee {emp.id}

        1 - Name: {emp.name}
        2 - Address: {emp.address}
        3 - Homeline: {emp.homeline}
        4 - Phone: {emp.phone}
        5 - Location: {emp.location}
        r - return to previous menu
        """
        print(edit_options)

    def edit_employee(self):
        #check if id is len 4
        print("Quit by entering (q)")
        while True:
            edit_id = str(input("Enter employee id: "))
            if edit_id != "q":
                emp = self.llapi.search_employee(edit_id)
                if emp == None: 
                    print("The employee id was not found")
                else: 
                    self.promt_edit(emp)
                    return
            else: return

    def promt_edit(self, emp):
        while True:
            self.print_emp_as_menu(emp)
            command = input("Enter edit option: ")
            
            if command == "1":
                emp.name = self.input_and_check("name", lambda value : self.llapi.is_name_correct(value))
                self.llapi.edit_employee(emp)
            elif command == "2":
                emp.address = self.input_and_check("address", lambda value : self.llapi.is_address_correct(value))
                self.llapi.edit_employee(emp)
            elif command == "3":
                emp.homeline = self.input_and_check("homeline", lambda value : self.llapi.is_phone_correct(value))
                self.llapi.edit_employee(emp)
            elif command == "4":
                emp.phone = self.input_and_check("phone", lambda value : self.llapi.is_phone_correct(value))
                self.llapi.edit_employee(emp)
            elif command == "5":
                emp.location = self.available_locations()
                self.llapi.edit_employee(emp)
            elif command == "r":
                return
            else:
                print("Invalid option")
# ------------------------------------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------------------------------------
# Filters by the employee location
    def filter_by_location(self):
                all_emps = self.llapi.all_employees()
                for emp in all_emps: 
                    print(emp)
                filter_input = input("Do you want to filter by location(y/n)?: ")
                if filter_input == 'y':
                    location = self.available_locations()
                    result = LLAPI().filter_employee(location)
                    for row in result:
                        print(row)
# ------------------------------------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------------------------------------
# Search for employee by ther id
    def search_employee(self):
        while True:
            print("Quit by entering (q)")
            search_id = input("Enter employee id: ")
            if search_id.lower() != "q":
                result = LLAPI().search_employee(search_id)
                print(result)
            else: break
# ------------------------------------------------------------------------------------------------------------------
