from data_layer.DLAPI import DLAPI
from models.Employee import Employee


class EmployeeLL:
    def __init__(self, dlapi):
        self.dlapi = dlapi
    
    def all_employees(self):
        return self.dlapi.get_all_employees()

    def create_employee(self, emp):
        self.dlapi.create_employee(emp)
    
    def edit_employee(self, edit_id):
        self.dlapi.edit_employee(edit_id)

    def search(self, search_type, value):
        return self.dlapi.emp_search(search_type, value)

if __name__ == "__main__":
    empLL = EmployeeLL(DLAPI())
