from models.Case import Case

CASE = 'CAS-'
PRIORITY = ['low','medium','high']

class CreateCase:
    
    def __init__(self, llapi, user):
        self.user = user
        self.llapi = llapi

    def priority_check(self):
        while True:
            print('What priority?: ')
            for prio in PRIORITY:
                print(prio)
            priority = str(input("Enter priority: ")) #setja inn low/medium/high
            if priority in PRIORITY:
                return priority

    def create_case(self, real_est):
        emp_id = self.user.user_id
        all_cases = self.llapi.all_cases()
        id = CASE + str(len(all_cases) + 1)
        location = real_est.location
        subject = input("Enter subject: ")
        description = input("Enter description: ")
        priority = self.priority_check()
        repeated = input("Is the case repeated(y/n)?: ")
        if repeated == "y":
            repeat_days = int(input("Enter how many days between cases: "))
        else:
            repeat_days = 0
        real_id = real_est.id
        
        case = Case(id,location,subject, description, priority, repeated, repeat_days, real_id, emp_id)
        save = self.print_case(case)
        if save:
            self.llapi.create_case(case)

    def print_case(self, case):
        layout = f"""
      __|__                                                                                             __|__
*---o--(_)--o---*                                                                                 *---o--(_)--o---* 
___________________________________________________________________________________________________________________
|                                                                                                                 |
|       Home        Employee          Real estate         >Cases<           Contractor           Location         |
|_________________________________________________________________________________________________________________|
|                                                                                                                 |
|      Case: {case.id:28s}Created by: {case.emp_id:61s}|
|                                                                                                                 |
|          Real estate ID: {case.real_est_id:87s}|
|                Location: {case.location:87s}|
|                 Subject: {case.subject:87s}|
|             Description: {case.description:87s}|
|                Priority: {case.priority:87s}|
|                Repeated: {case.repeated:87s}|
|           Repeated days: {case.repeat_days:<87d}|
|                    Date: {case.date:87s}|
|                  Status: {case.status:87s}|
|             Closed date: {case.closed_date:87s}|
|_________________________________________________________________________________________________________________|
"""
        print(layout)
        while True:
            save = input("Do you want to save(y/n):")
            if save == "y":
                return True
            elif save == "n":
                return False
            else:
                print("Invalid option")