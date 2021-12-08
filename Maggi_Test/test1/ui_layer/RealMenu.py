from logic_layer.LLAPI import LLAPI
from models.RealEstate import RealEstate
from models.Case import Case
import ast

PRIORITY = ['low','medium','high']
# AVAILABLE_LOCATIONS = ["Reykjavík", "Nuuk", "Kulusuk", "Þórshöfn", "Tingwall", "Longyearbyen" ]
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
                if result is not None:
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
            if command == "1": self.edit_real(result)
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
        value = int(input("How many apartments are the in your area: "))
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
# Edit real estate
    def print_real_as_menu(self, real):
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

    def edit_real(self, real):
            real = self.llapi.search_realestate(real.id)
            if real == None:
                print("The real estate id was not found")
                print(self.edit_options) 
                return
            self.promt_edit_real(real)

    def promt_edit_real(self, real):
            while True:
                self.print_real_as_menu(real)
                command = input("Enter edit option: ")
                
                if command == "1":
                    real.address = self.input_real_and_check("address", lambda value : self.llapi.is_address_correct(value))
                    self.llapi.edit_realestate(real)
                elif command == "2":
                    real.size = self.input_real_and_check("size", lambda value : self.llapi.check_if_size_correct(value))
                    self.llapi.edit_realestate(real)
                elif command == "3":
                    real.rooms = self.input_real_and_check("rooms", lambda value : self.llapi.check_if_room_correct(value))
                    self.llapi.edit_realestate(real)
                elif command == "4":
                    self.amenities_ui(real)
                    real.amenities = self.amenities_logic(real)
                    self.llapi.edit_realestate(real)
                elif command == "5":
                    real.location = self.location_in()
                    self.llapi.edit_realestate(real)
                elif command == "r":
                    return
                else:
                    print("Invalid option")

    def amenities_ui(self, ame):
        self.edit_ame = f"""
        Amenities: {ame.amenities}
        1 - Remove
        2 - Add
        """
        print(self.edit_ame)

    def amenities_logic(self, ame):
        input_ame = input("Enter a option: ")
        if input_ame == "1":
            list_ame = self.amenities_remove(ame)
        elif input_ame == "2":
            list_ame = self.amenities_add(ame)
        return list_ame

    def amenities_remove(self, ame):
        while True:
            print(ame.amenities)
            rem_input = input("Enter a amenitie to remove: ")
            if rem_input in ame.amenities: 
                new_list = ast.literal_eval(ame.amenities)
                new_list.remove(rem_input)
                return new_list
            else: print(f"{rem_input} is not in the amenities")

    def amenities_add(self, ame):
        print(ame.amenities)
        list_ame = input("Enter a amenities to add, seperated by(,): ").split(",")
        if ame.amenities == "":
            ame.amenities = []
        return ame.amenities.extend(list_ame)

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
            else: return None
# ------------------------------------------------------------------------------------------------------------------

#=============================Case functions begins here======================================================================

# ------------------------------------------------------------------------------------------------------------------
# það þarf að skoða þetta fall eihvða betur geta
# allavega hreinskrifa þetta eihvða 

    def priority_check(self):
        while True:
            print('What priority?: ')
            for prio in PRIORITY:
                print(prio)
            priority = str(input("Enter priority: ")) #setja inn low/medium/high
            if priority in PRIORITY:
                return priority

    def create_case_start(self):
        emp_id = input("Enter your supervisor ID: ")
        result = LLAPI().search_employee(emp_id)
        return result

    def create_case(self, result):
        emp = self.create_case_start()
        if emp.id.split("-")[0] == "air":
            all_cases = self.llapi.all_cases()
            id = CASE + str(len(all_cases) + 1)
            location = result.location
            subject = input("Enter subject: ")
            description = input("Enter description: ")
            priority = self.priority_check()
            repeated = input("Is the case repeated(y/n)?: ")
            real_id = result.id

        case = Case(id,location,subject, description, priority, repeated, repeat_days, real_id, emp_id)
        self.llapi.create_case(case)        
# ------------------------------------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------------------------------------
# Edit Case
    def print_case_as_menu(self, case):
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
        case = self.llapi.search_cases_for_real_id(real.id)
        if case == None:
            print("The case id was not found")
            print(self.edit_options) 
            return
        self.promt_edit_case(case)

    def promt_edit_case(self, case):
        while True:
            self.print_case_as_menu(case)
            command = input("Enter edit option: ")
            
            if command == "1":
                case.location = self.location_in()
                self.llapi.edit_case(case)
            elif command == "2":
                case.subject = input("Enter subject")
                self.llapi.edit_case(case)
            elif command == "3":
                case.description = input("Enter description: ")
                self.llapi.edit_case(case)
            elif command == "4":
                while True:
                    print('What priority?: ')
                    for prio in PRIORITY:
                        print(prio)
                    case.priority = str(input("Enter priority: ")) #setja inn low/medium/high
                    if case.priority in PRIORITY:
                        self.llapi.edit_case(case)
                        break 
            elif command == "5":
                case.repeated = input("Enter repeated(y/n): ")
                self.llapi.edit_case(case)
            elif command == "r":
                return
            else:
                print("Invalid option")