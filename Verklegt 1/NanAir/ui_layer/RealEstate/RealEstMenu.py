from os import system
from logic_layer.LLAPI import LLAPI
from ui_layer.RealEstate.CreateReal import CreateReal
from ui_layer.RealEstate.EditReal import EditReal
from ui_layer.RealEstate.SearchReal import SearchReal
from ui_layer.RealEstate.CreateCase import CreateCase
from ui_layer.RealEstate.EditCase import EditCase
from ui_layer.RealEstate.ListReal import ListReal



class RealEstMenu:
    def __init__(self, llapi, user):
        self.create_real = CreateReal(llapi, user)
        self.edit_real = EditReal(llapi, user)
        self.search_real = SearchReal(llapi, user)
        self.create_case = CreateCase(llapi, user)
        self.edit_case = EditCase(llapi, user)
        self.list_real = ListReal(llapi, user)
        self.user = user
        self.llapi = llapi
        self.header = """
      __|__                                                                                             __|__
*---o--(_)--o---*                                                                                 *---o--(_)--o---* 
___________________________________________________________________________________________________________________
|                                                                                                                 |
|       Home(home)        Employee(emp)        >Real estate(real)<         Cases(cases)        Contractor(con)    |
|_________________________________________________________________________________________________________________|
|                                                                                                                 |
|   - 1               //list all realestate                     - 2           //search real estate                |"""
        self.supervisorLine = """|   - 3               //Creates new estate                                                                        |"""
        self.footer = """|   - r               //return                                                                                    |
|_________________________________________________________________________________________________________________|
"""

    # def draw_options(self):
    #     #prints out menu bar
    #     self.print_options()
    #     return self.prompt_input()

    def print_options(self):
        #determines if menu bar should include supervisor options or not
        print(self.header)
        if self.user.is_supervisor():
            print(self.supervisorLine)
        print(self.footer)
    
    def prompt_input(self):
        while True:
            self.print_options()
            command = input("Choose option: ")
            if command == "1":
                self.llapi.clear()
                self.list_real.real_printer()
            elif command == "2":
                self.llapi.clear()
                result = self.search_real.search_realestate()
                if result is not None:
                    self.search_real.prompt_input_search(result)
            elif command == "3" and self.user.is_supervisor():
                self.llapi.clear()
                self.create_real.create_realestate()
            elif command == "r":
                self.llapi.clear()
                return "r"
            else:
                print("invalid option, try again!")
