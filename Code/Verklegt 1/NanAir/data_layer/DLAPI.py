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


# ----------------------------------------------------------------
# EMPLOYEE FUNCTIONS
    def get_all_employees(self):
        return self.empDL.get_all_employees()

    def create_employee(self, emp):
        return self.empDL.create_employee(emp)

    def check_if_employee_exists(self, id):
        return self.empDL.check_if_employee_exists(id)

    def edit_employee(self, emp):
        return self.empDL.edit_employee(emp)
# ----------------------------------------------------------------
# REAL ESTATE FUNCTIONS
    def get_all_realestate(self):
        return self.realDL.get_all_realestate()

    def create_realestate(self, real):
        return self.realDL.create_realestate(real)

    def edit_realestate(self, real):
        return self.realDL.edit_realestate(real)
# ----------------------------------------------------------------
# CASE FUNCTIONS
    def get_all_cases(self):
        return self.caseDL.get_all_cases()

    def create_case(self, case):
        return self.caseDL.create_case(case)

    def check_if_case_exists(self, id):
        return self.caseDL.check_if_case_exists(id)

    def edit_case(self, case):
        return self.caseDL.edit_case(case)
# ----------------------------------------------------------------
# CONTRACTOR FUNCTIONS
    def get_all_contractors(self):
        return self.contrDL.get_all_contractors()

    def create_contractor(self, contr):
        return self.contrDL.create_contractor(contr)
    
    def edit_contractor(self, name):
        return self.contrDL.edit_contractor(name)
# ----------------------------------------------------------------
# LOCATION FUNCTIONS
    def get_all_locations(self):
        return self.locDL.get_all_locations()

    def create_location(self, loc):
        return self.locDL.create_location(loc)
# ----------------------------------------------------------------
# MAINTENANCE REPORT FUNCTIONS
    def get_all_maintenance_reports(self):
        return self.maintanancereportDL.get_all_maintenance_reports()

    def create_maintenance_report(self, maintenancereport):
        return self.maintanancereportDL.create_maintenance_report(maintenancereport)