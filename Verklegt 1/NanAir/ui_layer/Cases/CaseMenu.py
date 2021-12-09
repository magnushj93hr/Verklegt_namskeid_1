from ui_layer.Cases.search_case import SearchCasae

class CaseMenu:
    def __init__(self, llapi):
        self.llapi = llapi
        self.search_case = SearchCasae(llapi)
        self.options = """
      __|__                                                                                             __|__
*---o--(_)--o---*                                                                                 *---o--(_)--o---* 
___________________________________________________________________________________________________________________
|                                                                                                                 |
|       Home(home)        Employee(emp)        Real estate(real)         >Cases(cases)<        Contractor(con)    |
|_________________________________________________________________________________________________________________|
|                                                                                                                 |
|   - 1              //Search for cases                         - 2          //List all cases                     |
|   - 3              //List all maintenance reports             - r          //Go back                            |
|_________________________________________________________________________________________________________________|
"""

    # def draw_options(self):
    #     print(self.options)
    #     return self.prompt_input()

    def prompt_input(self):
        while True:
            print(self.options)
            command = input("Choose option: ")
            if command == "1":
                self.search_case.search_options()
            elif command == "2":
                pass
            elif command == "3":
                pass
            elif command == "r":
                return "r"
            elif command == "m":
                return "m"
            else:
                print("invalid option, try again!")
