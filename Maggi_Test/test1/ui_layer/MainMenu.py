from ui_layer.RealMenu import RealMenu
from ui_layer.EmpMenu import EmpMenu
from ui_layer.CaseMenu import CaseMenu
from ui_layer.ContractorMenu import ContractorMenu
from ui_layer.LocMenu import LocMenu
from ui_layer.MaintenanceMenu import MaintenanceMenu
from logic_layer.LLAPI import LLAPI

class MainMenu:
    def __init__(self):
        self.llapi = LLAPI()
        self.options = """
      __|__                                                                                             __|__
*---o--(_)--o---*                                                                                 *---o--(_)--o---* 
___________________________________________________________________________________________________________________
|                                                                                                                 |
|       >Home<        Employee        Real estate         Cases        Contractor        Location                 |
|_________________________________________________________________________________________________________________|
|                                                                                                                 |
|   - 1         //Goes to employee menu                                             - q         //Quit            |
|   - 2         //Goes to real estate menu                                                                        |
|   - 3         //Goes to case menu                                                                               |
|   - 4         //Goes to contractor menu                                                                         |
|   - 5         //Goes to location menu                                                                           |"""
        self.supervisorLine = """|   - dest        //Goes to destination screen, shows what destinations are available                             |"""
        self.footer = """|_________________________________________________________________________________________________________________|
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


    def draw_options(self):
        print(self.options)
        print(self.footer)
        self.prompt_input()

    def prompt_input(self):
        return_option = ""
        while True:
            command = input("Enter your input: ")
            if command == "1":
                emp_menu = EmpMenu(self.llapi)
                return_option = emp_menu.draw_options()
            elif command == "2":
                real_menu = RealMenu(self.llapi)
                real_menu.draw_options()
            elif command == '3':
                case_menu = CaseMenu(self.llapi)
                case_menu.draw_options()
            elif command == '4':
                case_menu = ContractorMenu(self.llapi)
                case_menu.draw_options()
            elif command == "5":
                loc_menu = LocMenu(self.llapi)
                loc_menu.draw_options()
            elif command == "6":
                maint_menu = MaintenanceMenu(self.llapi)
                maint_menu.draw_options()
            elif command == "q":
                print("Thanks for using NaN air")
                return
            else:
                print("Invalid option, try again!")
            if return_option == "m":
                return "m"
            print(self.options)
            print(self.footer)