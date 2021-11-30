from ui_layer.Destination.DestMenu import DestMenu
from ui_layer.Employee.EmpMenu import EmpMenu
from ui_layer.RealEstate.real_estate_menu import RealEstate
from ui_layer.Cases.cases_menu import Cases
from ui_layer.Contractor.contractor_menu import Contractor
from logic_layer.LLAPI import LLAPI

class MainMenu:
    def __init__(self, user):
        self.user = user
        self.llapi = LLAPI()
        self.header = """
      __|__                                                                                             __|__
*---o--(_)--o---*                                                                                 *---o--(_)--o---* 
___________________________________________________________________________________________________________________
|                                                                                                                 |
|       >Home(home)<        Employee(emp)        Real estate(real)         Cases(cases)        Contractor(con)    |
|_________________________________________________________________________________________________________________|
|                                                                                                                 |
|   - home        //Goes to home screen                                             - quit         //Quit         |
|   - emp         //Goes to employee screen                                                                       |
|   - real        //Goes to real estate screen                                                                    |
|   - cases       //Goes to cases screen                                                                          |
|   - con         //Goes to contractor screen                                                                     |"""
        self.supervisorLine = """|   - dest        //Goes to destination screen, shows what destinations are available                             |"""
        self.footer = """|_________________________________________________________________________________________________________________|
|                                                                                                                 |
|                                                                                                                 |
|                                                      |                                                          |
|                                                      |                                                          |
|                            .''.         .''. `._    _|_    _.' .''.         .''.                                |
|                             '. '.     .' .'     ~-./ _ \.-~     '. '.     .' .'                                 |
|             ____              '. '._.' .'         /_/_\_\         '. '._.' .'               ____                |
|            '.__ ~~~~-----......-'.' '.'`~-.____.-~       ~-..____.-~'.' '.'`-......-----~~~~ __.'               |
|                ~~~~----....__  .''._.'.              .              .'._.''.  ___....----~~~~                   |
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
        #prints out menu bar
        self.print_options()
        return self.prompt_input()

    def print_options(self):
        #determines if menu bar should include supervisor options or not
        print(self.header)
        if self.user.is_supervisor():
            print(self.supervisorLine)
        print(self.footer)

    def prompt_input(self):
        # return_option = ""
        while True:
            command = input("Choose option: ")
            if command == "emp":
                emp_menu = EmpMenu(self.llapi, self.user)
                emp_menu.draw_options()
            elif command == "dest" and self.user.is_supervisor():
                dest_menu = DestMenu(self.llapi)
                dest_menu.draw_options()
            elif command == "real":
                real_menu = RealEstate(self.llapi, self.user)
                real_menu.draw_options()
            elif command == "cases":
                cases_menu = Cases(self.llapi, self.user)
                cases_menu.draw_options()
            elif command == "con":
                con_menu = Contractor(self.llapi, self.user)
                con_menu.draw_options()
            elif command == "quit":
                return
            else:
                print("invalid option, try again!")
            # if return_option == "m":
            #     return "m"
            print(self.options)


