from ui_layer.Cases.create_report import CreateReport

class SearchCase:
    def __init__(self, llapi, user):
        self.llapi = llapi
        self.report = CreateReport(llapi, user)
        self.options = """
      __|__                                                                                             __|__
*---o--(_)--o---*                                                                                 *---o--(_)--o---* 
___________________________________________________________________________________________________________________
|                                                                                                                 |
|       Home(home)        Employee(emp)        Real estate(real)         >Cases(cases)<        Contractor(con)    |
|_________________________________________________________________________________________________________________|
|                                                                                                                 |
|   - 1              //Search by case ID                                                                          |
|   - 2              //Search by employee ID                                                                      |
|   - 3              //Search by real estate ID                                                                   |
|   - 4              //Search by contractor                                                                       |
|   - r              //Go back                                                                                    |
|_________________________________________________________________________________________________________________|
"""

    def search_options(self):
        while True:
            print(self.options)
            command = input("Enter your input: ")
            if command == "1":
                search_id = input("Enter case id: ")
                result = self.llapi.get_case(search_id)
                if result != None:
                    self.print_full_case(result)
                    self.make_report(result)
                else:
                    print("No case found")
            elif command == "2":
                search_id = input("Enter employee id: ")
                result = self.llapi.search_case(search_id, 'empid')
                if len(result) != 0:
                    self.printing_cases(result)
                    case = self.select_case()
                    if case != None:
                        self.print_full_case(case)
                        self.make_report(case)
                else:
                    print("No case found")
            elif command == "3":
                search_id = input("Enter real estate id: ")
                result = self.llapi.search_case(search_id, 'realid')
                if len(result) != 0:
                    self.printing_cases(result)
                    case = self.select_case()
                    if case != None:
                        self.print_full_case(case)
                        self.make_report(case)
                else:
                    print("No case found")
            elif command == "4": 
                cases = self.get_contractors()
                if len(result) != 0:
                    self.printing_cases(result)
                    case = self.select_case()
                    if case != None:
                        self.print_full_case(case)
                        self.make_report(case)
                else:
                    print("No case found")
            elif command == "r":
                    return
            else:
                print("Invalid option")


    def print_full_case(self, case):
        reports = self.llapi.search_maintenance_report(case.id)
        print_case = f"""
      __|__                                                                                             __|__
*---o--(_)--o---*                                                                                 *---o--(_)--o---* 
___________________________________________________________________________________________________________________
|                                                                                                                 |
|       Home        Employee          Real estate         >Cases<           Contractor           Location         |
|_________________________________________________________________________________________________________________|
|                                                                                                                 |
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

        print(print_case)
        if len(reports) == 0:
            print("No maintenance reports have been made")
        elif len(reports) == 1:
            self.print_report(reports[0])
        else:
            for rep in reports:
                self.print_report(rep)
            


    def print_report(self, report):
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
        if len(reports) != 0:
            last_report = reports[-1]
            return last_report.total_cost
        return "0"


    def printing_cases(self, case_list):
        header = """
__________________________________________________________________________________________________________________________________________________________________
|   ID       Subject                     Real estate ID       Location                   Priority        Created          Status             Closed date         |
|                                                                                                                                                                |"""
        print(header)
        for case in case_list:
            print(f"|   {case.id:<9s}{case.subject:<28s}{case.real_est_id:<21s}{case.location:<27}{case.priority:<16s}{case.date:<17}{case.status:<19s}{case.closed_date:<20s}|")
        print("|________________________________________________________________________________________________________________________________________________________________|")



    def select_case(self):
        while True:
            option = input("Do you want to select a case(y/n): ")
            if option == "y":
                return self.get_the_case()
            elif option == "n":
                return
            else:
                print("Invalid option")

    def get_the_case(self):
        while True:
            case_id = input("Enter case ID: ")
            case = self.llapi.get_case(case_id)
            if case == None:
                print("No case found")
            else:
                return case

    def get_contractors(self):
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

    def make_report(self, case):
        if case.status == "Open":
            while True:
                option = input("Do you want to create maintenance report(y/n): ")
                if option =="y":
                    self.report.create_maintenance_report(case)
                    return
                elif option == "n":
                    return
                else:
                    print("Invalid option")