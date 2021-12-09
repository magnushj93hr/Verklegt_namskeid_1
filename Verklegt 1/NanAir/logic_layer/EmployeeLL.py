from data_layer.DLAPI import DLAPI
from models.Employee import Employee
import csv 


class EmployeeLL:
    def __init__(self, dlapi):
        self.dlapi = dlapi

    def all_employees(self):
        """Returns list of all employees"""
        return self.dlapi.get_all_employees()

    def search_employee(self, emp_id):
        """Takes in id and searches for employee"""
        all_employees = self.dlapi.get_all_employees()
        for employee in all_employees:
            if employee.id == emp_id:
                return employee
    
    def filter_employee(self, filter):
        """Returns employees by location"""
        filtered_employees = []
        all_employees = self.dlapi.get_all_employees()
        for employee in all_employees:
            if employee.location == filter:
                filtered_employees.append(employee)
        return filtered_employees

    def create_employee(self, emp):
        """Takes in information and creates an employee"""

        self.dlapi.create_employee(emp)
    
    def edit_employee(self, edit_id):
        """Takes in ID and edits employee """

        self.dlapi.edit_employee(edit_id)


# ----------------------------------------------------------------
#check if employee exists
    def check_if_employee_exists(self, id):
        """Takes in ID and checks if employee exists """

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
    empLL = EmployeeLL(DLAPI())
