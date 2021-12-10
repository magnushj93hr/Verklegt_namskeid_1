import datetime
from models.Case import Case
from ui_layer.Cases.search_case import SearchCase

CASE = 'CAS-'

class ListAllCases:
    def __init__(self, llapi, user):
        self.llapi = llapi
        self.search_case = SearchCase(llapi, user)
        self.filter_options = """
      __|__                                                                                             __|__
*---o--(_)--o---*                                                                                 *---o--(_)--o---* 
___________________________________________________________________________________________________________________
|                                                                                                                 |
|       Home        Employee          Real estate         >Cases<           Contractor           Location         |
|_________________________________________________________________________________________________________________|
|                                                                                                                 |
|   - 1              //Filter by open cases                                                                       |
|   - 2              //Filter by "Ready to close" cases                                                           |
|   - 3              //Filter by closed cases                                                                     |
|   - r              //Go back                                                                                    |
|_________________________________________________________________________________________________________________|
"""
    
    def list_all_cases(self):
        """Returns list of all cases and asks if user wants to filter by status"""
        all_cases = self.llapi.all_cases()
        self.search_case.printing_cases(all_cases)
        while True:
            option = input("Do you want to filter by status(y/n): ")
            if option == "y":
                self.prompt_input_filter()
                return
            elif option == "n":
                return
            else:
                print("Invalid option")
        

    def prompt_input_filter(self):
        """Asks user to enter filter by status option"""
        while True:
            self.llapi.clear()
            print(self.filter_options)
            command = input("Enter input: ")
            if command == "1":
                cases = self.llapi.filter_cases("Open")
                case, reports = self.select_case(cases)
                if case != None:
                    self.search_case.edit_or_report(case)

            elif command == "2":
                self.llapi.clear()
                cases = self.llapi.filter_cases("Ready to close")
                case, reports = self.select_case(cases)
                if case != None:
                    close_case_opt = input("Do you want to close the case(y/n): ")
                    if close_case_opt == "y":
                        self.contractor_review(reports)
                        self.change_case_status("Closed", case)
                        if case.repeated == "y" and len(reports) == 1:
                            self.create_repeated_case(case.id)

            elif command == "3":
                self.llapi.clear()
                cases = self.llapi.filter_cases("Closed")
                case, reports = self.select_case(cases)
                if case != None:
                    open_case_opt = input("Do you want to open the case(y/n): ")
                    if open_case_opt == "y":
                        self.change_case_status("Open", case)
            elif command == "r":
                self.llapi.clear()
                return
            else:
                print("Invalid option")


    def select_case(self, cases):
        """Asks to select a case from list of case"""
        self.search_case.printing_cases(cases)
        if len(cases) == 0:
            print("No cases found")
            return None, None
        case_ids_list = map(lambda case: case.id, cases)
        while True:
            search_case_opt = input("Do you want to select a case(y/n): ")
            if search_case_opt == "n":
                return None, None
            elif search_case_opt == "y":
                while True:
                    case_id = input("Enter case id: ")
                    if case_id not in case_ids_list:
                        print("Invalid id")
                    case = next(case for case in cases if case.id == case_id)
                    reports = self.llapi.search_maintenance_report(case_id)
                    self.search_case.print_full_case(case)
                    return case, reports
            else:
                print("Invalid option")


    def contractor_review(self, reports):
        """Asks user to review contractor"""
        report = reports[-1]
        contractor = self.llapi.search_contractor(report.contractor)
        if report.contractor != "":
            while True:
                review = input("Pleas review contractor(1-5): ")
                if review != "1" and review != "2" and review != "3" and review != "4" and review != "5":
                    print("Invalid input")
                else:
                    contractor.review = review
                    self.llapi.edit_contractor(contractor)
                    return
                    
        return

    def change_case_status(self, status, case):
        """Takes in case information and status, changes the status of the case """
        if status == "Closed":
            dt = datetime.datetime.now()
            case.closed_date = "%s/%s/%s" % (dt.day, dt.month, dt.year)
        elif status == "Open":
            case.closed_date = None
        case.status = status
        self.llapi.edit_case(case)

    def create_repeated_case(self, case_id):
        """Takes in case id, making a case a repeated case"""
        all_cases = self.llapi.all_cases()
        case = self.llapi.get_case(case_id)
        id = CASE + str(len(all_cases) + 1)
        next_date = datetime.datetime.strptime(case.date, "%d/%m/%Y") + datetime.timedelta(days = int(case.repeat_days))
        new_date = "%s/%s/%s" % (next_date.day, next_date.month, next_date.year)
        new_case = Case(id, case.location, case.subject, case.description, case.priority, case.repeated, case.repeat_days, case.real_est_id, case.emp_id, new_date)
        self.llapi.create_case(new_case)