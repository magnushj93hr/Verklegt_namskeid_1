from ui_layer.DestMenu import DestMenu
from ui_layer.EmpMenu import EmpMenu
from ui_layer.real_estate import RealEstate
from ui_layer.cases import Cases
from ui_layer.conductor import Conductor
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
|   >Home(home)<   Employee(emp)    Real estate(real)    Cases(cases)    Contuctor(con)    Deestination(dest)     |
|_________________________________________________________________________________________________________________|
|                                                                                                                 |
|   home:       //Goes to home screen                                                                             |
|   emp:        //Goes to employee screen                                                                         |
|   real:       //Goes to real estate screen                                                                      |
|   cases:      //Goes to cases screen                                                                            |
|   con:        //Goes to contractor screen                                                                       |
|   dest:       //Goes to destination screen, shows what destinations are available                               |
|_________________________________________________________________________________________________________________|
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
        print(self.options)
        self.prompt_input()

    def prompt_input(self):
        return_option = ""
        while True:
            command = input("Choose option: ")
            if command == "emp":
                emp_menu = EmpMenu(self.llapi, self.user)
                emp_menu.draw_options()
            elif command == "dest":
                dest_menu = DestMenu(self.llapi)
                dest_menu.draw_options()
            elif command == "real":
                real_menu = RealEstate(self.llapi)
                real_menu.draw_options()
            elif command == "cases":
                cases_menu = Cases(self.llapi)
                cases_menu.draw_options()
            elif command == "con":
                con_menu = Conductor(self.llapi)
                con_menu.draw_options()
            elif command == "r":
                return
            else:
                print("invalid option, try again!")
            if return_option == "m":
                return "m"
            print(self.options)