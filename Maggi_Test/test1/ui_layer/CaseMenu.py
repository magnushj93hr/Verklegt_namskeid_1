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

        self.case_menu = """
Real estate search menu
1 - create maintenance report
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
                all_cases = self.llapi.list_cases()
                for case in all_cases:
                    print(case)
                filter_input = input("Do you want to filter by status(y/n): ")
                if filter_input == "y":
                    self.prompt_input_filter()
            elif command == "2":
                result = self.search_case()
                self.prompt_input_search(result)
            elif command == "r":
                return "r"
            else:
                print("Invalid option, try again!")
            print(self.options)
# ------------------------------------------------------------------------------------------------------------------

    def search_case(self):
        self.search_id = input("Enter case id: ")
        result = self.llapi.search_case(self.search_id)
        print(result)
        return result

    def prompt_input_filter(self):
        while True:
            print(self.filter_options)
            command = input("Enter input: ")
            if command == "1":
                cases = self.llapi.filter_cases("Open")
                cases_id = []
                for case in cases:
                    cases_id.append(case.id)
                    print(case)
                search_case_opt = input("Do you want to select a case(y/n): ")
                if search_case_opt == "y":
                    case_id = self.select_id(cases_id)
            elif command == "2":
                cases = self.llapi.filter_cases("Ready to close")
                cases_id = []
                for case in cases:
                    cases_id.append(case.id)
                    print(case)
                search_case_opt = input("Do you want to select a case(y/n): ")
                if search_case_opt == "y":
                    case_id = self.select_id(cases_id)
                    close_case_opt = input("Do you want to close the case(y/n): ")
                    if close_case_opt == "y":
                        self.change_case_status("Close", case_id)
            elif command == "3":
                cases = self.llapi.filter_cases("Close")
                cases_id = []
                for case in cases:
                    cases_id.append(case.id)
                    print(case)
                search_case_opt = input("Do you want to select a case(y/n): ")
                if search_case_opt == "y":
                    case_id = self.select_id(cases_id)
                    open_case_opt = input("Do ypu want to open the case(y/n): ")
                    if open_case_opt == "y":
                        self.change_case_status("Open", case_id)
            elif command == "r":
                return
            else:
                print("Invalid option")

    def select_id(self, cases_id):
        while True:
            case_id = input("Enter case id: ")
            if case_id not in cases_id:
                print("Invalid id")
            print(self.llapi.search_case(case_id))
            print(f"Report - {self.llapi.search_maintenance_report(case_id)}")
            return case_id

    def change_case_status(self, status, case_id):
        case = self.llapi.search_case(case_id)
        case.status = status
        self.llapi.edit_case(case)

    def prompt_input_search(self, result):
            while True:
                print(self.case_menu)
                command = input("Enter your input: ")
                if command == "1":
                    self.create_maintenance_report(result)
                elif command == "r":
                    return
                else:
                    print("Invalid option, try again!")


    def create_maintenance_report(self, result):
        real_estate_id = result.real_est_id
        tasks_done = input("Enter what you did:")
        employee_id = input("Enter your employee id: ")
        case_id = result.id
        cost_of_materials = input("Enter cost of materials: ")
        used_contractor = input('Did you use a contractor(y/n)?: ')
        if used_contractor == "y":
            contractor = input("Enter contractor: ")
        else:
            contractor = ""
        
        maintenance = MaintananceReport(real_estate_id, tasks_done, employee_id, case_id, cost_of_materials, contractor)

        case = self.llapi.search_case(case_id)
        case.status = "Ready to close"
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
        repeated = input("Is the case repeated(y/n)?: ")
        real_id = self.input_and_check("id", lambda value : self.llapi.check_if_rel_id_correct(value)) if controller == "create" else 0

        return int(id), location, subject, description, priority, repeated, real_id

