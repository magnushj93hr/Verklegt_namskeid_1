from logic_layer.EmployeeLL import EmployeeLL
from logic_layer.RealEstateLL import RealEstateLL
from logic_layer.CaseLL import CaseLL
from logic_layer.ContractorLL import ContractorLL
from logic_layer.LocationLL import LocationLL
from data_layer.DLAPI import DLAPI


class LLAPI:
    def __init__(self):
        self.dlapi = DLAPI()
        self.empLL = EmployeeLL(self.dlapi)
        self.realLL = RealEstateLL(self.dlapi)
        self.caseLL = CaseLL(self.dlapi)
        self.contrLL = ContractorLL(self.dlapi)
        self.locLL = LocationLL(self.dlapi)
        
    def all_employees(self):
        return self.empLL.all_employees()

    def create_employee(self, emp):
        return self.empLL.create_employee(emp)
    
    def all_realestate(self):
        return self.realLL.all_realestate()
    
    def create_realestate(self, real):
        return self.realLL.create_realestate(real)
    
    def create_case(self, case):
        return self.caseLL.create_case(case)
    
    def all_cases(self):
        return self.caseLL.all_cases()
    
    def all_contractors(self):
        return self.contrLL.all_contractors()
    
    def create_contractor(self, contr):
        return self.contrLL.create_contractor(contr)

    def all_location(self):
        return self.locLL.all_location()
    
    def create_location(self,loc):
        return self.locLL.create_location(loc)