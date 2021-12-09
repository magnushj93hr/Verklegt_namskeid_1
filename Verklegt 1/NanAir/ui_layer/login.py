from ui_layer.MainMenu import MainMenu
from ui_layer.user import User

class Login:
    def __init__(self):
        self.screen = """
         __      __       .__                                   __              _______           _______         _____  .__        
        /  \    /  \ ____ |  |   ____  ____   _____   ____    _/  |_  ____      \      \ _____    \      \       /  _  \ |__|______ 
        \   \/\/   // __ \|  | _/ ___\/  _ \ /     \_/ __ \   \   __\/  _ \     /   |   //__  \   /   |   \     /  /_\  \|  \_  __ /
         \        /\  ___/|  |_\  \__(  <_> )  Y Y  \  ___/    |  | (  <_> )   /    |    \/ __ \_/    |    \   /    |    \  ||  | \/
          \__/\  /  \___  >____/\___  >____/|__|_|  /\___  >   |__|  \____/    \____|__  (____  /\____|__  /   \____|__  /__||__|   
               \/       \/          \/            \/     \/                            \/     \/         \/            \/           


                                                           |
                                                           |
                                 .''.         .''. `._    _|_    _.' .''.         .''.
                                  '. '.     .' .'     ~-./ _ \.-~     '. '.     .' .'
                  ____              '. '._.' .'         /_/_\_\         '. '._.' .'               ____
                 '.__ ~~~~-----......-'.' '.'`~-.____.-~       ~-..____.-~'.' '.'`-......-----~~~~ __.'
                     ~~~~----....__  .''._.'.              .              .'._.''.  ___....----~~~~
                                   .' .'__'. '._..__               __.._.' .'__'. '.
                                 .' .'||    '. '.   ~-.._______..-~   .' .'    ||'. '.
                                '.,'  ||-.    ',.'        |_|        '.,'    .-||  ',.'
                                      \| |                .'.                | |/
                                       | |                | |                | |
                                       '.'                '.'                '.


                                                  
"""

    def draw_login(self):
        print(self.screen)
        self.promt_input()

    def promt_input(self):
        user_id = input("Enter ID: ")
        user = User(user_id)
        main_menu = MainMenu(user)
        main_menu.prompt_input()
