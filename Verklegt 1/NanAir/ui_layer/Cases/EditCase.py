
PRIORITY = ['low','medium','high']

class EditCase:
    def __init__(self, llapi):
        self.llapi = llapi

# ------------------------------------------------------------------------------------------------------------------
# Edit Case
    def print_case_as_menu(self, case):
        self.header = f"""
      __|__                                                                                             __|__
*---o--(_)--o---*                                                                                 *---o--(_)--o---* 
___________________________________________________________________________________________________________________
|                                                                                                                 |
|       Home(home)        Employee(emp)        >Real estate(real)<         Cases(cases)        Contractor(con)    |
|_________________________________________________________________________________________________________________|
|                                                                                                                 |
|                                     - r        //Return to previous menu                                        |
|_________________________________________________________________________________________________________________|"""

        self.edit_options = f"""|                                                                                                                 |
|      Case: {case.id:101s}|
|                                                                                                                 |
|       1 - Location: {case.location:92s}|
|       2 - Subject: {case.subject:93s}|
|       3 - Description: {case.description:89s}|
|       4 - Priority: {case.priority:92s}|
|       5 - Repeated: {case.repeated:92s}|
|_________________________________________________________________________________________________________________|
"""
        self.llapi.clear()
        print(f"{self.header}\n{self.edit_options}")

    def promt_edit_case(self, case):
        while True:
            self.print_case_as_menu(case)
            command = input("Enter edit option: ")
            
            if command == "1":
                case.location = self.available_locations()
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
                if case.repeated == "y":
                    case.repeat_days = int(input("Enter how many days between cases: "))
                self.llapi.edit_case(case)
            elif command == "r":
                return
            else:
                print("Invalid option")


    def available_locations(self):
        """Displays available locations and returns the location the user chooses"""
        while True:
            print('Available locations to choose from: \n')
            for location in self.llapi.get_locations_name():
                print(location)
            print()
            location = str(input("Enter location: ")).lower().capitalize()
            if location not in self.llapi.get_locations_name():
                print("Invalid location")
            else:
                return location