from logic_layer.LLAPI import LLAPI
from models.Contractor import Contractor

class ContractorMenu:
    def __init__(self, llapi):
        self.llapi = llapi
        self.options = """
contractor menu
1 - list all contractors
2 - create a new contractor
r - return to previous menu
"""

    def draw_options(self):
        print(self.options)
        return self.prompt_input()

    def prompt_input(self):
        while True:
            command = input("Enter your input: ")
            if command == "1":
                all_contrs = self.llapi.all_contractors()
                for contr in all_contrs:
                    print(contr)
            elif command == "2":
                self.create_contractor()
            elif command == "r":
                return "r"
            else:
                print("invalid option, try again!")
            print(self.options)

#------------------------------------------------------------------------------------------
# User options and check if correct:
    def input_and_check(self, info_type, check_fun):
        while True:
            value = input(f"Enter {info_type} for contractor: ")
            if not check_fun(value):
                print(f"Invalid {info_type} for contractor!")
            else:
                return value

    def user_options(self):
        name = self.input_and_check("name", lambda value : self.llapi.is_name_correct(value))
        phone = self.input_and_check("phone number", lambda value : self.llapi.is_phone_correct(value))
        contact = self.input_and_check("contact", lambda value : self.llapi.is_address_correct(value))
        location = self.input_and_check("location", lambda value : self.llapi.is_address_correct(value))
        open = self.input_and_check("opening hours", lambda value : self.llapi.is_address_correct(value))
        return name, phone, contact, location, open
#------------------------------------------------------------------------------------------

    def create_contractor(self):
        name, phone, contact, location, opening_hours = self.user_options()        
        contr = Contractor(name, contact, phone, opening_hours, location)
        self.llapi.create_contractor(contr)

