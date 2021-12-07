from ui_layer.Location.create_loc import CreateLoc
from logic_layer.LLAPI import LLAPI
from models.Location import Location

class LocMenu:
    def __init__(self, llapi):
        self.llapi = llapi
        self.create_loc = CreateLoc()
        self.options = """
      __|__                                                                                             __|__
*---o--(_)--o---*                                                                                 *---o--(_)--o---* 
___________________________________________________________________________________________________________________
|                                                                                                                 |
|       >Home(home)<        Employee(emp)        Real estate(real)         Cases(cases)        Contractor(con)    |
|_________________________________________________________________________________________________________________|
|                                                                                                                 |
|   - cr        //Create new location                                    - b           //Go back                  |
|_________________________________________________________________________________________________________________|
"""

    def draw_options(self):
        print(self.options)
        self.prompt_input()

    def prompt_input(self):
        while True:
            command = input("Choose option: ")
            if command == "cr":
                self.create_loc.draw_options()
            elif command == "b":
                return
            else:
                print("invalid option, try again!")
            if command == "m":
                return
            print(self.options)

