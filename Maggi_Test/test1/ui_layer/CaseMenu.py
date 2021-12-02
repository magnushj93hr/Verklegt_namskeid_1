from logic_layer.LLAPI import LLAPI
from models.Case import Case

class CaseMenu:
    def __init__(self, llapi):
        self.llapi = llapi
        self.options = """
Employee menu
1 - list all cases
2 - create a new case
3 - edit case
r - return to previous menu
"""

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
                self.create_case()
            elif command == "3":
                self.edit_case()
            elif command == "r":
                return "r"
            else:
                print("invalid option, try again!")
            print(self.options)

    def create_case(self):
        id = input("Enter id for case: ")
        subject = input("Enter subject: ")
        description = input("Enter description ")
        priority = input("Set priority: ")
        due_date = input("Enter due date: ")
        repeated = input("Is the case repeated?: ")
        
        case = Case(id,subject, description, priority, due_date, repeated)
        self.llapi.create_case(case)
    def edit_case(self):
        edit_id = str(input("Enter case id: "))

        print(f"you are editing a case with the id: {edit_id}")
        print("You can't delete the case id.\n")
        
        subject = str(input("Enter the subject name: "))
        description = str(input("Enter description: "))
        priority = str(input("Enter priority: "))
        due_date = str(input("Enter due date: "))
        repeated = str(input("Is the case repeated?: "))
        

        case = Case(edit_id, subject, description, priority, due_date, repeated)        
        self.llapi.edit_case(case)
