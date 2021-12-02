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
            elif command == "r":
                return "r"
            else:
                print("invalid option, try again!")
            print(self.options)

    def user_options(self, controller):
        name = input("Enter employee name: ")
        name_c = self.llapi.check_if_name_correct(name)
        if name_c == False:
            print("invalid employee name")
            self.user_options(controller)
#----
        phone = input("Enter employee phone: ")
        phone_c = self.llapi.check_if_phone_correct(phone)
        if phone_c == False:
            print("invalid employee phone")
            self.user_options(controller)
#----
        if controller == "create": 
            id = input("Enter employee id: ")
            id_c = self.llapi.check_if_id_correct(id)
            if id_c == False:
                print("Invalid employee id")
                self.user_options(controller)
        else: id == None
#----
        address = input("Enter employee address: ")
        address_c = self.llapi.check_if_address_correct(address)
        homeline = input("Enter employee homeline: ")
        location = input("Enter employee location: ")
        return name, email, phone, id, address, homeline, location

    def create_employee(self):
        name, email, phone, id, address, homeline, location = user_options("create")
        emp = Employee(name, id, address, homeline, email, location, phone)
        self.llapi.create_employee(emp)

    def edit_employee(self):
        #check if id is len 4
        while True:
            
            edit_id = str(input("Enter employee id: "))
            id_c = self.llapi.check_if_id_correct(edit_id)
            if id_c == False:
                print("Invalid employee id(id is 4 number long)")
            else: break

        ready_to_continue = self.llapi.check_if_employee_exists(edit_id)
        if ready_to_continue:
            name, email, phone, id, address, homeline, location = self.user_options(None)
            emp = Employee(name, edit_id, address, homeline, email, location, phone)        
            self.llapi.edit_employee(emp)
        else:
            print("The employee id was not found")
            print(self.options)



