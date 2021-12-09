from data_layer.DLAPI import DLAPI
from models.Case import Case


class CaseLL:
    def __init__(self, dlapi):
        self.dlapi = dlapi
    
    def all_cases(self):

        """Returns list of all cases"""
        cases = self.dlapi.get_all_cases()
        cases_listed = self.list_cases(cases)
        return cases_listed

    def create_case(self, case):
        """Takes in information and creates case"""
        self.dlapi.create_case(case)
    
    def edit_case(self, case):
        """Takes in a case and updates it """
        self.dlapi.edit_case(case)
    
    def search_case(self, search_id, controller):
        """Takes in id and searches for case"""
        all_cases = self.dlapi.get_all_cases()
        case_list = []
        if controller == 'caseid':
            for case in all_cases:
                if case.id == search_id:
                    result = self.list_cases(case)
                    case_list.append(result)
            return case_list
        elif controller == 'empid':
            for case in all_cases:
                if case.emp_id == search_id:
                    result = self.list_cases(case)
                    case_list.append(result)
            return case_list
        elif controller == "realid":
            for case in all_cases:
                if case.real_est_id == search_id:
                    result = self.list_cases(case)
                    case_list.append(result)
            return case_list

    def search_cases_for_real_id(self, search_id):
        """Takes in id and searches for real estate"""
        
        all_cases = self.dlapi.get_all_cases()
        for case in all_cases:
            if case.real_est_id == search_id:
                return case 

    def get_case(self, search_id):
        """Takes in id and returns case"""

        all_cases = self.dlapi.get_all_cases()
        for case in all_cases:
            if case.id == search_id:
                return case 
    
    def list_cases(self, case):
        """Takes in case and changes employee id to employee name"""
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
            

<<<<<<< Updated upstream
=======
    
>>>>>>> Stashed changes
    def filter_cases(self, status):
        """Returns cases by status of case"""
        filtered_cases = []
        all_cases = self.all_cases()
        for case in all_cases:
            if case.status == status:
                filtered_cases.append(case)
        return filtered_cases

if __name__ == "__main__":
    empLL = CaseLL(DLAPI())
