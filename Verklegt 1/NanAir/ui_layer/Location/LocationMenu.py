from ui_layer.Location.CreateLocation import CreateLocation
from ui_layer.Location.list_all_locations import ListAllLocations

class LocationMenu:
    def __init__(self, llapi, user):
        self.create_location = CreateLocation(llapi, user)
        self.list_locations = ListAllLocations(llapi)
        self.llapi = llapi
        self.user = user
        self.header = """
      __|__                                                                                             __|__
*---o--(_)--o---*                                                                                 *---o--(_)--o---* 
___________________________________________________________________________________________________________________
|                                                                                                                 |
|       >Home(home)<        Employee(emp)        Real estate(real)         Cases(cases)        Contractor(con)    |
|_________________________________________________________________________________________________________________|
|                                                                                                                 |
|       - 1         //List all locations                                                                          |"""
        
        self.supervisor_opt = """|       - 2         //Create new location                                                                         |"""

        self.footer = """|       - r         //Return to previous menu                                                                     |
|_________________________________________________________________________________________________________________|
"""

    def draw_options(self):
        print(self.header)
        if self.user.is_supervisor():
            print(self.supervisor_opt)
        print(self.footer)

    def prompt_input(self):
        while True:
            self.draw_options()
            command = input("Choose option: ")
            if command == "1":
                self.list_locations.list_all_locations()
            elif command == "2" and self.user.is_supervisor():
                self.create_location.create_location()
            elif command == "r":
                return "r"
            else:
                print("invalid option, try again!")
            if command == "m":
                return

