from data_layer.DLAPI import DLAPI
from models.Employee import Employee
import csv 

MAX_NAME = 40
MAX_ID = 4
EMAIL = "@nanair.com"
MAX_PHONE = 7
MAX_ADDRESS = 20
MAX_LOCATION = 15


class EmployeeLL:
    def __init__(self, dlapi):
        self.dlapi = dlapi

    def all_employees(self):
        return self.dlapi.get_all_employees()

    def search_employee(self, emp_id):
        all_employees = self.dlapi.get_all_employees()
        for employee in all_employees:
            if employee.id == emp_id:
                return employee
    
    def filter_employee(self, filter):
        filtered_employees = []
        all_employees = self.dlapi.get_all_employees()
        for employee in all_employees:
            if employee.location == filter:
                filtered_employees.append(employee)
        return filtered_employees
        
    def create_employee(self, emp):
        self.dlapi.create_employee(emp)
    
    def check_if_employee_exists(self, id):
        return self.dlapi.check_if_employee_exists(id)
    
    def edit_employee(self, edit_id):
        self.dlapi.edit_employee(edit_id)


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
    def check_if_location_correct(self, location):
        if len(location) <= MAX_LOCATION:
            return True
        return False
# ----------------------------------------------------------------


if __name__ == "__main__":
    empLL = EmployeeLL(DLAPI())
