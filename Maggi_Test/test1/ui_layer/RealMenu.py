from logic_layer.LLAPI import LLAPI
from models.RealEstate import RealEstate

class RealMenu:
    def __init__(self, llapi):
        self.llapi = llapi
        self.options = """
Dest menu
1 - list all real estate
2 - create real estate
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
            elif command == "2":
                self.create_realestate()
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
        location = input("Enter location of real estate: ")
        
        
        real = RealEstate(address, size, rooms, id, amenities, location)
        self.llapi.create_realestate(real)
