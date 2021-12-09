from ui_layer.Employee.create_emp import CreateEmp
from ui_layer.Employee.search_emp import SearchEmp
from ui_layer.Employee.list_all_emp import ListAllEmployee


class EmpMenu:
    def __init__(self, llapi, user):
        self.user = user
        self.llapi = llapi
        self.create_emp = CreateEmp(llapi)
        self.search_emp = SearchEmp(llapi)
        self.list_all_emp = ListAllEmployee(llapi)
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
            elif command == "2":
                self.list_all_emp.list_all_employees()
            elif command == "3" and self.user.is_supervisor():
                self.create_emp.create_employee()
            elif command == "4":
                pass
            elif command == "r":
                return
            elif command == "m":
                return "m"
            else:
                print("invalid option, try again!")

