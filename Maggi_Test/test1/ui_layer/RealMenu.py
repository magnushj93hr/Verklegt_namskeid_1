from logic_layer.LLAPI import LLAPI
from models.RealEstate import RealEstate

AVAILABLE_LOCATIONS = ["Reykjavík", "Nuuk", "Kulusuk", "Þórshöfn", "Tingwall", "Longyearbyen" ]

class RealMenu:
    def __init__(self, llapi):
        self.llapi = llapi
        self.options = """
Dest menu
1 - list all real estate
2 - create real estate
3 - edit real estate
4 - search real estate
r - return to previous menu
"""

    def draw_options(self):
        print(self.options)
        return self.prompt_input()

    def prompt_input(self):
        while True:
            command = input("Enter your input: ")
            if command == "1":
                all_real = self.llapi.all_realestate()
                for real in all_real:
                    print(real)
                filter_input = input("Do you want to filter by location(y/n)?: ")
                if filter_input == 'y':
                    filter_location = input('Enter location to filter by: ')
                    result = LLAPI().filter_realestate(filter_location)
                    for row in result:
                        print(row)
            elif command == "2":
                self.create_realestate()
            elif command == "3":
                self.edit_realestate()
            elif command == "4":
                self.search_realestate()
            elif command == "r":
                return
            else:
                print("invalid option, try again!")
            print(self.options)
    
    def create_realestate(self):
        address = input("Enter address: ")
        size = input("Enter size of real estate: ")
        rooms = input("Enter how many rooms are in the real estate: ")
        id = input("Enter ID of real estate: ")
        amenities = input("Enter amenities of real estate: ")
        while True:
            print('Available locations to choose from:')
            for location in AVAILABLE_LOCATIONS:
                print(location)
            location = str(input("Enter location: "))
            if location in AVAILABLE_LOCATIONS:
                break
            
        real = RealEstate(address, size, rooms, id, amenities, location)
        self.llapi.create_realestate(real)

    def edit_realestate(self):
        edit_id = str(input("Enter real estate id: "))

        print(f"you are editing real estate with the id: {edit_id}")
        print("You can't delete the real estate id.\n")
        address = str(input("Enter address: "))
        size = str(input("Enter size: "))
        rooms = str(input("Enter rooms: "))
        amentities = str(input("Enter amentities "))
        while True:
            print('Available locations to choose from:')
            for location in AVAILABLE_LOCATIONS:
                print(location)
            location = str(input("Enter location: "))
            if location in AVAILABLE_LOCATIONS:
                break

        real = RealEstate(address, size, rooms,edit_id, amentities, location)        
        self.llapi.edit_realestate(real)

    def search_realestate(self):
        search_id = input("Enter real estate id: ")
        result = LLAPI().search_realestate(search_id)
        print(result)
