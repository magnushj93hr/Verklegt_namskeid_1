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

        self.real_est_options = """
Real estate search menu
1 - edit real estate
2 - create case
3 - edit case
r - return to previous menu
    """
    def draw_options(self):
        print(self.options)
        return self.prompt_input()

    def prompt_input(self):
        while True:
            command = input("Enter your input: ")
            if command == "1":
                all_cases = self.llapi.all_cases()
                for case in all_cases:
                    print(case)
            elif command == "2":
                self.edit_case()
            elif command == "3":
                self.search_case()
            elif command == "r":
                return "r"
            else:
                print("invalid option, try again!")
            print(self.options)
# ------------------------------------------------------------------------------------------------------------------


    def search_case(self):
        search_id = input("Enter case id: ")
        result = LLAPI().search_case(search_id)
        print(result)

    def prompt_input_search(self):
            while True:
                print(self.real_est_options)
                command = input("Enter your input: ")
                if command == "1":
                    self.edit_realestate()
                elif command == "2":
                    self.create_case()
                elif command == "3":
                    self.edit_case()   
                elif command == "r":
                    return
                else:
                    print("invalid option, try again!")


    def create_maintenance_report(self):
        real_estate_id = input("Enter ID: ")
        description = input("Enter description:")
        repeated = input("Is it repeated: ")
        employee_id = input("Enter employee id : ")
        case_id = input("Enter case id: ")
        total_cost = input("Enter total cost: ")
        contractor = input("Enter contractor: ")
        
        
        maintenance = MaintananceReport(real_estate_id, description, repeated, employee_id, case_id, total_cost, contractor)
        self.llapi.create_maintenance_report(maintenance)