from data_layer.EmployeeDL import EmployeeDL
from data_layer.RealEstateDL import RealEstateDL
from data_layer.CaseDL import CaseDL
from data_layer.ContractorDL import ContractorDL
from data_layer.LocationDL import LocationDL
from data_layer.MaintananceReportDL import MaintenanceDL

class DLAPI:
    def __init__(self):
        self.empDL = EmployeeDL()
        self.realDL = RealEstateDL()
        self.caseDL = CaseDL()
        self.contrDL = ContractorDL()
        self.locDL = LocationDL()
        self.maintanancereportDL = MaintenanceDL()

    def get_all_employees(self):
        return self.empDL.get_all_employees()
    
    def create_employee(self, emp):
        return self.empDL.create_employee(emp)
    
    def edit_employee(self, emp):
        return self.empDL.edit_employee(emp)

    def emp_search(self, search_type, value):
        return self.empDL.search(search_type, value)
    
    def get_all_realestate(self):
        return self.realDL.get_all_realestate()
    
    def create_realestate(self, real):
        return self.realDL.create_realestate(real)
    
    def edit_realestate(self, real):
        return self.realDL.edit_realestate(real)
    
    def get_all_cases(self):
        return self.caseDL.get_all_cases()
    
    def create_case(self, case):
        return self.caseDL.create_case(case)
    
    def edit_case(self, case):
        return self.caseDL.edit_case(case)
    
    def get_all_contractors(self):
        return self.contrDL.get_all_contractors()
    
    def create_contractor(self, contr):
        return self.contrDL.create_contractor(contr)

    def get_all_locations(self):
        return self.locDL.get_all_locations()
    
    def create_location(self, loc):
        return self.locDL.create_location(loc)

    def get_all_maintenance_reports(self):
        return self.maintanancereportDL.get_all_maintenance_reports()
    
    def create_maintenance_report(self, maintenancereport):
        return self.maintanancereportDL.create_maintenance_report(maintenancereport)