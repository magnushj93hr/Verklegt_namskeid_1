from ui_layer.Cases.search_case import SearchCase
from ui_layer.Cases.list_all_cases import ListAllCases

class CaseMenu:
    def __init__(self, llapi, user):
        self.llapi = llapi
        self.search_case = SearchCase(llapi, user)
        self.list_all_cases = ListAllCases(llapi, user)
        self.options = """
      __|__                                                                                             __|__
*---o--(_)--o---*                                                                                 *---o--(_)--o---* 
___________________________________________________________________________________________________________________
|                                                                                                                 |
|       Home        Employee          Real estate         >Cases<           Contractor           Location         |
|_________________________________________________________________________________________________________________|
|                                                                                                                 |
|   - 1              //Search for cases                         - 2          //List all cases                     |
|   - r              //Go back                                                                                    |
|_________________________________________________________________________________________________________________|
"""

    def prompt_input(self):
        """Asks user to enter Case menu option"""
        while True:
            self.llapi.clear()
            print(self.options)
            command = input("Choose option: ")
            if command == "1":
                self.search_case.search_options()
            elif command == "2":
                self.list_all_cases.list_all_cases()
            elif command == "r":
                self.llapi.clear()
                return "r"
            else:
                print("invalid option, try again!")
