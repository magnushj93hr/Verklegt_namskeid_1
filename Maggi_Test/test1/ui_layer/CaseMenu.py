from logic_layer.LLAPI import LLAPI
from models.Case import Case
from models.MaintananceReport import MaintananceReport

AVAILABLE_LOCATIONS = ["Reykjavík", "Nuuk", "Kulusuk", "Þórshöfn", "Tingwall", "Longyearbyen" ]

class CaseMenu:
    def __init__(self, llapi):
        self.llapi = llapi
        self.options = """
Case menu
1 - list all cases
2 - search for case
r - return to previous menu
"""

        self.case_options = """
Case search menu
1 - edit case
2 - create maintenance report
r - return to previous menu
    """

        self.filter_options = """
1 - filter by open cases
2 - filter by "ready to close" cases
3 - filter by closed cases
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
                filter_input = input("Do you want to filter by status(y/n): ")
                if filter_input == "y":
                    self.prompt_input_filter()
            elif command == "2":
                self.search_case()
                self.prompt_input_search()
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

    def prompt_input_filter(self):
        while True:
            print(self.filter_options)
            command = input("Enter input: ")
            if command == "1":
                cases = self.llapi.filter_cases("open")
                for case in cases:
                    print(case)
            elif command == "2":
                cases = self.llapi.filter_cases("ready to close")
                for case in cases:
                    print(case)
            elif command == "3":
                cases = self.llapi.filter_cases("close")
                for case in cases:
                    print(case)
            elif command == "r":
                return
            else:
                print("Invalid option")

    def prompt_input_search(self):
            while True:
                print(self.case_options)
                command = input("Enter your input: ")
                if command == "1":
                    self.edit_case()
                elif command == "2":
                    self.create_maintenance_report()
                elif command == "r":
                    return
                else:
                    print("invalid option, try again!")


    def create_maintenance_report(self):
        real_estate_id = input("Enter real estate id: ")
        description = input("Enter description: ")
        repeated = input("Is it repeated: ")
        employee_id = input("Enter employee id: ")
        case_id = self.search_id
        total_cost = input("Enter total cost: ")
        contractor = input("Enter contractor: ")
        
        maintenance = MaintananceReport(real_estate_id, description, repeated, employee_id, case_id, total_cost, contractor)

        case = self.llapi.search_case(case_id)
        case.status = "ready to close"
        self.llapi.create_maintenance_report(maintenance)
        self.llapi.edit_case(case)

    def edit_case(self):
        edit_id = self.search_id
        _, location, subject, description, priority, repeated, real_est_id = self.user_options(None)

        case = Case(edit_id, location, subject, description, priority, repeated, real_est_id)        
        self.llapi.edit_case(case)       
#----------------------------------------------------------------
    def input_and_check(self, info_type, check_fun):
        while True:
            value = input(f"Enter case {info_type}: ")
            if not check_fun(value): print(f"Invalid case {info_type}")
            else: return value  

    def location_in(self):
        while True:
            print('Available locations to choose from:')
            for location in AVAILABLE_LOCATIONS:
                print(location)
            location = str(input("Enter location: "))
            if location in AVAILABLE_LOCATIONS:
                return location

    def user_options(self, controller):
        id = self.input_and_check("id", lambda value : self.llapi.is_id_correct(value)) if controller == "create" else 0
        location = self.location_in()
        subject = input("Enter subject: ")
        description = input("Enter description: ")
        priority = input("Enter priority: ")
        repeated = input("Is the case repeated?: ")
        real_id = self.input_and_check("id", lambda value : self.llapi.check_if_rel_id_correct(value)) if controller == "create" else 0

        return int(id), location, subject, description, priority, repeated, real_id

