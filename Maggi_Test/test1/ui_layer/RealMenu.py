from logic_layer.LLAPI import LLAPI
from models.RealEstate import RealEstate
from models.Case import Case

PRIORITY = ['low','medium','high']
AVAILABLE_LOCATIONS = ["Reykjavík", "Nuuk", "Kulusuk", "Þórshöfn", "Tingwall", "Longyearbyen" ]
CASE = 'CAS-'


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
#=============================User input functions begins here======================================================================
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
                result = self.search_realestate()
                self.prompt_input_search(result)
            elif command == "r": return
            else: print("invalid option, try again!")
            print(self.main_options)
# ------------------------------------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------------------------------------
# search for real estate
    def prompt_input_search(self, result):
        while True:
            print(self.real_est_options)
            command = input("Enter your input: ")
            if command == "1": self.edit_realestate(result.id)
            elif command == "2": self.create_case(result)
            elif command == "3": self.edit_case(result)   
            elif command == "r": return
            else: print("Invalid option, try again!")
# ------------------------------------------------------------------------------------------------------------------

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
            for location in AVAILABLE_LOCATIONS:
                print(location)
            location = str(input("Enter location: "))
            if location in AVAILABLE_LOCATIONS: return location
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
        value = int(input("How many apartments are the in your area: "))
        address, size, rooms, id, amenities, location = self.user_options("create")
        for apartment in range(0, value):
            real = RealEstate(address, size, rooms, id, amenities, location)
            self.llapi.create_realestate(real)
            id += 1
# ------------------------------------------------------------------------------------------------------------------
# Edit real estate
    def edit_realestate(self,result):
        edit_id = int(result.id)
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

#=============================Case functions begins here======================================================================

# ------------------------------------------------------------------------------------------------------------------
# það þarf að skoða þetta fall eihvða betur geta
# allavega hreinskrifa þetta eihvða 

    def create_case(self, result):
        all_cases = self.llapi.all_cases()
        id = CASE + str(len(all_cases) + 1)
        location = result.location
        subject = input("Enter subject: ")
        description = input("Enter description: ")
        while True:
            print('What priority?: ')
            for prio in PRIORITY:
                print(prio)
            priority = str(input("Enter priority: ")) #setja inn low/medium/high
            if priority in PRIORITY:
                break
        repeated = input("Is the case repeated(y/n)?: ")
        real_id = result.id
        emp_id = input("Enter your employee ID: ")

        case = Case(id,location,subject, description, priority, repeated, real_id, emp_id)
        self.llapi.create_case(case)        
# ------------------------------------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------------------------------------
# Edit Case
    def print_emp_as_menu(self, case):
        print(case.id)
        print(case.location)
        print(case.subject)
        print(case.description)
        print(case.priority)
        print(case.repeated)
        self.edit_options = f"""
        Case: {case.id}
        1 - Location: {case.location}
        2 - subject: {case.subject}
        3 - description: {case.description}
        4 - priority: {case.priority}
        5 - repeated: {case.repeated}
        r - return to previous menu
        """
        print(self.edit_options)

    def edit_case(self, real):
        print(real.id)
        case = self.llapi.search_case_real_id(real.id)
        if case == None:
            print("The case id was not found")
            print(self.edit_options) 
            return
        self.promt_edit(case)

    def promt_edit(self, case):
        while True:
            self.print_emp_as_menu(case)
            command = input("Enter edit option: ")
            
            if command == "1":
                case.location = self.location_in()
                self.llapi.edit_case(case)
            elif command == "2":
                case.subject = self.input_case_and_check("subject", lambda value : self.llapi.is_address_correct(value))
                self.llapi.edit_case(case)
            elif command == "3":
                case.description = self.input_case_and_check("description", lambda value : self.llapi.is_phone_correct(value))
                self.llapi.edit_case(case)
            elif command == "4":
                case.priority = self.input_case_and_check("priority", lambda value : self.llapi.is_phone_correct(value))
                self.llapi.edit_case(case)
            elif command == "5":
                case.repeated = self.input_case_and_check("repeated", lambda value : self.llapi.is_phone_correct(value))
                self.llapi.edit_case(case)
            elif command == "r":
                return
            else:
                print("Invalid option")