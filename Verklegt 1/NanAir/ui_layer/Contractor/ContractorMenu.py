from ui_layer.Contractor.list_all_con import ListAllContractors
from ui_layer.Contractor.create_con import CreateCon
from ui_layer.Contractor.search_con import SearchCon
from ui_layer.Contractor.edit_con import EditCon

class ContractorMenu:
    def __init__(self, llapi, user):
        self.user = user
        self.llapi = llapi
        self.list_all_con = ListAllContractors(llapi)
        self.create_con = CreateCon(llapi)
        self.search_con = SearchCon(llapi)
        self.edit_con = EditCon(llapi)
        self.header = """
      __|__                                                                                             __|__
*---o--(_)--o---*                                                                                 *---o--(_)--o---* 
___________________________________________________________________________________________________________________
|                                                                                                                 |
|       Home         Employee           Real estate         Cases          >Contractor<          Location         |
|_________________________________________________________________________________________________________________|
|                                                                                                                 |
|   - 1               //List all contractor                     - 2               //Search contractor             |"""
        self.supervisorLine = """|   - 3               //Creates new contractor                  - 4               //Edit contractor               |"""

        self.footer = """|   - r               //return                                                                                    |
|_________________________________________________________________________________________________________________|
"""


    def draw_options(self):
        """determines if menu bar should include supervisor options or not"""
        print(self.header)
        if self.user.is_supervisor():
            print(self.supervisorLine)
        print(self.footer)

    def prompt_input(self):
        """Asks user to enter contractor menu option"""
        while True:
            self.draw_options()
            command = input("Choose option: ")
            if command == "1":
                self.list_all_con.list_all_contractors()
            elif command == "2":
                self.search_con.search_con()
            elif command == "3" and self.user.is_supervisor():
                self.create_con.create_contractor()
            elif command == "4" and self.user.is_supervisor():
                self.edit_con.promt_input()
            elif command == "r":
                return "r"
            elif command == "m":
                return "m"
            else:
                print("invalid option, try again!")
            