from logic_layer.LLAPI import LLAPI
from models.Case import Case
from models.MaintananceReport import MaintananceReport
import datetime

# AVAILABLE_LOCATIONS = ["Reykjavík", "Nuuk", "Kulusuk", "Þórshöfn", "Tingwall", "Longyearbyen" ]
CASE = 'CAS-'

class CaseMenu:
    def __init__(self, llapi):
        self.llapi = llapi
        self.options = """
Case menu
1 - list all cases
2 - search for case
3 - list all maintenance reports
r - return to previous menu
"""

        self.case_menu = """
Real estate search menu
1 - create maintenance report
r - return to previous menu
    """

        self.filter_options = """
1 - filter by open cases
2 - filter by "Ready to close" cases
3 - filter by closed cases
r - return to previous menu
"""

        self.search_options = """
1 - search by case id
2 - search by employee id
3 - search by real_estate_id
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
                case_list = self.search_case()
                if len(case_list) == 1:
                    self.prompt_input_search(case_list[0])
                elif len(case_list) == 0:
                    return
                else:
                    selected_case = self.prompt_which_case(case_list)
                    if selected_case != None:
                        self.prompt_input_search(selected_case)
            elif command == "3": 
                all_maintenance_reports = self.llapi.all_maintenance_reports()
                for maintenance in all_maintenance_reports:
                    print(maintenance)
            elif command == "r":
                return "r"
            else:
                print("Invalid option, try again!")
            print(self.options)

    def prompt_which_case(self, case_list):
        case_id = input("Enter case id: ")
        for case in case_list:
            if case_id == case.id:
                return case
        print("Unknown case!")
        return None
# ------------------------------------------------------------------------------------------------------------------

    def search_case(self):
        print(self.search_options)
        command = input("Enter your input: ")
        if command == "1":
            search_id = input("Enter case id: ")
            result = self.llapi.get_case(search_id)
            print(result)
            return [result]
        elif command == "2":
            search_id = input("Enter employee id: ")
            result = LLAPI().search_case(search_id, 'empid')
            for i in result:
                print(i)
            return result
        elif command == "3":
            search_id = input("Enter real estate id: ")
            result = LLAPI().search_case(search_id, 'realid')
            for i in result:
                print(i)
            return result
        elif command == "r":
                return
        # return result

    def prompt_input_filter(self):
        while True:
            print(self.filter_options)
            command = input("Enter input: ")
            if command == "1":
                cases = self.llapi.filter_cases("Open")
                case, report = self.select_case(cases)
                if case != None:
                    make_report = input("Do you want to make a report(y/n): ")
                    if make_report == "y":
                        self.create_maintenance_report(case)

            elif command == "2":
                cases = self.llapi.filter_cases("Ready to close")
                case, report = self.select_case(cases)
                if case != None:
                    close_case_opt = input("Do you want to close the case(y/n): ")
                    if close_case_opt == "y":
                        self.contractor_review(report)
                        self.change_case_status("Close", case)
                        if case.repeated == "y":
                            self.create_repeated_case(case)

            elif command == "3":
                cases = self.llapi.filter_cases("Close")
                case, report = self.select_case(cases)
                if case != None:
                    open_case_opt = input("Do you want to open the case(y/n): ")
                    if open_case_opt == "y":
                        self.change_case_status("Open", case)
            elif command == "r":
                return
            else:
                print("Invalid option")

    def select_case(self, cases):
        for case in cases:
            print(case)
        case_ids_list = map(lambda case: case.id, cases)
        search_case_opt = input("Do you want to select a case(y/n): ")
        if search_case_opt != "y":
            return None
        while True:
            case_id = input("Enter case id: ")
            if case_id not in case_ids_list:
                print("Invalid id")
            case = next(case for case in cases if case.id == case_id)
            print(case)
            report = self.llapi.search_maintenance_report(case_id)
            print(f"Report - {report}")
            return case, report


    # def select_id(self, case_ids_list):
    #     while True:
    #         case_id = input("Enter case id: ")
    #         if case_id not in case_ids_list:
    #             print("Invalid id")
    #         print(self.llapi.search_case(case_id))
    #         print(f"Report - {self.llapi.search_maintenance_report(case_id)}")
    #         return case_id, self.llapi.search_maintenance_report(case_id)

    def contractor_review(self, report):
        contractor = self.llapi.search_contractor(report.contractor)
        if report.contractor != "":
            contractor.review = int(input("Pleas review contractor(1-5): "))
            self.llapi.edit_contractor(contractor)
        return

    def change_case_status(self, status, case):
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
        tasks_done = input("Enter what you did: ")
        employee_id = input("Enter your employee id: ")
        case_id = result.id
        cost_of_materials = int(input("Enter cost of materials: "))
        used_contractor = input('Did you use a contractor(y/n)?: ')
        if used_contractor == "y":
            contractor = input("Enter contractor: ")
            contractor_cost = int(input("Enter contractor cost: "))
            total_cost = cost_of_materials + contractor_cost
        else:
            contractor = ""
            contractor_cost = 0
            total_cost = cost_of_materials
        
        maintenance = MaintananceReport(real_estate_id, tasks_done, employee_id, case_id, total_cost, contractor, contractor_cost)

        case = self.llapi.get_case(case_id)
        case.status = "Ready to close"
        self.llapi.create_maintenance_report(maintenance)
        self.llapi.edit_case(case)

    # def edit_case(self):
    #     edit_id = self.search_id
    #     _, location, subject, description, priority, repeated, real_est_id = self.user_options(None)

    #     case = Case(edit_id, location, subject, description, priority, repeated, real_est_id)        
    #     self.llapi.edit_case(case)       
#----------------------------------------------------------------
    def input_and_check(self, info_type, check_fun):
        while True:
            value = input(f"Enter case {info_type}: ")
            if not check_fun(value): print(f"Invalid case {info_type}")
            else: return value  

    def location_in(self):
        while True:
            print('Available locations to choose from:')
            for location in self.llapi.get_locations_name():
                print(location)
            location = str(input("Enter location: "))
            if location in self.llapi.get_locations_name():
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

    def create_repeated_case(self, case):
        all_cases = self.llapi.all_cases()
        id = CASE + str(len(all_cases) + 1)
        next_date = datetime.datetime.strptime(case.date, "%d/%m/%Y") + datetime.timedelta(days = int(case.repeat_days))
        new_date = "%s/%s/%s" % (next_date.day, next_date.month, next_date.year)
        new_case = Case(id, case.location, case.subject, case.description, case.priority, case.repeated, case.repeat_days, case.real_est_id, case.emp_id, new_date)
        self.llapi.create_case(new_case)   