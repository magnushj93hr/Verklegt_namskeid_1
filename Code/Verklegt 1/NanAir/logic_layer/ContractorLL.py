from data_layer.DLAPI import DLAPI
from models.Contractor import Contractor

MAX_NAME = 40
MAX_PHONE = 7
MAX_ADDRESS = 20


class ContractorLL:
    def __init__(self, dlapi):
        self.dlapi = dlapi
    
    def all_contractors(self):
        """Returns list of all contractors"""
        return self.dlapi.get_all_contractors()

    def create_contractor(self, contr):
        """Takes in information and creates case"""
        self.dlapi.create_contractor(contr)
    
    def search_contractor(self, name):
        """Takes in contractor name, searches and returns contractor"""
        all_contractors = self.all_contractors()
        for contractor in all_contractors:
            if contractor.name == name:
                return contractor
    
    def edit_contractor(self, contractor):
        """Takes in contractor and updates it"""
        return self.dlapi.edit_contractor(contractor)

    def get_contractors_name(self):
        """Returns a list of contractors names"""
        contractors_names = []
        all_contractors = self.all_contractors()
        for contractor in all_contractors:
            contractors_names.append(contractor.name)
        return contractors_names


if __name__ == "__main__":
    empLL = ContractorLL(DLAPI())
