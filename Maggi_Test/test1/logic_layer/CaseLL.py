from data_layer.DLAPI import DLAPI
from models.Case import Case


class CaseLL:
    def __init__(self, dlapi):
        self.dlapi = dlapi
    
    def all_cases(self):
        return self.dlapi.get_all_cases()

    def create_case(self, case):
        self.dlapi.create_case(case)

if __name__ == "__main__":
    empLL = CaseLL(DLAPI())
