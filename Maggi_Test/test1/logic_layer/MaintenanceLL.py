from data_layer.DLAPI import DLAPI
from models.MaintananceReport import MaintananceReport


class MaintenanceLL:
    def __init__(self, dlapi):
        self.dlapi = dlapi
    
    def all_maintenance_reports(self):
        return self.dlapi.get_all_maintenance_reports()

    def create_maintenance_report(self, maintenance):
        self.dlapi.create_maintenance_report(maintenance)
    
    def search_maintenance_report(self, report_id):
        all_reports = self.all_maintenance_reports()
        for report in all_reports:
            if report.case_id == report_id:
                return report

if __name__ == "__main__":
    empLL = MaintenanceLL(DLAPI())
