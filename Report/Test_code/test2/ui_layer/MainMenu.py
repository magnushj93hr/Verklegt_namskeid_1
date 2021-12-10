from ui_layer.DestMenu import DestMenu
from ui_layer.EmpMenu import EmpMenu
from logic_layer.LLAPI import LLAPI

class MainMenu:
    def __init__(self):
        self.llapi = LLAPI()
        self.options = """
    Main menu
1 - employee menu
2 - destination menu
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
                dest_menu = DestMenu(self.llapi)
                dest_menu.draw_options()
            elif command == "r":
                return
            else:
                print("invalid option, try again!")
            if return_option == "m":
                return "m"
            print(self.options)


