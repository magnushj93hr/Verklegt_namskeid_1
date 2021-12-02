from data_layer.DLAPI import DLAPI
from models.Employee import Employee
import csv 


class EmployeeLL:
    def __init__(self, dlapi):
        self.dlapi = dlapi
    
    def all_employees(self):
        return self.dlapi.get_all_employees()

    def create_employee(self, emp):
        self.dlapi.create_employee(emp)
    
    def edit_employee(self, edit_id):
        self.dlapi.edit_employee(edit_id)

    # def search(self, search_type, value):
    #     fieldnames = ["name","id","address",'homeline','email','location','phone']
    #     with open(self.filepath, newline='', encoding='utf-8') as csvfile:
    #         reader = csv.DictReader(csvfile, fieldnames=fieldnames)
    #         for row in reader:
    #             emp = Employee(row["name"], row["id"], row["address"], row["homeline"], row["email"], row["location"], row["phone"])
    #             if self.matches(emp, search_type, value):
    #                 return emp

    # def matches(self, emp, search_type, value):
    #     if search_type == "name" and value == emp.name:
    #         return True

    def search(self, search_type, value):
        return self.dlapi.emp_search(search_type, value)

if __name__ == "__main__":
    empLL = EmployeeLL(DLAPI())
