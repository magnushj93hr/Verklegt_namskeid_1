from ui_layer.Employee.create_emp import CreateEmp
from ui_layer.Employee.search_emp import SearchEmp
from ui_layer.Employee.list_all_emp import ListAllEmployee
from ui_layer.Employee.edit_emp import EditEmployee


class EmpMenu:
    def __init__(self, llapi, user):
        self.user = user
        self.llapi = llapi
        self.create_emp = CreateEmp(llapi)
        self.search_emp = SearchEmp(llapi)
        self.list_all_emp = ListAllEmployee(llapi)
        self.edit_emp = EditEmployee(llapi)
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


    def draw_options(self):
        """determines if menu bar should include supervisor options or not"""
        self.llapi.clear()
        print(self.header)
        if self.user.is_supervisor():
            print(self.supervisorLine)
        print(self.footer)

    def prompt_input(self):
        """Asks user to enter employee menu option"""
        while True:
            self.draw_options()
            command = input("Choose option: ")
            if command == "1":
                self.search_emp.search_employee()
            elif command == "2":
                self.list_all_emp.list_all_employees()
            elif command == "3" and self.user.is_supervisor():
                self.create_emp.create_employee()
            elif command == "4":
                self.edit_emp.edit_employee()
            elif command == "r":
                self.llapi.clear()
                return
            else:
                print("invalid option, try again!")

