from ui_layer.Contractor.create_con import CreateReal
from logic_layer.LLAPI import LLAPI
from models.Contractor import Contractor

class Contractor:
    def __init__(self, llapi, user):
        self.user = user
        self.llapi = llapi
        self.create_con = CreateCon
        self.header = """
      __|__                                                                                             __|__
*---o--(_)--o---*                                                                                 *---o--(_)--o---* 
___________________________________________________________________________________________________________________
|                                                                                                                 |
|       Home(home)        Employee(emp)        Real estate(real)         Cases(cases)        >Contractor(con)<    |
|_________________________________________________________________________________________________________________|
|                                                                                                                 |
|   - s               //Search for contractor                      - fi          //Filter options                 |
|   - o               //Open, for more info                        - d           //Display cases form contractor  |
|   - b               //Go back                                                                                   |"""
        self.supervisorLine = """|   - cr              //Creates new contractor                                                                    |"""

        self.footer = """|_________________________________________________________________________________________________________________|
"""

    def draw_options(self):
        #prints out menu bar
        self.print_options()
        return self.prompt_input()

    def print_options(self):
        #determines if menu bar should include supervisor options or not
        print(self.header)
        if self.user.is_supervisor():
            print(self.supervisorLine)
        print(self.footer)

    def prompt_input(self):
        while True:
            command = input("Choose option: ")
            if command == "s":
                pass
                # all_emps = self.llapi.all_employees()
                # for emp in all_emps:
                #     print(emp)
            elif command == "cr" and self.user.is_supervisor():
                self.create_con.draw_options()
            elif command == "fi":
                pass
            elif command == "o":
                pass
            elif command == "d":
                pass
            elif command == "b":
                return "b"
            elif command == "m":
                return "m"
            else:
                print("invalid option, try again!")
            print(self.options)