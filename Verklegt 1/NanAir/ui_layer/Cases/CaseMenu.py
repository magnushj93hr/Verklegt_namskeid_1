from ui_layer.Cases.search_case import SearchCasae
from ui_layer.Cases.list_all_cases import ListAllCases

class CaseMenu:
    def __init__(self, llapi):
        self.llapi = llapi
        self.search_case = SearchCasae(llapi)
        self.list_all_cases = ListAllCases(llapi)
        self.options = """
      __|__                                                                                             __|__
*---o--(_)--o---*                                                                                 *---o--(_)--o---* 
___________________________________________________________________________________________________________________
|                                                                                                                 |
|       Home(home)        Employee(emp)        Real estate(real)         >Cases(cases)<        Contractor(con)    |
|_________________________________________________________________________________________________________________|
|                                                                                                                 |
|   - 1              //Search for cases                         - 2          //List all cases                     |
|   - r              //Go back                                                                                    |
|_________________________________________________________________________________________________________________|
"""

    def prompt_input(self):
        while True:
            print(self.options)
            command = input("Choose option: ")
            if command == "1":
                self.search_case.search_options()
            elif command == "2":
                self.list_all_cases.list_all_cases()
            elif command == "r":
                return "r"
            elif command == "m":
                return "m"
            else:
                print("invalid option, try again!")
