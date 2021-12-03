from logic_layer.LLAPI import LLAPI
from models.RealEstate import RealEstate
from models.Case import Case


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
                self.prompt_input_search()
            elif command == "r":
                return
            else:
                print("invalid option, try again!")
            print(self.main_options)
    
    def create_realestate(self):
        address = input("Enter address: ")
        size = input("Enter size of real estate: ")
        rooms = input("Enter how many rooms are in the real estate: ")
        id = input("Enter ID of real estate: ")
        amenities = input("Enter amenities of real estate: ")
        location = input("Enter location of real estate: ")
        
        
        real = RealEstate(address, size, rooms, id, amenities, location)
        self.llapi.create_realestate(real)

    def search_realestate(self):
        while True:
            self.search_id = input("Enter real estate id: ")
            result = LLAPI().search_realestate(self.search_id)
            if result == None:
                print("Invalid ID")
            else:
                print(result)
                break
    

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

        print(f"you are editing real estate with the id: {edit_id}")
        print("You can't delete the real estate id.\n")
        address = str(input("Enter address: "))
        size = str(input("Enter size: "))
        rooms = str(input("Enter rooms: "))
        amentities = str(input("Enter amentities "))
        location = str(input("Enter location: "))

        real = RealEstate(address, size, rooms,edit_id, amentities, location)        
        self.llapi.edit_realestate(real)


    def create_case(self):
        id = input("Enter id for case: ")
        location = input("Enter the location: ")
        subject = input("Enter subject: ")
        description = input("Enter description: ")
        priority = input("Set priority: ")
        due_date = input("Enter due date: ")
        repeated = input("Is the case repeated?: ")
        
        case = Case(id,location,subject, description, priority, due_date, repeated, self.search_id)
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
