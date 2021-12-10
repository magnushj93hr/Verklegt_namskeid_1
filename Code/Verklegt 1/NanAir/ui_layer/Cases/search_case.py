from ui_layer.Cases.create_report import CreateReport
from ui_layer.Cases.EditCase import EditCase
import datetime
from models.Case import Case

CASE = 'CAS-'


class SearchCase:
    def __init__(self, llapi, user):
        self.llapi = llapi
        self.report = CreateReport(llapi, user)
        self.edit_case = EditCase(llapi)
        self.options = """
      __|__                                                                                             __|__
*---o--(_)--o---*                                                                                 *---o--(_)--o---* 
___________________________________________________________________________________________________________________
|                                                                                                                 |
|       Home        Employee          Real estate         >Cases<           Contractor           Location         |
|_________________________________________________________________________________________________________________|
|                                                                                                                 |
|   - 1              //Search by case ID                                                                          |
|   - 2              //Search by employee ID                                                                      |
|   - 3              //Search by real estate ID                                                                   |
|   - 4              //Search by contractor                                                                       |
|   - r              //Go back                                                                                    |
|_________________________________________________________________________________________________________________|
"""

        self.header_report_open = """
      __|__                                                                                             __|__
*---o--(_)--o---*                                                                                 *---o--(_)--o---* 
___________________________________________________________________________________________________________________
|                                                                                                                 |
|       Home        Employee          Real estate         >Cases<           Contractor           Location         |
|_________________________________________________________________________________________________________________|
|                                                                                                                 |
|   - 1              //Edit case                                - 2             //Make maintenance report         |
|   - r              //Return                                                                                     |
|_________________________________________________________________________________________________________________|"""
        self.header_report_reddy_to_close = """
      __|__                                                                                             __|__
*---o--(_)--o---*                                                                                 *---o--(_)--o---* 
___________________________________________________________________________________________________________________
|                                                                                                                 |
|       Home(home)        Employee(emp)        Real estate(real)         >Cases(cases)<        Contractor(con)    |
|_________________________________________________________________________________________________________________|
|                                                                                                                 |
|    - 1             //accept and close                         - r             //Return to previous menu         |
|_________________________________________________________________________________________________________________|"""
        self.header_report_closed = """
      __|__                                                                                             __|__
*---o--(_)--o---*                                                                                 *---o--(_)--o---* 
___________________________________________________________________________________________________________________
|                                                                                                                 |
|       Home(home)        Employee(emp)        Real estate(real)         >Cases(cases)<        Contractor(con)    |
|_________________________________________________________________________________________________________________|
|                                                                                                                 |
|    - 1             //open case                                - r             //Return to previous menu         |
|_________________________________________________________________________________________________________________|"""



    def search_options(self):
        """Search for case"""    
        while True:
            self.llapi.clear()
            print(self.options)
            command = input("Enter your input: ")
            if command == "1":
                search_id = input("Enter case id: ")
                result = self.llapi.get_case(search_id)
                if result != None:
                    self.status_options(result)
                else:
                    print("No case found")
            elif command == "2":
                search_id = input("Enter employee id: ")
                result = self.llapi.search_case(search_id, 'empid')
                if len(result) != 0:
                    self.printing_cases(result)
                    case = self.select_case()
                    if case != None:
                        self.status_options(case)
                else:
                    print("No case found")
            elif command == "3":
                search_id = input("Enter real estate id: ")
                result = self.llapi.search_case(search_id, 'realid')
                if len(result) != 0:
                    self.printing_cases(result)
                    case = self.select_case()
                    if case != None:
                        self.status_options(case)
                else:
                    print("No case found")
            elif command == "4": 
                cases = self.get_contractors()
                if len(result) != 0:
                    self.printing_cases(result)
                    case = self.select_case()
                    if case != None:
                        self.status_options(case)
                else:
                    print("No case found")
            elif command == "r":
                    return
            else:
                print("Invalid option")


    def print_full_case(self, case):
        """Print case info plus maintenance report"""
        reports = self.llapi.search_maintenance_report(case.id)
        print_case = f"""|                                                                                                                 |
|      Case: {case.id:28s}Created by: {case.emp_id:31}Total cost: {self.get_total_cost(reports):<18s}|
|                                                                                                                 |
|          Real estate ID: {case.real_est_id:87s}|
|                Location: {case.location:87s}|
|                 Subject: {case.subject:87s}|
|             Description: {case.description:87s}|
|                Priority: {case.priority:87s}|
|                Repeated: {case.repeated:87s}|
|           Repeated days: {case.repeat_days:87s}|
|                    Date: {case.date:87s}|
|                  Status: {case.status:87s}|
|             Closed date: {case.closed_date:87s}|
|_________________________________________________________________________________________________________________|"""

        # if case.status == "Open":
        #     self.llapi.clear()
        #     self.status_options(case)
        #     print(self.header_report_open) 
        # elif case.status == "Ready to close":
        #     self.llapi.clear()
        #     self.status_options(case)
        #     print(self.header_report_reddy_to_close)
        # elif case.status == "Closed":
        #     self.llapi.clear()
        #     self.status_options(case)
        #     print(self.header_report_closed)
        # print(print_case)
        print(print_case)

        if len(reports) == 0:
            print("No maintenance reports have been made")
        elif len(reports) == 1:
            self.print_report(reports[0])
        else:
            for rep in reports:
                self.print_report(rep)
            


    def print_report(self, report):
        """prints report"""
        content =  f"""|                                                                                                                 |
|      Maintenance Report                                                                                         |
|                                                                                                                 |
|             Employee ID: {report.employee_id:87s}|
|           Material cost: {report.material_cost:87s}|
|              Contractor: {report.contractor:87s}|
|         Contractor cost: {report.contractor_cost:87s}|
|             Description: {report.description:87s}|
|_________________________________________________________________________________________________________________|"""
        
        print(content)


    def get_total_cost(self, reports):
        """Takes in report info and returns total cost"""
        if len(reports) != 0:
            last_report = reports[-1]
            return last_report.total_cost
        return "0"


    def printing_cases(self, case_list):
        """Prints list of cases"""
        self.llapi.clear()
        header = """
__________________________________________________________________________________________________________________________________________________________________
|   ID       Subject                     Real estate ID       Location                   Priority        Created          Status             Closed date         |
|                                                                                                                                                                |"""
        print(header)
        for case in case_list:
            print(f"|   {case.id:<9s}{case.subject:<28s}{case.real_est_id:<21s}{case.location:<27}{case.priority:<16s}{case.date:<17}{case.status:<19s}{case.closed_date:<20s}|")
        print("|________________________________________________________________________________________________________________________________________________________________|")



    def select_case(self):
        """Asks user if he wants to select a case"""
        while True:
            option = input("Do you want to select a case(y/n): ")
            if option == "y":
                return self.get_the_case()
            elif option == "n":
                return
            else:
                print("Invalid option")

    def get_the_case(self):
        """Returns a case"""
        while True:
            case_id = input("Enter case ID: ")
            case = self.llapi.get_case(case_id)
            if case == None:
                print("No case found")
            else:
                return case

    def get_contractors(self):
        """Displays all available contractors and asks what contractor user wants,
        returns cases he's worked on"""
        all_contractors = self.llapi.get_contractors_name()
        print("Here are all available contractors: ")
        for contractor in all_contractors:
            print(contractor)
        while True:
            print()
            contr_name = input("Enter contractor name: ")
            if contr_name in all_contractors:
                result = self.llapi.search_contractor_in_case(contr_name)
                for case in result:
                    print(case)
                return result
            else:
                print("Invalid option")

    def edit_or_report(self, case):
        """Asks user to enter input, either edit or create"""
        if case.status == "Open":
            while True:
                self.llapi.clear()
                print(self.header_report_open)
                self.print_full_case(case)
                option = input("Enter option: ")
                if option =="1":
                    self.edit_case.promt_edit_case(case)
                    return
                elif option == "2":
                    self.report.create_maintenance_report(case)
                    return
                elif option == "r":
                    return
                else:
                    print("Invalid option")

    def status_options(self, case):
        if case.status == "Open":
            self.edit_or_report(case)
        elif case.status == "Ready to close":
            self.llapi.clear()
            print(self.header_report_reddy_to_close)
            self.print_full_case(case)
            opt = input("Enter option: ")
            if opt == "1":
                reports = self.llapi.search_maintenance_report(case.id)
                self.contractor_review(reports)
                self.change_case_status("Closed", case)
                if case.repeated == "y" and len(reports) == 1:
                    self.create_repeated_case(case.id)
        elif case.status == "Closed":
            self.llapi.clear()
            print(self.header_report_closed)
            self.print_full_case(case)
            opt = input("Enter option: ")
            if opt == "y":
                self.change_case_status("Open", case)



    def create_repeated_case(self, case_id):
        """Takes in case id, making a case a repeated case"""
        all_cases = self.llapi.all_cases()
        case = self.llapi.get_case(case_id)
        id = CASE + str(len(all_cases) + 1)
        next_date = datetime.datetime.strptime(case.date, "%d/%m/%Y") + datetime.timedelta(days = int(case.repeat_days))
        new_date = "%s/%s/%s" % (next_date.day, next_date.month, next_date.year)
        new_case = Case(id, case.location, case.subject, case.description, case.priority, case.repeated, case.repeat_days, case.real_est_id, case.emp_id, new_date)
        self.llapi.create_case(new_case)


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