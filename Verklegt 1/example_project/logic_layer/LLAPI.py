from logic_layer.EmployeeLL import EmployeeLL
from data_layer.DLAPI import DLAPI

class LLAPI:
    def __init__(self):
        self.dlapi = DLAPI()
        self.empLL = EmployeeLL(self.dlapi)

    def all_employees(self):
        return self.empLL.all_employees()

    def create_employee(self, emp):
        return self.empLL.create_employee(emp)