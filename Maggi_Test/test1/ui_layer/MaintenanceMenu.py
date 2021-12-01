from logic_layer.LLAPI import LLAPI
from models.MaintananceReport import MaintananceReport

class MaintenanceMenu:
    def __init__(self, llapi):
        self.llapi = llapi
        self.options = """
contractor menu
1 - list all locations
2 - create new maintenance report
r - return to previous menu
"""

    def draw_options(self):
        print(self.options)
        return self.prompt_input()

    def prompt_input(self):
        while True:
            command = input("Enter your input: ")
            if command == "1":
                all_maintenance_reports = self.llapi.all_maintenance_reports()
                for maintenance in all_maintenance_reports:
                    print(maintenance)
            elif command == "2":
                self.create_maintenance_report()
            elif command == "r":
                return "r"
            else:
                print("invalid option, try again!")
            print(self.options)

    def create_maintenance_report(self):
        real_estate_id = input("Enter ID: ")
        description = input("Enter description:")
        repeated = input("Is it repeated: ")
        employee_id = input("Enter employee id : ")
        case_id = input("Enter case id: ")
        total_cost = input("Enter total cost: ")
        contractor = input("Enter contractor: ")
        
        
        maintenance = MaintananceReport(real_estate_id, description, repeated, employee_id, case_id, total_cost, contractor)
        self.llapi.create_maintenance_report(maintenance)
