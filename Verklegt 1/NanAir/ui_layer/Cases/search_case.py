

class SearchCasae:
    def __init__(self, llapi):
        self.llapi = llapi
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
                self.print_full_case(result)
            elif command == "2":
                search_id = input("Enter employee id: ")
                result = self.llapi.search_case(search_id, 'empid')
                self.printing_cases(result)
                case = self.select_case()
                self.print_full_case(case)
            elif command == "3":
                search_id = input("Enter real estate id: ")
                result = self.llapi.search_case(search_id, 'realid')
                self.printing_cases(result)
                case = self.select_case()
                self.print_full_case(case)
            elif command == "4": 
                search_contractor = input("Enter contractor name: ")
                result = False
            elif command == "r":
                    return
            else:
                print("Invalid option")


# id, location, subject, description, priority, repeated, repeat_days, real_est_id, emp_id, date = None, status = 'Open', closed_date = None


    def print_full_case(self, case):
            printing_case = f"""
      __|__                                                                                             __|__
*---o--(_)--o---*                                                                                 *---o--(_)--o---* 
___________________________________________________________________________________________________________________
|                                                                                                                 |
|       Home        Employee          Real estate         >Cases<           Contractor           Location         |
|_________________________________________________________________________________________________________________|
|                                                                                                                 |
|      Case: {case.id:101s}|
|                                                                                                                 |
|          Real estate ID: {case.real_est_id:87s}|
|             Employee ID: {case.emp_id:87s}|
|                Location: {case.location:87s}|
|                 Subject: {case.id:87s}|
|            Descriptioin: {case.description:87s}|
|                Priority: {case.priority:87s}|
|                Repeated: {case.repeated:87s}|
|           Repeated days: {case.repeat_days:87s}|
|                    Date: {case.date:87s}|
|                  Status: {case.status:87s}|
|             Closed date: {case.closed_date:87s}|
|_________________________________________________________________________________________________________________|
"""
            print(printing_case)


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



    # all_contractors = self.llapi.get_contractors_name()
    # print('Here are all available contractors:')
    # for contractor in all_contractors:
    #     print(contractor)
    # while True:
    #     print()
    #     contr_name = input("Enter contractor name: ")
    #     if contr_name in all_contractors:
    #         result = self.llapi.search_contractor_in_case(contr_name)
    #         for i in result:
    #             print(i)
    #         return result