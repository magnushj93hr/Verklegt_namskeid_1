import csv
from models.MaintananceReport import MaintananceReport


class MaintenanceDL:
    def __init__(self):
        self.filepath = "Maggi_Test/test1/csv_files/MaintenanceReport.csv"
    
    def get_all_maintenance_reports(self):
        ret_list = []
        with open(self.filepath, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                maintenance = MaintananceReport(row["real estate id"], row["description"], row["repeated"], row["employee id"], row["case id"], row["total cost"], row["contractor"])
                ret_list.append(maintenance)
        return ret_list

    def create_maintenance_report(self, maintenance):
        with open(self.filepath, 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ["real estate id","description","repeated",'employee id','case id','cost','contractor']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'real estate id': maintenance.real_estate_id, "description": maintenance.description, "repeated": maintenance.repeated, "employee id": maintenance.employee_id, "case id": maintenance.case_id, "cost": maintenance.total_cost,"contractor": maintenance.contractor})
    