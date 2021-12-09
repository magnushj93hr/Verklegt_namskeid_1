from ui_layer.Employee.create_emp import CreateEmp
from logic_layer.LLAPI import LLAPI
from models.Employee import Employee
from ui_layer.Employee.search_emp import SearchEmp


class EmpMenu:
    def __init__(self, llapi, user):
        self.user = user
        self.llapi = llapi
        # self.create_emp = CreateEmp()
        self.search_emp = SearchEmp(llapi)
        self.header = """
      __|__                                                                                             __|__
*---o--(_)--o---*                                                                                 *---o--(_)--o---* 
___________________________________________________________________________________________________________________
|                                                                                                                 |
|       Home        >Employee<          Real estate         Cases           Contractor           Location         |
|_________________________________________________________________________________________________________________|
|                                                                                                                 |
|   - 1               //Search for employee                     - 2           //List all employees                |"""
        self.supervisorLine = """|   - 3               //Creates new employee                    - 4           //Edit an existing employee         |"""

        self.footer = """|   - r               //Return to previous menu                                                                   |
|_________________________________________________________________________________________________________________|
"""

    # def draw_options(self):
    #     #prints out menu bar
    #     self.print_options()
    #     return self.prompt_input()

    def draw_options(self):
        #determines if menu bar should include supervisor options or not
        print(self.header)
        if self.user.is_supervisor():
            print(self.supervisorLine)
        print(self.footer)

    def prompt_input(self):
        while True:
            self.draw_options()
            command = input("Choose option: ")
            if command == "1":
                self.search_emp.search_employee()
                # self.search_employee()
            elif command == "2":
                self.list_all_employees()
            elif command == "3" and self.user.is_supervisor():
                self.create_emp.draw_options()
            elif command == "4":
                pass
            elif command == "r":
                return
            elif command == "m":
                return "m"
            else:
                print("invalid option, try again!")
# ------------------------------------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------------------------------------

# List all employees
    def list_all_employees(self):
        all_emps = self.llapi.all_employees()
        for emp in all_emps: 
            print(emp)
        self.filter_by_location()
        
# Asks to filter by location
    def filter_by_location(self):
        while True:
            filter_input = input("Do you want to filter by location(y/n)?: ")
            if filter_input == 'y':
                location = self.available_locations()
                result = self.llapi.filter_employee(location)
                for row in result:
                    print(row)
                return
            elif filter_input == "n":
                return
            else:
                print("Invalid option")

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