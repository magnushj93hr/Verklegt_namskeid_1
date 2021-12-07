from models.Case import Case

PRIORITY = ['low','medium','high']

class CreateCase:
    def __init__(self, llapi, user):
        self.user = user
        self.llapi = llapi
        self.options = """
      __|__                                                                                             __|__
*---o--(_)--o---*                                                                                 *---o--(_)--o---* 
___________________________________________________________________________________________________________________
|                                                                                                                 |
|       Home(home)         Employee(emp)         >Real estate(real)<       Cases(cases)        Contractor(con)    |
|_________________________________________________________________________________________________________________|
|                                                                                                                 |
|   Create New Case                                                                                               |
|_________________________________________________________________________________________________________________|
"""

    def draw_options(self):
        print(self.options)
        return self.create_case()

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

        case = Case(id,location,subject, description, priority, repeated, self.search_id) 
        self.display_case(case)
        save = input("Do you want to save the information (yes/no)? ")
        if save == "yes":
            self.llapi.create_case(case)

    def display_case(self, case):
        header = """
      __|__                                                                                             __|__
*---o--(_)--o---*                                                                                 *---o--(_)--o---* 
___________________________________________________________________________________________________________________
|                                                                                                                 |
|       Home(home)         Employee(emp)         Real estate(real)         Cases(cases)        Contractor(con)    |
|_________________________________________________________________________________________________________________|
|                                                                                                                 |
|   Create New Case                                                                                               |
|_________________________________________________________________________________________________________________|"""
        
        new_case = f"""|                                                                                                                 |
|   Create new case for real estate: {case.self.search_id:77s}|                                                   
|                                                                                                                 |
|                 Case ID: {case.id:87s}|                                                                          
|                Location: {case.location:87s}|
|                 Subject: {case.subject:87s}|
|             Description: {case.description:87s}|
|                Priority: {case.priority:87s}|
|                Repeated: {case.repeated:87s}|
|_________________________________________________________________________________________________________________|
"""

        print(header)
        print(new_case)