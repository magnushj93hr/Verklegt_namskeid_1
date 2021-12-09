
class EditCase:

    def __init__(self, llapi, user):
        self.llapi = llapi

# ------------------------------------------------------------------------------------------------------------------
# Edit Case
    def print_case_as_menu(self, case):
        self.edit_options_case = f"""
        Case: {case.id}

        1 - Location: {case.location}
        2 - subject: {case.subject}
        3 - description: {case.description}
        4 - priority: {case.priority}
        5 - repeated: {case.repeated}
        r - return to previous menu
        """
        print(self.edit_options_case)

    def edit_case(self, real):
        print(real.id)
        case = self.llapi.search_cases_for_real_id(real.id)
        if case == None:
            print("The case id was not found")
            return
        self.promt_edit_case(case)

    def promt_edit_case(self, case):
        while True:
            self.print_case_as_menu(case)
            command = input("Enter edit option: ")
            
            if command == "1":
                case.location = self.location_in()
                self.llapi.edit_case(case)
            elif command == "2":
                case.subject = input("Enter subject")
                self.llapi.edit_case(case)
            elif command == "3":
                case.description = input("Enter description: ")
                self.llapi.edit_case(case)
            elif command == "4":
                while True:
                    print('What priority?: ')
                    for prio in PRIORITY:
                        print(prio)
                    case.priority = str(input("Enter priority: ")) #setja inn low/medium/high
                    if case.priority in PRIORITY:
                        self.llapi.edit_case(case)
                        break 
            elif command == "5":
                case.repeated = input("Enter repeated(y/n): ")
                self.llapi.edit_case(case)
            elif command == "r":
                return
            else:
                print("Invalid option")
# ------------------------------------------------------------------------------------------------------------------