from logic_layer.LLAPI import LLAPI
from models.Location import Location

class LocMenu:
    def __init__(self, llapi):
        self.llapi = llapi
        self.options = """
contractor menu
1 - list all locations
2 - create a new location
r - return to previous menu
"""

    def draw_options(self):
        print(self.options)
        return self.prompt_input()

    def prompt_input(self):
        while True:
            command = input("Enter your input: ")
            if command == "1":
                all_loc = self.llapi.all_locations()
                for loc in all_loc:
                    print(loc)
            elif command == "2":
                self.create_location()
            elif command == "r":
                return "r"
            else:
                print("Invalid option, try again!")
            print(self.options)

    def create_location(self):
        country = input("Enter country name: ")
        location = input("Enter location: ")
        airport = input("Enter aiport:")
        phone = input("Enter location phone: ")
        opening_hours = input("Enter location opening hours: ")
        
        loc = Location(country, location, airport, phone, opening_hours)
        self.llapi.create_location(loc)
