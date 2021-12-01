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

    def create_employee(self):
        name = input("Enter employee name: ")
        email = input("Enter employee email: ")
        phone = input("Enter employee phone: ")
        id = input("Enter employee id: ")
        address = input("Enter employee address: ")
        homeline = input("Enter employee homeline: ")
        location = input("Enter employee location: ")

        emp = Employee(name, id, address, homeline, email, location, phone)
        self.llapi.create_employee(emp)

    def edit_employee(self):
        edit_id = str(input("Enter employee id: "))

        print(f"you are editing a employee with the id: {edit_id}")
        print("You can't delete the employee id.\n")
        name = str(input("Enter employee name: "))
        email = str(input("Enter employee email: "))
        phone = str(input("Enter employee phone: "))
        address = str(input("Enter employee address: "))
        homeline = str(input("Enter employee homeline: "))
        location = str(input("Enter employee location: "))

        emp = Employee(name, edit_id, address, homeline, email, location, phone)        
        self.llapi.edit_employee(emp)


