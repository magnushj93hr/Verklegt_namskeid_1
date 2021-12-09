from models.Case import Case


class CreateCase:
    
    def __init__(self, llapi, user):
        self.llapi = llapi

    def priority_check(self):
        while True:
            print('What priority?: ')
            for prio in PRIORITY:
                print(prio)
            priority = str(input("Enter priority: ")) #setja inn low/medium/high
            if priority in PRIORITY:
                return priority

    def create_case_start(self):
        emp_id = input("Enter your supervisor ID: ").lower()
        result = LLAPI().search_employee(emp_id)
        try:
            result.id
            return result, emp_id
        except AttributeError:
            print("Invalid supervisor ID")
            return None, None

    def create_case(self, result):
        emp, emp_id = self.create_case_start()
        if emp != None:
            all_cases = self.llapi.all_cases()
            id = CASE + str(len(all_cases) + 1)
            location = result.location
            subject = input("Enter subject: ")
            description = input("Enter description: ")
            priority = self.priority_check()
            repeated = input("Is the case repeated(y/n)?: ")
            if repeated == "y":
                repeat_days = int(input("Enter how many days between cases: "))
            real_id = result.id
            
            case = Case(id,location,subject, description, priority, repeated, repeat_days, real_id, emp_id)
            self.llapi.create_case(case)