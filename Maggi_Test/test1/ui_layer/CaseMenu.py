from logic_layer.LLAPI import LLAPI
from models.Case import Case

class CaseMenu:
    def __init__(self, llapi):
        self.llapi = llapi
        self.options = """
Case menu
1 - list all cases
2 - edit case
3 - search for case
r - return to previous menu
"""
# ------------------------------------------------------------------------------------------------------------------
# menu input
    def draw_options(self):
        print(self.options)
        return self.prompt_input()

    def prompt_input(self):
        while True:
            command = input("Enter your input: ")
            if command == "1":
                all_cases = self.llapi.all_cases()
                for case in all_cases:
                    print(case)
            elif command == "2":
                self.edit_case()
            elif command == "3":
                self.search_case()
            elif command == "r":
                return "r"
            else:
                print("invalid option, try again!")
            print(self.options)
# ------------------------------------------------------------------------------------------------------------------


    def search_case(self):
        search_id = input("Enter case id: ")
        result = LLAPI().search_case(search_id)
        print(result)