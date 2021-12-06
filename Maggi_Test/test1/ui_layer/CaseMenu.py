from logic_layer.LLAPI import LLAPI
from models.Case import Case
from models.MaintananceReport import MaintananceReport

class CaseMenu:
    def __init__(self, llapi):
        self.llapi = llapi
        self.options = """
Case menu
1 - list all cases
2 - edit case ##??????
3 - search for case
r - return to previous menu
"""

        self.case_options = """
Case menu ###standa case id hérna ??
1 - edit case ??? þetta er líka í real áttu að geta editað hérna??
2 - create maintenance report
3 - edit maintenance report???
r - return to previous menu
    """
#---------------------------------------------
# Menu options
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
            elif command == "2": #??????? þarf edit í main
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
        self.search_id = input("Enter case id: ")
        result = LLAPI().search_case(self.search_id)
        print(result)

    def prompt_input_search(self):
        while True:
            print(self.case_options)
            command = input("Enter your input: ")
            if command == "1": self.edit_case()
            elif command == "2": self.create_maintenance_report()
            elif command == "3": self.edit_maintenance_report()   
            elif command == "r": return
            else: print("invalid option, try again!")

    def edit_case(self):
        edit_id = self.search_id
        id, location, subject, description, priority, repeated, real_estate_id, date = self.user_options(None)
        
        case = Case(edit_id, location, subject, description, priority, repeated, real_estate_id, date)        
        self.llapi.edit_case(case)


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