from logic_layer.LLAPI import LLAPI
from models.Case import Case

PRIORITY = ['low','medium','high']

class CaseMenu:
    def __init__(self, llapi):
        self.llapi = llapi
        self.options = """
Employee menu
1 - list all cases
2 - create a new case
3 - edit case
4 - search for case
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
            elif command == '4':
                self.search_case()
            elif command == "r":
                return "r"
            else:
                print("invalid option, try again!")
            print(self.options)

    def create_case(self):
        
        id = input("Enter id for case: ")
        location = input("Enter the location: ")
        subject = input("Enter subject: ")
        description = input("Enter description: ")
        while True:
            print('What priority?: ')
            for prio in PRIORITY:
                print(prio)
            priority = str(input("Enter priority: "))
            if priority in PRIORITY:
                break
        repeated = input("Is the case repeated?: ")
        
        
        case = Case(id,location,subject, description, priority, repeated)
        self.llapi.create_case(case)
        
        
    def edit_case(self):
        edit_id = str(input("Enter case id: "))

        print(f"you are editing a case with the id: {edit_id}")
        print("You can't delete the case id.\n")
        
        location = str(input("Enter the location: "))
        subject = str(input("Enter the subject name: "))
        description = str(input("Enter description: "))
        priority = str(input("Enter priority: "))
        repeated = str(input("Is the case repeated?: "))
        

        case = Case(edit_id, location, subject, description, priority, repeated)        
        self.llapi.edit_case(case)
    
    def search_case(self):
        search_id = input("Enter case id: ")
        result = LLAPI().search_case(search_id)
        print(result)