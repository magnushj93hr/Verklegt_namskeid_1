from logic_layer.EmployeeLL import EmployeeLL

from logic_layer.RealEstateLL import RealEstateLL

from logic_layer.CaseLL import CaseLL

from logic_layer.ContractorLL import ContractorLL

from logic_layer.LocationLL import LocationLL

from logic_layer.MaintenanceLL import MaintenanceLL

from data_layer.DLAPI import DLAPI



class LLAPI:

    SEARCH_TYPE_NAME = "name"

    SEARCH_TYPE_ID = "emp_id"

    SEARCH_TYPE_ADDRESS = "address"

    SEARCH_TYPE_PHONE = "phonenumber"

    SEARCH_TYPE_GSM = "gsm"

    SEARCH_TYPE_EMAIL = "email"


    def __init__(self):

        self.dlapi = DLAPI()

        self.empLL = EmployeeLL(self.dlapi)

        self.realLL = RealEstateLL(self.dlapi)

        self.caseLL = CaseLL(self.dlapi)

        self.contrLL = ContractorLL(self.dlapi)

        self.locLL = LocationLL(self.dlapi)

        self.maintenanceLL = MaintenanceLL(self.dlapi)

    


# ----------------------------------------------------------------

    # This function checks if the employee is valid
    def is_name_correct(self, name):
        return self.empLL.check_if_name_correct(name)
    def is_id_correct(self, id):

        return self.empLL.check_if_id_correct(id)
    def make_email(self):
        return self.empLL.make_email()

    def is_phone_correct(self, phone):

        return self.empLL.check_if_phone_correct(phone)
    def is_address_correct(self, address):

        return self.empLL.check_if_address_correct(address)

    def is_location_correct(self, location):
        return self.empLL.check_if_location_correct(location)

# ----------------------------------------------------------------





# ----------------------------------------------------------------

# EMPOYEE FUNCTIONS

    def all_employees(self):

        return self.empLL.all_employees()


    def create_employee(self, emp):

        return self.empLL.create_employee(emp)


    def check_if_employee_exists(self, id):

        return self.empLL.check_if_employee_exists(id) 


    def edit_employee(self, emp):

        return self.empLL.edit_employee(emp)
    

    def search_employee(self, emp_id):

        return self.empLL.search_employee(emp_id)
    

    def filter_employee(self, filter):

        return self.empLL.filter_employee(filter)

# ----------------------------------------------------------------

# REAL ESTATE FUNCTIONS

    def all_realestate(self):

        return self.realLL.all_realestate()


    def create_realestate(self, real):

        return self.realLL.create_realestate(real)


    def edit_realestate(self, real):

        return self.realLL.edit_realestate(real)
    

    def search_realestate(self, real_id):

        return self.realLL.search_realestate(real_id)
    

    def filter_realestate(self, filter):

        return self.realLL.filter_realestate(filter)

# ----------------------------------------------------------------

# CASE FUNCTIONS

    def create_case(self, case):

        return self.caseLL.create_case(case)


    def all_cases(self):

        return self.caseLL.all_cases()


    def edit_case(self, case):

        return self.caseLL.edit_case(case)
    

    def search_case(self, case_id):

        return self.caseLL.search_employee(case_id)

# ----------------------------------------------------------------

# CONTRACTOR FUNCTIONS

    def all_contractors(self):

        return self.contrLL.all_contractors()


    def create_contractor(self, contr):

        return self.contrLL.create_contractor(contr)

# ----------------------------------------------------------------

# LOCATION FUNCTIONS

    def all_locations(self):

        return self.locLL.all_locations()


    def create_location(self,loc):

        return self.locLL.create_location(loc)

# ----------------------------------------------------------------

# MAINTENANCE REPORT FUNCTIONS

    def create_maintenance_report(self,maintenance):

        return self.maintenanceLL.create_maintenance_report(maintenance)


    def all_maintenance_reports(self):

        return self.maintenanceLL.all_maintenance_reports()

# ----------------------------------------------------------------