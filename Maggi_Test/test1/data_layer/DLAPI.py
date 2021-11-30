from data_layer.EmployeeDL import EmployeeDL
from data_layer.RealEstateDL import RealEstateDL
from data_layer.CaseDL import CaseDL

class DLAPI:
    def __init__(self):
        self.empDL = EmployeeDL()
        self.realDL = RealEstateDL()
        self.caseDL = CaseDL()

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