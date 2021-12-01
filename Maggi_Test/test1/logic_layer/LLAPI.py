from logic_layer.EmployeeLL import EmployeeLL
from logic_layer.RealEstateLL import RealEstateLL
from logic_layer.CaseLL import CaseLL
from logic_layer.ContractorLL import ContractorLL
from logic_layer.LocationLL import LocationLL
from logic_layer.MaintenanceLL import MaintenanceLL
from data_layer.DLAPI import DLAPI


class LLAPI:
    def __init__(self):
        self.dlapi = DLAPI()
        self.empLL = EmployeeLL(self.dlapi)
        self.realLL = RealEstateLL(self.dlapi)
        self.caseLL = CaseLL(self.dlapi)
        self.contrLL = ContractorLL(self.dlapi)
        self.locLL = LocationLL(self.dlapi)
        self.maintenanceLL = MaintenanceLL(self.dlapi)
        
    def all_employees(self):
        return self.empLL.all_employees()

    def create_employee(self, emp):
        return self.empLL.create_employee(emp)
    
    def edit_employee(self, emp):
        return self.empLL.edit_employee(emp)
    
    def all_realestate(self):
        return self.realLL.all_realestate()
    
    def create_realestate(self, real):
        return self.realLL.create_realestate(real)
    def edit_realestate(self, real):
        return self.empLL.edit_employee(real)
    
    def create_case(self, case):
        return self.caseLL.create_case(case)
    
    def all_cases(self):
        return self.caseLL.all_cases()
    
    def all_contractors(self):
        return self.contrLL.all_contractors()
    
    def create_contractor(self, contr):
        return self.contrLL.create_contractor(contr)

    def all_locations(self):
        return self.locLL.all_locations()
    
    def create_location(self,loc):
        return self.locLL.create_location(loc)
    def create_maintenance_report(self,maintenance):
        return self.maintenanceLL.create_maintenance_report(maintenance)
    def all_maintenance_reports(self):
        return self.maintenanceLL.all_maintenance_reports