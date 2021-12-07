from data_layer.DLAPI import DLAPI
from models.Case import Case


class CaseLL:
    def __init__(self, dlapi):
        self.dlapi = dlapi
    
    def all_cases(self):
        cases = self.dlapi.get_all_cases()
        cases_listed = self.list_cases(cases)
        return cases_listed

    def create_case(self, case):
        self.dlapi.create_case(case)
    
    def edit_case(self, edit_id):
        self.dlapi.edit_case(edit_id)
    
<<<<<<< Updated upstream
    def search_case_real_id(self, real_id):
        all_cases = self.dlapi.get_all_cases()
        for case in all_cases:
            if case.real_est_id == real_id:
                return case
    
    def search_case(self, case_id):
=======
    def search_case(self, search_id, controller):
>>>>>>> Stashed changes
        all_cases = self.dlapi.get_all_cases()
        if controller == 'caseid':
            for case in all_cases:
                if case.id == search_id:
                    result = self.list_cases(case)
                    return result
        elif controller == 'empid':
            for case in all_cases:
                if case.emp_id == search_id:
                    result = self.list_cases(case)
                    return result
        elif controller == "realid":
            for case in all_cases:
                if case.real_est_id == search_id:
                    result = self.list_cases(case)
                    return result
            
    
    def list_cases(self, case):
        employees = self.dlapi.get_all_employees()
        try:
            if len(case) > 1:
                for i in case:
                    for employee in employees:
                        if i.emp_id == employee.id:
                            i.emp_id = employee.name
            return case
        
        except:
            for employee in employees:
                if case.emp_id == employee.id:
                    case.emp_id = employee.name
            return case
            

    def case_exist(self, id):
        all_cases = self.all_cases()
        pass
    def filter_cases(self, status):
        filtered_cases = []
        all_cases = self.all_cases()
        for case in all_cases:
            if case.status == status:
                filtered_cases.append(case)
        return filtered_cases

if __name__ == "__main__":
    empLL = CaseLL(DLAPI())
