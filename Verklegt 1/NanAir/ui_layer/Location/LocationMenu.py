from ui_layer.Location.list_all_locations import ListAllLocations
from ui_layer.Location.create_location import CreateLocation

class LocationMenu:
    def __init__(self, llapi):
        self.llapi = llapi
        self.list_loc = ListAllLocations(llapi)
        self.create_loc = CreateLocation(llapi)
        self.options = """
      __|__                                                                                             __|__
*---o--(_)--o---*                                                                                 *---o--(_)--o---* 
___________________________________________________________________________________________________________________
|                                                                                                                 |
|       Home        Employee          Real estate         Cases           Contractor           >Location<         |
|_________________________________________________________________________________________________________________|
|                                                                                                                 |
|   - 1              //List all cases                         - 2          //Create new location                  |
|   - r              //Go back                                                                                    |
|_________________________________________________________________________________________________________________|
"""

    def prompt_input(self):
        while True:
            print(self.options)
            command = input("Choose option: ")
            if command == "1":
                self.list_loc.list_all_locations()
            elif command == "2":
                self.create_loc.create_location()
            elif command == "r":
                return
            else:
                print("invalid option, try again!")
            if command == "m":
                return
