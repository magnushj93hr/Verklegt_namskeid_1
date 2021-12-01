import csv
from models.Employee import Employee

class EmployeeDL:
    def __init__(self):
        self.filepath = "csv_files/Employee.csv"

    def load_employee_from_file(self):
        ret_list = []
        with open(self.filepath, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                emp = Employee(row["name"], row["emp_id"], row["address"], row["homeline"], row["email"], row["phone"], row["location"], row["area"])
                ret_list.append(emp)
        return ret_list

    def store_employee_to_file(self, emp):
        with open(self.filepath, 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ["name","ID","Address","Homeline","Phone","Email","Location"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'name': emp.name, "ID": emp.emp_id, "address": emp.address, "Homeline": emp.homeline, 'Phone': emp.phone, 'Email': emp.email, 'Location': emp.location})