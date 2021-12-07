from logic_layer.LLAPI import LLAPI
from models.Case import Case
from models.MaintananceReport import MaintananceReport

class CaseMenu:
    def __init__(self, llapi):
        self.llapi = llapi
        self.options = """
Case menu
1 - list all cases
2 - edit case
3 - search for case
r - return to previous menu
"""

        self.case_menu = """
Real estate search menu
1 - create maintenance report
r - return to previous menu
    """
    def draw_options(self):
        print(self.options)
        return self.prompt_input()

    def prompt_input(self):
        while True:
            command = input("Enter your input: ")
            if command == "1":
                all_cases = self.llapi.list_cases()
                for case in all_cases:
                    print(case)
            elif command == "2":
                self.edit_case()
            elif command == "3":
                result = self.search_case()
                self.prompt_input_search(result)
            elif command == "r":
                return "r"
            else:
                print("invalid option, try again!")
            print(self.options)
# ------------------------------------------------------------------------------------------------------------------


    def search_case(self):
        self.search_id = input("Enter case id: ")
        result = LLAPI().search_case(self.search_id)
        print(result)
        return result

    def prompt_input_search(self, result):
            while True:
                print(self.case_menu)
                command = input("Enter your input: ")
                if command == "1":
                    self.create_maintenance_report(result)
                elif command == "r":
                    return
                else:
                    print("invalid option, try again!")


    def create_maintenance_report(self, result):
        real_estate_id = result.real_estate_id
        description = input("Enter description:")
        employee_id = input("Enter your employee id: ")
        case_id = result.id
        cost_of_materials = input("Enter cost of materials: ")
        used_contractor = input('Did you use a contractor(y/n)?: ')
        if used_contractor == "y":
            contractor = input("Enter contractor: ")
        
        
        maintenance = MaintananceReport(real_estate_id, description, employee_id, case_id, cost_of_materials, contractor)
        self.llapi.create_maintenance_report(maintenance)

        # id, location, subject, description, priority, repeated, real_est_id, status, date = LLAPI().search_case(case_id)
        #1001,rvk,Pizza,pepperoni,3,y,2/12/2021,0001,open

        # id = "1001"
        # location = "rvk"
        # subject = "Pizza"
        # description = "pepperoni"
        # priority = "3"
        # repeated = "y"
        # real_est_id = "0001"
        print(self.llapi.case_exist(case_id))

        # case = Case(id, location, subject, description, priority, repeated, real_est_id, "ready to close")
        # self.llapi.edit_case(case)