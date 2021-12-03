import csv
import shutil
from tempfile import NamedTemporaryFile

from models.Employee import Employee

class EmployeeDL:
    def __init__(self):
        self.filepath = "Maggi_Test/test1/csv_files/Employee.csv"

    def get_all_employees(self):
        ret_list = []
        with open(self.filepath, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                emp = Employee(row["name"], row["id"], row["address"], row["homeline"], row["location"], row["phone"])
                ret_list.append(emp)
                # print(emp)
        return ret_list

    def create_employee(self, emp):
        with open(self.filepath, 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ["name","id","address",'homeline','email','location','phone']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'name': emp.name, "id": emp.id, "address": emp.address, 'homeline': emp.homeline, 'email': emp.email, 'location': emp.location, 'phone': emp.phone})

    def check_if_employee_exists(self, id):
        ret_list = []
        with open(self.filepath, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['id'] == id:
                    return True
                else:
                    return False

    def edit_employee(self, emp):
        temp_file = NamedTemporaryFile(mode = 'w', delete=False)
        
        fieldnames = ["name","id","address",'homeline','email','location','phone']
        with open(self.filepath, 'r', newline='', encoding='utf-8') as csvfile, temp_file:
            reader = csv.DictReader(csvfile, fieldnames=fieldnames)
            #fieldnames = ["name","id","address",'homeline','email','location','phone']
            writer = csv.DictWriter(temp_file, fieldnames=fieldnames)
            # writer.writeheader()
            for row in reader:
                if row['id'] == emp.id:
                    print('updating row', row['id'])
                    writer.writerow({'name': emp.name, "id": emp.id, "address": emp.address, 'homeline': emp.homeline, 'email': emp.email, 'location': emp.location, 'phone': emp.phone})
                else:
                    row = {'name': row['name'], 'id': row['id'], 'address': row['address'], 'homeline': row['homeline'], 'email': row['email'], 'location': row['location'], 'phone': row['phone']}
                    writer.writerow(row)
        shutil.move(temp_file.name, self.filepath)

    def search(self, search_type, value):
        fieldnames = ["name","id","address",'homeline','email','location','phone']
        with open(self.filepath, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile, fieldnames=fieldnames)
            for row in reader:
                emp = Employee(row["name"], row["id"], row["address"], row["homeline"], row["email"], row["location"], row["phone"])
                if self.matches(emp, search_type, value):
                    return emp

    
    def matches(self, emp, search_type, value):
        if search_type == "name" and value == emp.name:
            return True
