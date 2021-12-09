from models.RealEstate import RealEstate

class CreateReal:
    
    def __init__(self, llapi, user):
        self.llapi = llapi
    
#=============================User input functions begins here======================================================================

# ------------------------------------------------------------------------------------------------------------------
# Check if the input is valid and 
    def input_real_and_check(self, info_type, check_fun):
        while True:
            value = input(f"Enter the {info_type} of the real estate: ")
            if not check_fun(value): print(f"Invalid {info_type} for the real estate")
            else: return value

    def input_case_and_check(self, info_type, check_fun):
        while True:
            value = input(f"Enter case {info_type}: ")
            if not check_fun(value): print(f"Invalid {info_type} for the real estate")
            else: return value

    def location_in(self):
        while True:
            print('Available locations to choose from:')
            for location in self.llapi.get_locations_name():
                print(location)
            location = str(input("Enter location: "))
            if location in self.llapi.get_locations_name(): return location
            else: print("Invalid location")


    def user_options(self, controller):
        address = self.input_real_and_check("address", lambda value : self.llapi.is_address_correct(value))
        size = self.input_real_and_check("size", lambda value : self.llapi.check_if_size_correct(value))
        rooms = self.input_real_and_check("rooms", lambda value : self.llapi.check_if_room_correct(value))
        id = self.input_real_and_check("id", lambda value : self.llapi.check_if_rel_id_correct(value)) if controller == "create" else 0
        amenities = input("Enter amenities seperated by (,): ").split(",")
        location = self.location_in()

        return address, size, rooms, int(id), amenities, location
# ------------------------------------------------------------------------------------------------------------------

#=============================Real Estate functions begins here======================================================================

# ------------------------------------------------------------------------------------------------------------------
# Create real estate
    def create_realestate(self):
        try:
            value = int(input("How many apartments are the in your area: "))
        except ValueError:
            print("Only enter a int number")
        address, size, rooms, id, amenities, location = self.user_options("create")
        if value > 1:
            for apartment in range(0, value):
                self.make_realestate(address, size, rooms, id, amenities, location)
                id += 1
        else: self.make_realestate(address, size, rooms, id, amenities, location)

    def make_realestate(self, address, size, rooms, id, amenities, location):
        real = RealEstate(address, size, rooms, id, amenities, location)
        self.llapi.create_realestate(real)
# ------------------------------------------------------------------------------------------------------------------