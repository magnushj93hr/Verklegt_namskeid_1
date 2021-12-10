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
|       Home        Employee          Real estate         >Cases<           Contractor           Location         |
|_________________________________________________________________________________________________________________|
|                                                                                                                 |
|       - 1         //Create new destination                        - r         //Return to previous menu         |
|_________________________________________________________________________________________________________________|
"""

    def draw_options(self):
        print(self.options)
        self.prompt_input()

    def prompt_input(self):
        while True:
            command = input("Choose option: ")
            if command == "1":
                self.create_location.create_location()
            elif command == "r":
                return "r"
            else:
                print("invalid option, try again!")
            if command == "m":
                return
            print(self.options)

