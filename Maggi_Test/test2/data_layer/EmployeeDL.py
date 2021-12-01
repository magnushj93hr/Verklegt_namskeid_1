import csv

from models.Employee import Employee

class EmployeeDL:
    def __init__(self):
        self.filepath = "csv_files/Employee.csv"
    
    def get_all_employees(self):
        ret_list = []
        with open(self.filepath, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                emp = Employee(row["name"], row["email"], row["phone"])
                ret_list.append(emp)
        return ret_list

    def create_employee(self, emp):
        with open(self.filepath, 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ["name","email","phone"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'name': emp.name, "email": emp.email, "phone": emp.phone})
       