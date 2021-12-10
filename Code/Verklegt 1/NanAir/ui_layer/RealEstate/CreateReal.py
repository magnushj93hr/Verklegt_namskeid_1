from models.RealEstate import RealEstate

class CreateReal:
    
    def __init__(self, llapi, user):
        self.llapi = llapi
    
#=============================User input functions begins here======================================================================

# ------------------------------------------------------------------------------------------------------------------
# Check if the input is valid and 
    def input_real_and_check(self, info_type, check_fun):
        """Takes in real estate info type  and checks if the value is valid"""
        while True:
            value = input(f"Enter the {info_type} of the real estate: ")
            if not check_fun(value): print(f"Invalid {info_type} for the real estate")
            else: return value

    def input_case_and_check(self, info_type, check_fun):
        """Takes in case info type and checks if the value is valid"""
        while True:
            value = input(f"Enter case {info_type}: ")
            if not check_fun(value): print(f"Invalid {info_type} for the real estate")
            else: return value

    def location_in(self):
        """Displays all location and asks user to enter location"""
        while True:
            print('Available locations to choose from:')
            for location in self.llapi.get_locations_name():
                print(location)
            location = str(input("Enter location: "))
            if location in self.llapi.get_locations_name(): return location
            else: print("Invalid location")


    def user_options(self, controller):
        """User input and checks if its valid, returns real estate info"""
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
        """Create real estate"""
        try:
            value = int(input("How many apartments are available for rental: "))
            star = True
        except ValueError:
            print("Only enter a int number")
            star = False
        if star == True:
            address, size, rooms, id, amenities, location = self.user_options("create")
            if value > 1:
                for apartment in range(0, value):
                    self.make_realestate(address, size, rooms, id, amenities, location)
                    id += 1
            else: self.make_realestate(address, size, rooms, id, amenities, location)

    def make_realestate(self, address, size, rooms, id, amenities, location):
        """Make real estate"""
        real = RealEstate(address, size, rooms, id, amenities, location)
        save = self.display_real(real)
        if save == True:
            self.llapi.create_realestate(real)
# ------------------------------------------------------------------------------------------------------------------

    def display_real(self, real):
        """Prints real estate info"""
        self.header = """
      __|__                                                                                             __|__
*---o--(_)--o---*                                                                                 *---o--(_)--o---* 
___________________________________________________________________________________________________________________
|                                                                                                                 |
|       Home        Employee          >Real estate<         Cases           Contractor           Location         |
|_________________________________________________________________________________________________________________|
|                                                                                                                 |
|   Create New Real Estate                                                                                        |
|_________________________________________________________________________________________________________________|"""
        
        self.new_real = f"""|                                                                                                                 |
|      Real Eastete                                                                                               |
|                                                                                                                 |
|            1 - address: {real.address:88s}|
|            2 - size: {real.size:91s}|
|            3 - rooms: {real.rooms:90s}|
|            4 - amenities: {str(real.amenities):86s}|
|            5 - location: {real.location:87s}|
|_________________________________________________________________________________________________________________|"""
        self.llapi.clear()
        print(f"{self.header}\n{self.new_real}")
        while True:
            save = input("Do you want to save real estate(y/n): ")
            if save == "y":
                return True
            elif save == "n":
                return False
            else:
                print("Invalid option")