from logic_layer.LLAPI import LLAPI

class RealEstate:
    def __init__(self, llapi, user):
        self.user = user
        self.llapi = llapi
        self.header = """
      __|__                                                                                             __|__
*---o--(_)--o---*                                                                                 *---o--(_)--o---* 
___________________________________________________________________________________________________________________
|                                                                                                                 |
|       Home(home)        Employee(emp)        Real estate(real)         >Cases(cases)<        Contractor(con)    |
|_________________________________________________________________________________________________________________|
|                                                                                                                 |
|   - s               //Search for estate                       - fi          //Filter options                    |
|   - b               //Go back                                                                                   |"""
        self.supervisorLine = """|   - cr              //Creates new estate                                                                        |"""

        self.footer = """|_________________________________________________________________________________________________________________|
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
        while True:
            command = input("Choose option: ")
            if command == "s":
                pass
                # all_emps = self.llapi.all_employees()
                # for emp in all_emps:
                #     print(emp)
            elif command == "cr" and self.user.is_supervisor():
                pass
            elif command == "fi":
                pass
            elif command == "e":
                pass
            elif command == "b":
                return "b"
            elif command == "m":
                return "m"
            else:
                print("invalid option, try again!")
            print(self.options)