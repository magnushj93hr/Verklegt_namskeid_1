from ui_layer.Location.CreateLocation import CreateLocation


class LocationMenu:
    def __init__(self, llapi, user):
        self.create_location = CreateLocation(llapi, user)
        self.llapi = llapi
        self.user = user
        self.options = """
      __|__                                                                                             __|__
*---o--(_)--o---*                                                                                 *---o--(_)--o---* 
___________________________________________________________________________________________________________________
|                                                                                                                 |
|       >Home(home)<        Employee(emp)        Real estate(real)         Cases(cases)        Contractor(con)    |
|_________________________________________________________________________________________________________________|
|                                                                                                                 |
|       - 1         //Create new destination                        - r         //Return to previous menu         |
|_________________________________________________________________________________________________________________|
"""

    def draw_options(self):
        self.llapi.clear()
        print(self.options)
        self.prompt_input()

    def prompt_input(self):
        while True:
            command = input("Choose option: ")
            if command == "1":
                self.create_location.create_location()
            elif command == "r":
                self.llapi.clear()
                return "r"
            else:
                print("invalid option, try again!")
            if command == "m":
                return
            print(self.options)

