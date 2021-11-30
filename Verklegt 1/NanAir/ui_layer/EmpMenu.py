from logic_layer.LLAPI import LLAPI
from models.Employee import Employee

class EmpMenu:
    def __init__(self, llapi, user):
        self.user = user
        self.llapi = llapi
        self.header = """
      __|__                                                                                             __|__
*---o--(_)--o---*                                                                                 *---o--(_)--o---* 
___________________________________________________________________________________________________________________
|                                                                                                                 |
|   Home(home)   >Employee(emp)<    Real estate(real)    Cases(cases)    Contuctor(con)    Deestination(dest)     |
|_________________________________________________________________________________________________________________|
|                                                                                                                 |
|   s:              //Search for employee                       fi:         //Filter options                      |"""
        self.supervisorLine = """|   create:         //Creates new employee                      edit:       //Edit an existing employee           |"""

        self.footer = """|_________________________________________________________________________________________________________________|
"""
    def print_options(self):
        print(self.header)
        if self.user.is_supervisor():
            print(self.supervisorLine)
        print(self.footer)

    def draw_options(self):
        self.print_options()
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
            elif command == "r":
                return "r"
            elif command == "m":
                return "m"
            else:
                print("invalid option, try again!")
            print(self.options)

    def create_employee(self):
        name = input("Enter employee name: ")
        email = input("Enter employee email: ")
        phone = input("Enter employee phone: ")
        emp = Employee(name, email, phone)
        self.llapi.create_employee(emp)


