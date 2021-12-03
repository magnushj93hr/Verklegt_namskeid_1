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

# ------------------------------------------------------------------------------------------------------------------
    def input_and_check(self, info_type, check_fun):
        while True:
            value = input(f"Enter the {info_type} of the real estate: ")
            if not check_fun(value): print(f"Invalid {info_type} for the real estate")
            else: return value

    def location_im(self):
        while True:
            print('Available locations to choose from:')
            for location in AVAILABLE_LOCATIONS:
                print(location)
            location = str(input("Enter location: "))
            if location in AVAILABLE_LOCATIONS:
                break


    def user_options(self, controller):
        address = self.input_and_check("address", lambda value : self.llapi.is_address_correct(value))
        size = self.input_and_check("size", lambda value : self.llapi.check_if_size_correct(value))
        rooms = self.input_and_check("rooms", lambda value : self.llapi.check_if_room_correct(value))
        id = self.input_and_check("id", lambda value : self.llapi.check_if_rel_id_correct(value)) if controller == "create" else None
        amenities = input("Enter amenities seaparadid by (,): ").split(",")
        location = self.location_im()
#----
        return address, size, rooms, int(id), amenities, location
# ------------------------------------------------------------------------------------------------------------------

    def create_realestate(self):
        value = int(input("How many apartments are the in your aria: "))
        address, size, rooms, id, amenities, location = self.user_options("create")
        for apartment in range(0, value+1):
            real = RealEstate(address, size, rooms, id, amenities, location)
            self.llapi.create_realestate(real)
            id += 1

    def edit_realestate(self):
        edit_id = str(input("Enter real estate id: "))
        ready_to_continue = self.llapi.check_if_employee_exists(edit_id)
        if ready_to_continue != None:
            pass

        real = RealEstate(address, size, rooms,edit_id, amentities, location)        
        self.llapi.edit_realestate(real)

    def search_realestate(self):
        search_id = input("Enter real estate id: ")
        result = LLAPI().search_realestate(search_id)
        print(result)
