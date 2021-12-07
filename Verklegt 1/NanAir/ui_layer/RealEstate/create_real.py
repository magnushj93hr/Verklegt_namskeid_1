from logic_layer.LLAPI import LLAPI
from models.RealEstate import RealEstate



PRIORITY = ['low','medium','high']
AVAILABLE_LOCATIONS = ["Reykjavík", "Nuuk", "Kulusuk", "Þórshöfn", "Tingwall", "Longyearbyen" ]

class CreateReal:
    def __init__(self, llapi, user):
        self.user = user
        self.llapi = llapi
        self.options = """
      __|__                                                                                             __|__
*---o--(_)--o---*                                                                                 *---o--(_)--o---* 
___________________________________________________________________________________________________________________
|                                                                                                                 |
|       Home(home)        Employee(emp)        >Real estate(real)<         Cases(cases)        Contractor(con)    |
|_________________________________________________________________________________________________________________|
|                                                                                                                 |
|   Create New Real Estate                                                                                        |
|_________________________________________________________________________________________________________________|
"""

    def draw_options(self):
        print(self.options)
        return self.create_realestate()

    def create_realestate(self):
        value = int(input("How many apartments are the in your area: "))
        address, size, rooms, id, amenities, location = self.user_options("create")
        for apartment in range(0, value+1):
            real = RealEstate(address, size, rooms, id, amenities, location)
            self.display_real(real)
            save = input("Do you want to save the information (yes/no)? ")
            if save == "yes":
                self.llapi.create_realestate(real)
                id += 1

    # Check if the input is valid
    def input_and_check(self, info_type, check_fun):
        while True:
            value = input(f"Enter the {info_type} of the real estate: ")
            if not check_fun(value): print(f"Invalid {info_type} for the real estate")
            else: return value

    def location_in(self):
        while True:
            print('Available locations to choose from:')
            for location in AVAILABLE_LOCATIONS:
                print(location)
            location = str(input("Enter location: "))
            if location in AVAILABLE_LOCATIONS:
                return location


    def user_options(self, controller):
        address = self.input_and_check("address", lambda value : self.llapi.is_address_correct(value))
        size = self.input_and_check("size", lambda value : self.llapi.check_if_size_correct(value))
        rooms = self.input_and_check("rooms", lambda value : self.llapi.check_if_room_correct(value))
        id = self.input_and_check("id", lambda value : self.llapi.check_if_rel_id_correct(value)) if controller == "create" else None
        amenities = input("Enter amenities seaparadid by (,): ").split(",")
        location = self.location_in()

        return address, size, rooms, int(id), amenities, location
# ------------------------------------------------------------------------------------------------------------------



    # def create_real_est(self):
    #     address = input("Enter real estate address: ")
    #     size = input("Enter real estate size: ")
    #     room = input("Enter how manu phone: ")
    #     location = input("Enter employee location: ")
    #     area = input("Enter employee area: ")
    #     supervisor = input("Is Supervisor(yes/no): ")
    #     real = RealEstate(address, size, rooms, id, amenities, location)
    #     self.display_emp(real)
    #     save = input("Do you want to save the information (yes/no)? ")
    #     if save == "yes":
    #         self.llapi.create_employee(emp)

    def display_real(self, real):
        header = """
      __|__                                                                                             __|__
*---o--(_)--o---*                                                                                 *---o--(_)--o---* 
___________________________________________________________________________________________________________________
|                                                                                                                 |
|       Home(home)        Employee(emp)        >Real estate(real)<         Cases(cases)        Contractor(con)    |
|_________________________________________________________________________________________________________________|
|                                                                                                                 |
|   Create New Real Estate                                                                                        |
|_________________________________________________________________________________________________________________|"""
        
        new_real = f"""|                                                                                                                |
|   Create New Real Estate                                                                                        |
|                                                                                                                 |
|                 Address: {real.name:87s}|
|                    Size: {real.emp_id:87s}|
|                   Rooms: {real.address:87s}|
|          Real estate ID: {real.homeline:87s}|
|               Amenities: {real.phone:87s}|
|                Location: {real.location:87s}|
|_________________________________________________________________________________________________________________|
"""

        print(header)
        print(new_real)