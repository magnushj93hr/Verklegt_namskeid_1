from logic_layer.LLAPI import LLAPI
from models.RealEstate import RealEstate
from models.Case import Case

PRIORITY = ['low','medium','high']

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
                filter_input = input("Do you want to filter by location(y/n)?: ")
                if filter_input == 'y':
                    filter_location = input('Enter location to filter by: ')
                    result = LLAPI().filter_realestate(filter_location)
                    for row in result:
                        print(row)
            elif command == "2":
                self.create_realestate()
            elif command == "3":
                self.search_realestate()
                self.get_cases(self.search_id)
                self.prompt_input_search()
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

    def search_realestate(self):
        while True:
            self.search_id = input("Enter real estate id: ")
            result = LLAPI().search_realestate(self.search_id)
            if result == None:
                print("Invalid ID")
            else:
                print(result)
                break
    
    def get_cases(self, search_id):
        result = self.llapi.get_cases(search_id)
        for case in result:
            print(case)


    def prompt_input_search(self):
        while True:
            print(self.real_est_options)
            command = input("Enter your input: ")
            if command == "1":
                self.edit_realestate()
            elif command == "2":
                self.create_case()
            elif command == "3":
                self.edit_case()   
            elif command == "r":
                return
            else:
                print("invalid option, try again!")

    def edit_realestate(self):
        edit_id = str(input("Enter real estate id: "))
        ready_to_continue = self.llapi.check_if_employee_exists(edit_id)
        if ready_to_continue != None:
            pass

        real = RealEstate(address, size, rooms,edit_id, amentities, location)        
        self.llapi.edit_realestate(real)


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

    def edit_case(self):
        edit_id = str(input("Enter case id: "))

        print(f"you are editing a case with the id: {edit_id}")
        print("You can't delete the case id.\n")
        
        location = str(input("Enter the location: "))
        subject = str(input("Enter the subject name: "))
        description = str(input("Enter description: "))
        priority = str(input("Enter priority: "))
        due_date = str(input("Enter due date: "))
        repeated = str(input("Is the case repeated?: "))
        

        case = Case(edit_id, location, subject, description, priority, due_date, repeated)        
        self.llapi.edit_case(case)  
