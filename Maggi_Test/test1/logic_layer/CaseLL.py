from data_layer.DLAPI import DLAPI
from models.Case import Case


class CaseLL:
    def __init__(self, dlapi):
        self.dlapi = dlapi
    
    def all_cases(self):
        return self.dlapi.get_all_cases()

    def create_case(self, case):
        self.dlapi.create_case(case)
    
    def edit_case(self, edit_id):
        self.dlapi.edit_case(edit_id)
    
    def search_case(self, case_id):
        all_cases = self.dlapi.get_all_cases()
        for case in all_cases:
            if case.id == case_id:
                return case

if __name__ == "__main__":
    empLL = CaseLL(DLAPI())
