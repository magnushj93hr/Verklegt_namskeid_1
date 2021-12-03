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

    def user_options(self):
        while True:
            name = input("Enter contractor name: ")
            name_c = self.llapi.check_if_name_correct(name)
            if name_c == False:
                print("invalid contractor name")
            else: break
#----
        while True:
            phone = input("Enter contractor phone number: ")
            phone_c = self.llapi.check_if_phone_correct(phone)
            if phone_c == False:
                print("invalid contractor phone number")
            else: break
#----
        while True:
            contact = input("Enter contractor contact: ")
            contact_c = self.llapi.check_if_location_correct(contact)
            if contact_c == False:
                print("invalid contracotr contact")
            else: break
#----
        while True:
            location = input("Enter contractor location: ")
            location_c = self.llapi.check_if_location_correct(location)
            if location_c == False:
                print("invalid Contractor location")
            else: break
#----
        while True:
            open = input("Enter opening hours for contractor: ")
            open_c = self.llapi.check_if_location_correct(open)
            if open_c == False:
                print("invalid opening hours for Contractor ")
            else: break
#----
        return name, phone, contact, location, open

    def create_contractor(self):
        name, phone, contact, location, opening_hours = self.user_options()        
        contr = Contractor(name, contact, phone, opening_hours, location)
        self.llapi.create_contractor(contr)

