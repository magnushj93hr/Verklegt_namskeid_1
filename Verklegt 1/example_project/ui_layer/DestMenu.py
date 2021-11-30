class DestMenu:
    def __init__(self, llapi):
        self.llapi = llapi
        self.options = """
Dest menu
1 - list all destinations
r - return to previous menu
"""

    def draw_options(self):
        print(self.options)
        self.prompt_input()

    def prompt_input(self):
        while True:
            command = input("Enter your input: ")
            if command == "1":
                print("dest menu")
            elif command == "r":
                return
            else:
                print("invalid option, try again!")
            print(self.options)

