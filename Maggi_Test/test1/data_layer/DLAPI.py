from data_layer.EmployeeDL import EmployeeDL
from data_layer.RealEstateDL import RealEstateDL
from data_layer.CaseDL import CaseDL
from data_layer.ContractorDL import ContractorDL

class DLAPI:
    def __init__(self):
        self.empDL = EmployeeDL()
        self.realDL = RealEstateDL()
        self.caseDL = CaseDL()
        self.contrDL = ContractorDL()

    def get_all_employees(self):
        return self.empDL.get_all_employees()
    
    def create_employee(self, emp):
        return self.empDL.create_employee(emp)
    
    def get_all_realestate(self):
        return self.realDL.get_all_realestate()
    
    def create_realestate(self, real):
        return self.realDL.create_realestate(real)
    
    def get_all_cases(self):
        return self.caseDL.get_all_cases()
    
    def create_case(self, case):
        return self.caseDL.create_case(case)
    
    def get_all_contractors(self):
        return self.contrDL.get_all_contractors()
    
    def create_contractor(self, contr):
        return self.contrDL.create_contractor(contr)