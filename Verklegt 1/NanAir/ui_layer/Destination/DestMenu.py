class DestMenu:
    def __init__(self, llapi):
        self.llapi = llapi
        self.options = """
      __|__                                                                                             __|__
*---o--(_)--o---*                                                                                 *---o--(_)--o---* 
___________________________________________________________________________________________________________________
|                                                                                                                 |
|       >Home(home)<        Employee(emp)        Real estate(real)         Cases(cases)        Contractor(con)    |
|_________________________________________________________________________________________________________________|
|                                                                                                                 |
|   - cr        //Create new destination                                 - b           //Go back                  |
|_________________________________________________________________________________________________________________|
"""

    def draw_options(self):
        print(self.options)
        self.prompt_input()

    def prompt_input(self):
        while True:
            command = input("Choose option: ")
            if command == "cr":
                pass
            elif command == "b":
                return
            else:
                print("invalid option, try again!")
            if command == "m":
                return
            print(self.options)

