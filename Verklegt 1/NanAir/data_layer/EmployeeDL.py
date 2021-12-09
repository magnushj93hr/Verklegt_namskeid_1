import csv
import shutil
from tempfile import NamedTemporaryFile

from models.Employee import Employee

class EmployeeDL:
    def __init__(self):
        self.filepath = "Verklegt 1/NanAir/csv_files/Employee.csv"

    def get_all_employees(self):
        """"Returns a list of all employees"""

        ret_list = []
        with open(self.filepath, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                emp = Employee(row["name"], row["id"], row["address"], row["homeline"], row["location"], row["phone"], row["supervisor"])
                ret_list.append(emp)
        return ret_list

    def create_employee(self, emp):
        """Takes in information you need to create a employee and puts in employee csv file  """

        with open(self.filepath, 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ["name","id","address",'homeline','email','location','phone',"supervisor"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'name': emp.name, "id": emp.id, "address": emp.address, 'homeline': emp.homeline, 'email': emp.email, 'location': emp.location, 'phone': emp.phone, "supervisor": emp.supervisor})

    def edit_employee(self, emp):
        """Takes in employee information from employee csv file, and updates it """

        temp_file = NamedTemporaryFile(mode = 'w', newline='', encoding='utf-8', delete=False)
        
        fieldnames = ["name","id","address",'homeline','email','location','phone', "supervisor"]
        with open(self.filepath, 'r', newline='', encoding='utf-8') as csvfile, temp_file:
            reader = csv.DictReader(csvfile, fieldnames=fieldnames)
            #fieldnames = ["name","id","address",'homeline','email','location','phone']
            writer = csv.DictWriter(temp_file, fieldnames=fieldnames)
            # writer.writeheader()
            for row in reader:
                if row['id'] == emp.id:
                    print('updating row', row['id'])
                    writer.writerow({'name': emp.name, "id": emp.id, "address": emp.address, 'homeline': emp.homeline, 'email': emp.email, 'location': emp.location, 'phone': emp.phone, "supervisor": emp.supervisor})
                else:
                    row = {'name': row['name'], 'id': row['id'], 'address': row['address'], 'homeline': row['homeline'], 'email': row['email'], 'location': row['location'], 'phone': row['phone'], "supervisor": row["supervisor"]}
                    writer.writerow(row)
        shutil.move(temp_file.name, self.filepath)