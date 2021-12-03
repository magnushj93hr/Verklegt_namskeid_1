from logic_layer.LLAPI import LLAPI
from models.Employee import Employee

AVAILABLE_LOCATIONS = ["Reykjavík", "Nuuk", "Kulusuk", "Þórshöfn", "Tingwall", "Longyearbyen" ]

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

    def prompt_input(self):
        while True:
            command = input("Enter your input: ")
            if command == "1":
                all_emps = self.llapi.all_employees()
                for emp in all_emps:
                    print(emp)
                filter_input = input("Do you want to filter by location(y/n)?: ")
                if filter_input == 'y':
                    filter_location = input('Enter location to filter by: ')
                    result = LLAPI().filter_employee(filter_location)
                    for row in result:
                        print(row)
            elif command == "2":
                self.create_employee()
            elif command == "3":
                self.edit_employee()
            elif command == "4":
                self.search_employee()
            elif command == "r":
                return "r"
            else:
                print("invalid option, try again!")
            print(self.options)

# ------------------------------------------------------------------------------------------------------------------
    def input_and_check(self, info_type, check_fun):
        while True:
            value = input(f"Enter employee {info_type}: ")
            if not check_fun(value): print(f"Invalid employee {info_type}")
            else: return value

    def user_options(self, controller):
        name = self.input_and_check("name", lambda value : self.llapi.is_name_correct(value))
        phone = self.input_and_check("phone", lambda value : self.llapi.is_phone_correct(value))
        id = self.input_and_check("id", lambda value : self.llapi.is_id_correct(value)) if controller == "create" else None
        address = self.input_and_check("address", lambda value : self.llapi.is_address_correct(value))
        homeline = self.input_and_check("homeline", lambda value : self.llapi.is_phone_correct(value))
#----
        while True:
            print('Available locations to choose from:')
            for location in AVAILABLE_LOCATIONS:
                print(location)
            location = str(input("Enter location: "))
            if location in AVAILABLE_LOCATIONS:
                break

        return name, phone, id, address, homeline, location
# ------------------------------------------------------------------------------------------------------------------

    def create_employee(self):
        name, phone, id, address, homeline, location = self.user_options("create")
        emp = Employee(name, id, address, homeline, location, phone)
        self.llapi.create_employee(emp)

    def edit_employee(self):
        #check if id is len 4
        edit_id = str(input("Enter employee id: "))

        ready_to_continue = self.llapi.check_if_employee_exists(edit_id)
        if ready_to_continue == True:
            name, phone, id, address, homeline, location = self.user_options(None)
            emp = Employee(name, edit_id, address, homeline, location, phone)        
            self.llapi.edit_employee(emp)
        else:
            print("The employee id was not found")
            print(self.options) 
    
    def search_employee(self):
        search_id = input("Enter employee id: ")
        result = LLAPI().search_employee(search_id)
        print(result)
