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

    def create_contractor(self):
        name = input("Enter contractor name: ")
        contact = input("Enter contractor contact: ")
        phone = input("Enter contractor phone: ")
        opening_hours = input("Enter contractor opening hours: ")
        location = input("Enter contractor location: ")
        
        contr = Contractor(name, contact, phone, opening_hours, location)
        self.llapi.create_contractor(contr)

