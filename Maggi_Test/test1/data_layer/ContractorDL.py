import csv

from models.Contractor import Contractor

class ContractorDL:
    def __init__(self):
        self.filepath = "Maggi_Test/test1/csv_files/Contractor.csv"
    
    def get_all_contractors(self):
        ret_list = []
        with open(self.filepath, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                contr = Contractor(row["name"], row["contact"], row["phone"], row["opening hours"], row["location"])
                ret_list.append(contr)
        return ret_list

    def create_contractor(self, contr):
        with open(self.filepath, 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ["name","contact","phone",'opening hours','location']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'name': contr.name, "contact": contr.contact, "phone": contr.phone, 'opening hours': contr.opening_hours, 'location': contr.location})