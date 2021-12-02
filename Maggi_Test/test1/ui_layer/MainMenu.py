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
    Main menu
1 - employee menu
2 - real estate menu
3 - case menu
4 - contractor menu
5 - location menu
6 - maintenance menu
r - return to previous menu
"""

    def draw_options(self):
        print(self.options)
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
            elif command == "r":
                return
            else:
                print("invalid option, try again!")
            if return_option == "m":
                return "m"
            print(self.options)

