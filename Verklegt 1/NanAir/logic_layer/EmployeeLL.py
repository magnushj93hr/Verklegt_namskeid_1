from data_layer.DLAPI import DLAPI
from models.Employee import Employee


class EmployeeLL:
    def __init__(self, dlapi):
        self.dlapi = dlapi
    
    def all_employees(self):
        return self.dlapi.get_all_employees()
    
    def mark_complete(self, mark):
        self.dlapi.mark_complete(mark)
    
    def create_maintenance_report(self, main):
        self.dlapi.create_maintenance_report(main)
    
    def search(self, search):
        self.dlapi.search(search)
    
    def make_sign(self, sign):
        self.dlapi.make_sign(sign)



if __name__ == "__main__":
    empLL = EmployeeLL(DLAPI())

