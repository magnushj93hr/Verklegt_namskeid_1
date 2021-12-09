import csv

from models.Contractor import Contractor
import shutil
from tempfile import NamedTemporaryFile

class ContractorDL:
    def __init__(self):
        self.filepath = "Maggi_Test/test1/csv_files/Contractor.csv"
    
    def get_all_contractors(self):
        ret_list = []
        with open(self.filepath, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                contr = Contractor(row["name"], row["contact"], row["phone"], row["opening hours"], row["location"], row["review"])
                ret_list.append(contr)
        return ret_list

    def create_contractor(self, contr):
        with open(self.filepath, 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ["name","contact","phone",'opening hours','location',"review"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'name': contr.name, "contact": contr.contact, "phone": contr.phone, 'opening hours': contr.opening_hours, 'location': contr.location, "review": contr.review})
    
    def edit_contractor(self, contr):
        temp_file = NamedTemporaryFile(mode = 'w', newline='', encoding='utf-8', delete=False)
        
        fieldnames = ["name","contact","phone",'opening hours','location','review']
        with open(self.filepath, 'r', newline='', encoding='utf-8') as csvfile, temp_file:
            reader = csv.DictReader(csvfile, fieldnames=fieldnames)
            writer = csv.DictWriter(temp_file, fieldnames=fieldnames)
            # writer.writeheader()
            for row in reader:
                if row['name'] == contr.name:
                    print('updating row', row['name'])
                    writer.writerow({'name': contr.name, "contact": contr.contact, "phone": contr.phone, "opening hours": contr.opening_hours, 'location': contr.location, "review": contr.review})
                else:
                    row = {"name": row["name"], "contact": row["contact"], "phone": row["phone"], "opening hours": row["opening hours"], "location": row["location"], "review": row["review"]}
                    writer.writerow(row)
        shutil.move(temp_file.name, self.filepath)