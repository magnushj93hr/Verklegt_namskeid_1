from ui_layer.Contractor.list_all_con import ListAllContractors
from ui_layer.Contractor.create_con import CreateCon

class ContractorMenu:
    def __init__(self, llapi, user):
        self.user = user
        self.llapi = llapi
        self.list_all_con = ListAllContractors(llapi)
        self.create_con = CreateCon(llapi)
        self.header = """
      __|__                                                                                             __|__
*---o--(_)--o---*                                                                                 *---o--(_)--o---* 
___________________________________________________________________________________________________________________
|                                                                                                                 |
|       Home         Employee           Real estate         Cases          >Contractor<          Location         |
|_________________________________________________________________________________________________________________|
|                                                                                                                 |
|   - 1               //List all contractor                     - r               //Return to previous menu       |"""
        self.supervisorLine = """|   - 2               //Creates new contractor                                                                    |"""

        self.footer = """|_________________________________________________________________________________________________________________|
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
            elif command == "2" and self.user.is_supervisor():
                self.create_con.create_contractor()
            elif command == "r":
                return "r"
            elif command == "m":
                return "m"
            else:
                print("invalid option, try again!")
            