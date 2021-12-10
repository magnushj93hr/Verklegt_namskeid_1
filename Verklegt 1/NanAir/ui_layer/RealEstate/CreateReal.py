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
        real = RealEstate(address, size, rooms, id, amenities, location)
        save = self.display_real(real)
        if save == True:
            self.llapi.create_realestate(real)
# ------------------------------------------------------------------------------------------------------------------

    def display_real(self, real):
        print(real)
        self.edit_options = f"""
            Real estate: {real.id}

            1 - address: {real.address}
            2 - size: {real.size}
            3 - rooms: {real.rooms}
            4 - amenities: {real.amenities}
            5 - location: {real.location}
            r - return to previous menu
            """
        print(self.edit_options)
        self.header = """
      __|__                                                                                             __|__
*---o--(_)--o---*                                                                                 *---o--(_)--o---* 
___________________________________________________________________________________________________________________
|                                                                                                                 |
|       Home(home)        Employee(emp)        >Real estate(real)<         Cases(cases)        Contractor(con)    |
|_________________________________________________________________________________________________________________|
|                                                                                                                 |
|   Create New Real Estate                                                                                        |
|_________________________________________________________________________________________________________________|"""
        
        self.new_real = f"""|                                                                                                                 |
|      Real Eastete                                                                                               |
|                                                                                                                 |
            1 - address: {real.address}
            2 - size: {real.size}
            3 - rooms: {real.rooms}
            4 - amenities: {real.amenities}
            5 - location: {real.location}
|_________________________________________________________________________________________________________________|"""
        print(f"{self.header}\n{self.new_real}")
        while True:
            save = input("Do you want to save employee(y/n): ")
            if save == "y":
                return True
            elif save == "n":
                return False
            else:
                print("Invalid option")