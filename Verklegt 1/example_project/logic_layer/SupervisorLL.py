from data_layer.DLAPI import DLAPI
from models.Employee import Employee


class SupervisorLL:
    def __init__(self, dlapi):
        self.dlapi = dlapi
    
    def create_employee(self, emp):
        self.dlapi.create_employee(emp)
    
    def create_destination(self, dest):
        self.dlapi.create_destination(dest)
    
    def create_realestate(self, real):
        self.dlapi.create_realestate(real)
    
    def create_case(self, case):
        self.dlapi.create_case(case)
    
    def edit_case(self, case):
        self.dlapi.edit_case(case)
    
    def accept_case(self, case):
        self.dlapi.accept_case(case)
    
    def open_case(self, case):
        self.dlapi.open_case(case)
    
    def edit_employee(self, emp):
        self.dlapi.edit_employee(emp)
    
    def edit_realestate(self, real):
        self.dlapi.edit_realestate(real)
    
    def create_contractor(self, contr):
        self.dlapi.create_contractor(contr)
    
    def prioritize(self, prio):
        self.dlapi.priority(prio)


if __name__ == "__main__":
    empLL = SupervisorLL(DLAPI())
