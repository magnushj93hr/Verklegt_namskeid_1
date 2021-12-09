import csv
from models.MaintananceReport import MaintananceReport


class MaintenanceDL:
    def __init__(self):
        self.filepath = "Maggi_Test/test1/csv_files/MaintenanceReport.csv"
    
    def get_all_maintenance_reports(self):
        """"Returns a list of all maintenance reports"""
        
        ret_list = []
        with open(self.filepath, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                maintenance = MaintananceReport(row["real_estate_id"], row["description"], row["employee_id"], row["case_id"], row["total_cost"], row["contractor"], row["contractor_cost"])
                ret_list.append(maintenance)
        return ret_list

    def create_maintenance_report(self, maintenance):
        """Takes in information you need to create a maintenance report and puts in maintenance report csv file  """


        with open(self.filepath, 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ["real_estate_id","description",'employee_id','case_id','cost','contractor',"contractor_cost"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'real_estate_id': maintenance.real_estate_id, "description": maintenance.description, "employee_id": maintenance.employee_id, "case_id": maintenance.case_id, "cost": maintenance.total_cost,"contractor": maintenance.contractor, "contractor_cost": maintenance.contractor_cost})
    