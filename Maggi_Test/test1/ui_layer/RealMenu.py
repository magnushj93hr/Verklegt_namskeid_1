from logic_layer.LLAPI import LLAPI
from models.RealEstate import RealEstate
from models.Case import Case

PRIORITY = ['low','medium','high']
AVAILABLE_LOCATIONS = ["Reykjavík", "Nuuk", "Kulusuk", "Þórshöfn", "Tingwall", "Longyearbyen" ]

class RealMenu:
    def __init__(self, llapi):
        self.llapi = llapi
        self.main_options = """
Real estate menu
1 - list all real estate
2 - create real estate
3 - search real estate
r - return to previous menu
"""

        self.real_est_options = """
Real estate search menu
1 - edit real estate
2 - create case
3 - edit case
r - return to previous menu
    """

# ------------------------------------------------------------------------------------------------------------------
# Menu options
    def draw_options(self):
        print(self.main_options)
        return self.prompt_input()

    def prompt_input(self):
        while True:
            command = input("Enter your input: ")
            if command == "1":
                all_real = self.llapi.all_realestate()
                for real in all_real:
                    print(real)
                self.sort_by_location()
            elif command == "2":
                self.create_realestate()
            elif command == "3":
                self.search_realestate()
                self.prompt_input_search()
            elif command == "r": return
            else: print("invalid option, try again!")
            print(self.main_options)

#=============================User input functions begins hear======================================================================

# ------------------------------------------------------------------------------------------------------------------
# Check if the input is valid and 
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
        id = self.input_and_check("id", lambda value : self.llapi.check_if_rel_id_correct(value)) if controller == "create" else 0
        amenities = input("Enter amenities seaparadid by (,): ").split(",")
        location = self.location_in()

        return address, size, rooms, int(id), amenities, location
# ------------------------------------------------------------------------------------------------------------------

#=============================Real Estate functions begins hear======================================================================

# ------------------------------------------------------------------------------------------------------------------
    def create_realestate(self):
        value = int(input("How many apartments are the in your aria: "))
        address, size, rooms, id, amenities, location = self.user_options("create")
        for apartment in range(0, value+1):
            real = RealEstate(address, size, rooms, id, amenities, location)
            self.llapi.create_realestate(real)
            id += 1
# ------------------------------------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------------------------------------
    def edit_realestate(self):
        edit_id = int(self.search_id)
        address, size, rooms, _, amentities, location = self.user_options(None)
        
        real = RealEstate(address, size, rooms, edit_id, amentities, location)        
        self.llapi.edit_realestate(real)
# ------------------------------------------------------------------------------------------------------------------

# --------------------------------------------------------------------------------------------------------------------
    def sort_by_location(self):
        while True:
            filter_input = input("Do you want to filter by location(y/n)?: ")
            if filter_input == 'y':
                filter_location = self.location_in()
                result = LLAPI().filter_realestate(filter_location)
                if result != []:
                    for row in result:
                        print(row)
                    break
                else: print("No real estate found.")
            else: break
# ------------------------------------------------------------------------------------------------------------------

#=============================Search functions begins hear======================================================================

# ------------------------------------------------------------------------------------------------------------------
# search for real estate
    def prompt_input_search(self):
        while True:
            print(self.real_est_options)
            command = input("Enter your input: ")
            if command == "1": self.edit_realestate()
            elif command == "2": self.create_case()
            elif command == "3": self.edit_case()   
            elif command == "r": return
            else: print("invalid option, try again!")
# ------------------------------------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------------------------------------
    def search_realestate(self):
        while True:
            print("Quit by entering (q)")
            self.search_id = input("Enter real estate id: ")
            if self.search_id != "q":
                result = LLAPI().search_realestate(self.search_id)
                if result == None:
                    print("Invalid ID")
                else:
                    print(result)
                    return result
            else: break
# ------------------------------------------------------------------------------------------------------------------

#=============================Case functions begins hear======================================================================

# ------------------------------------------------------------------------------------------------------------------
# það þarf að skoða þetta fall eihvða betur geta
# allavega hreinskrifa þetta eihvða 

    def create_case(self):
        id = input("Enter id for case: ")
        location = input("Enter the location: ")
        subject = input("Enter subject: ")
        description = input("Enter description: ")
        while True:
            print('What priority?: ')
            for prio in PRIORITY:
                print(prio)
            priority = str(input("Enter priority: "))
            if priority in PRIORITY:
                break
        repeated = input("Is the case repeated?: ")

        case = Case(id,location,subject, description, priority, repeated, self.search_id)
        self.llapi.create_case(case)        


# ------------------------------------------------------------------------------------------------------------------