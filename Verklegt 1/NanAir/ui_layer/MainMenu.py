import os

from ui_layer.Employee.EmpMenu import EmpMenu
from ui_layer.RealEstate.RealEstMenu import RealEstMenu
from ui_layer.Cases.CaseMenu import CaseMenu
from ui_layer.Contractor.ContractorMenu import ContractorMenu
from ui_layer.Location.LocationMenu import LocationMenu
from logic_layer.LLAPI import LLAPI


class MainMenu:
    def __init__(self, user):
        self.user = user
        self.llapi = LLAPI()
        self.options = """
      __|__                                                                                             __|__
*---o--(_)--o---*                                                                                 *---o--(_)--o---* 
___________________________________________________________________________________________________________________
|                                                                                                                 |
|       >Home<        Employee          Real estate         Cases           Contractor           Location         |
|_________________________________________________________________________________________________________________|
|                                                                                                                 |
|   - 1         //Goes to employee menu                                             - q         //Quit            |
|   - 2         //Goes to real estate menu                                                                        |
|   - 3         //Goes to case menu                                                                               |
|   - 4         //Goes to contractor menu                                                                         |
|   - 5         //Goes to location menu                                                                           |
|_________________________________________________________________________________________________________________|
|                                                                                                                 |
|                                                                                                                 |
|                                                      |                                                          |
|                                                      |                                                          |
|                            .''.         .''. `._    _|_    _.' .''.         .''.                                |
|                             '. '.     .' .'     ~-./ _ \.-~     '. '.     .' .'                                 |
|                               '. '._.' .'         /_/_\_\         '. '._.' .'                                   |
|            .----~~~~-----......-'.' '.'`~-.____.-~       ~-..____.-~'.' '.'`-......-----~~~~---.                |
|            '---~~~~----....__  .''._.'.              .              .'._.''.  ___....----~~~~--'                |
|                              .' .'__'. '._..__               __.._.' .'__'. '.                                  |
|                            .' .'||    '. '.   ~-.._______..-~   .' .'    ||'. '.                                |
|                           '.,'  ||-.    ',.'        |_|        '.,'    .-||  ',.'                               |
|                                 \| |                .'.                | |/                                     |
|                                  | |                | |                | |                                      |
|                                  '.'                '.'                '.'                                      |
|                                                                                                                 |
|_________________________________________________________________________________________________________________|
"""

    # def draw_options(self):
    #     print(self.options)
    #     self.prompt_input()

    def prompt_input(self):
        """Asks user to enter main menu option"""
        return_option = ""
        while True:
            self.llapi.clear()
            print(self.options)
            command = input("Enter your input: ")
            if command == "1":
                emp_menu = EmpMenu(self.llapi, self.user)
                return_option = emp_menu.prompt_input()
            elif command == "2":
                real_menu = RealEstMenu(self.llapi, self.user)
                real_menu.prompt_input()
            elif command == '3':
                case_menu = CaseMenu(self.llapi, self.user)
                case_menu.prompt_input()
            elif command == '4':
                con_menu = ContractorMenu(self.llapi, self.user)
                con_menu.prompt_input()
            elif command == "5":
                if self.user.is_supervisor() == True:
                    loc_menu = LocationMenu(self.llapi, self.user)
                    loc_menu.draw_options()
                else: print("That option is not available for a employee")
            elif command == "q":
                print("Thanks for using NaN air")
                return
            else:
                print("Invalid option, try again!")
            if return_option == "m":
                continue
