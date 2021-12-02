from logic_layer.LLAPI import LLAPI
from models.Employee import Employee

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

    def user_options(self, controller):
        while True:
            name = input("Enter employee name: ")
            name_c = self.llapi.check_if_name_correct(name)
            if name_c == False:
                print("invalid employee name")
            else: break
#----
        while True:
            phone = input("Enter employee phone: ")
            phone_c = self.llapi.check_if_phone_correct(phone)
            if phone_c == False:
                print("invalid employee phone")
            else: break
#----
        if controller == "create": 
            while True:
                id = input("Enter employee id: ")
                id_c = self.llapi.check_if_id_correct(id)
                if id_c == False:
                    print("Invalid employee id")
                else: break
        else: id = None
#----
        while True:
            address = input("Enter employee address: ")
            address_c = self.llapi.check_if_address_correct(address)
            if address_c == False:
                print("Invalid employee address")
            else: break
#----
        while True:
            homeline = input("Enter employee homeline: ")
            homeline_c = self.llapi.check_if_phone_correct(homeline)
            if homeline_c == False:
                print("invalid employee homeline")
            else: break
#----
        while True:
            location = input("Enter employee location: ")
            location_c = self.llapi.check_if_location_correct(location)
            if location_c == False:
                print("invalid employee location")
            else: break
#----
        return name, phone, id, address, homeline, location

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
        result = LLAPI.search_employee(search_id)
        print(result)
