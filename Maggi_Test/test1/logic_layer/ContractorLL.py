from data_layer.DLAPI import DLAPI
from models.Contractor import Contractor


class ContractorLL:
    def __init__(self, dlapi):
        self.dlapi = dlapi
    
    def all_contractors(self):
        return self.dlapi.get_all_contractors()

    def create_contractor(self, contr):
        self.dlapi.create_contractor(contr)

if __name__ == "__main__":
    empLL = ContractorLL(DLAPI())
