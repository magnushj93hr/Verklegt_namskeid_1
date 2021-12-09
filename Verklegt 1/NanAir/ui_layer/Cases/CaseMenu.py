from logic_layer.LLAPI import LLAPI

class CaseMenu:
    def __init__(self, llapi, user):
        self.user = user
        self.llapi = llapi
        self.options = """
      __|__                                                                                             __|__
*---o--(_)--o---*                                                                                 *---o--(_)--o---* 
___________________________________________________________________________________________________________________
|                                                                                                                 |
|       Home(home)        Employee(emp)        Real estate(real)         >Cases(cases)<        Contractor(con)    |
|_________________________________________________________________________________________________________________|
|                                                                                                                 |
|   - s              //Search for cases                        - fi         //Filter options                      |
|   - b              //Go back                                                                                    |
|_________________________________________________________________________________________________________________|
"""

    def draw_options(self):
        print(self.options)
        return self.prompt_input()


    def prompt_input(self):
        while True:
            command = input("Choose option: ")
            if command == "s":
                pass
                # all_emps = self.llapi.all_employees()
                # for emp in all_emps:
                #     print(emp)
            elif command == "fi":
                pass
                pass
            elif command == "b":
                return "b"
            elif command == "m":
                return "m"
            else:
                print("invalid option, try again!")
            print(self.options)