from data_layer.DLAPI import DLAPI
from models.Contractor import Contractor

MAX_NAME = 40
MAX_ID = 4
MAX_PHONE = 7
MAX_ADDRESS = 20


class ContractorLL:
    def __init__(self, dlapi):
        self.dlapi = dlapi
    
    def all_contractors(self):
        """Returns list of all contractors"""
        return self.dlapi.get_all_contractors()

    def create_contractor(self, contr):
        """Takes in """
        self.dlapi.create_contractor(contr)
    
    def search_contractor(self, name):
        all_contractors = self.all_contractors()
        for contractor in all_contractors:
            if contractor.name == name:
                return contractor
    
    def edit_contractor(self, contractor):
        return self.dlapi.edit_contractor(contractor)

    def get_contractors_name(self):
        contractors_names = []
        all_contractors = self.all_contractors()
        for contractor in all_contractors:
            contractors_names.append(contractor.name)
        return contractors_names
        
# ----------------------------------------------------------------
# INPUT CHECK
    def check_if_name_correct(self, name):
        if len(name) <= MAX_NAME:
            if not name.isdigit():
                return True
        return False
    def check_if_id_correct(self, id):
        if len(id) == MAX_ID:
            if id.isdigit():
                return True
        return False
    def check_if_phone_correct(self, phone):
        if len(phone) == MAX_PHONE:
            if phone.isdigit():
                return True
        return False
    def check_if_address_correct(self, address):
        if len(address) <= MAX_ADDRESS:
            return True
        return False      
    def check_if_employee_exists(self, id):
        all_employees = self.dlapi.get_all_employees()
        check_id = []
        for employee in all_employees:
            check_id.append(employee.id)
        if id in check_id:
            return True
        else:
            return False
# ----------------------------------------------------------------

if __name__ == "__main__":
    empLL = ContractorLL(DLAPI())
