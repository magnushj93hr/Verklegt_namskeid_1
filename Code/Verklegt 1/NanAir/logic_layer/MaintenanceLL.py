from data_layer.DLAPI import DLAPI
from models.MaintananceReport import MaintananceReport


class MaintenanceLL:
    def __init__(self, dlapi):
        self.dlapi = dlapi
    
    def all_maintenance_reports(self):
        """Returns a list of all maintenance reports"""
        return self.dlapi.get_all_maintenance_reports()

    def create_maintenance_report(self, maintenance):
        """Takes in information and makes a maintenance report"""
        self.dlapi.create_maintenance_report(maintenance)
    
    def search_maintenance_report(self, report_id):
        """Takes in ID and returns report"""
        reports = []
        all_reports = self.all_maintenance_reports()
        for report in all_reports:
            if report.case_id == report_id:
                reports.append(report)
        return reports

if __name__ == "__main__":
    empLL = MaintenanceLL(DLAPI())
