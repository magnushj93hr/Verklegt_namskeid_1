from data_layer.DLAPI import DLAPI
from models.Employee import Employee
import csv 

MAX_NAME = 40
MAX_ID = 4
EMAIL = "@nanair.com"
PHONE = 7
MAX_ADDRESS = 20
MAX_LOCATION = 15


class EmployeeLL:
    def __init__(self, dlapi):
        self.dlapi = dlapi
        self.emp = Employee()

    def check_if_name_correct(self, name):
        if len(self.emp.name) <= MAX_NAME:
            if not self.emp.name.isdigit():
                return True
        return False

    def check_if_id_correct(self, id):
        if len(id) == MAX_ID:
            if id.isdigit():
                return True
        return False

    def make_email(self):
        em = self.emp.name.split()[0]
        email = em + self.emp.id + EMAIL
        return email

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

    def all_employees(self):
        return self.dlapi.get_all_employees()

    def create_employee(self, emp):
        self.dlapi.create_employee(emp)
    
    def check_if_employee_exists(self, id):
        return self.dlapi.check_if_employee_exists(id)
    
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
