from models.MaintananceReport import MaintananceReport

class CreateReport:
    def __init__(self, llapi, user):
        self.llapi = llapi
        self.user = user


    def create_maintenance_report(self, case):
        real_estate_id = case.real_est_id
        tasks_done = input("Enter what you did: ")
        employee_id = self.user.user_id
        case_id = case.id
        cost_of_materials = int(input("Enter cost of materials: "))
        used_contractor = input('Did you use a contractor(y/n)?: ')
        if used_contractor == "y":
            contractor = self.available_contractors()
            contractor_cost = int(input("Enter contractor cost: "))
            total_cost = cost_of_materials + contractor_cost
        else:
            contractor = ""
            contractor_cost = 0
            total_cost = cost_of_materials
        
        maintenance = MaintananceReport(real_estate_id, tasks_done, employee_id, case_id, cost_of_materials, contractor, contractor_cost, total_cost)

        case = self.llapi.get_case(case_id)
        case.status = "Ready to close"
        self.llapi.create_maintenance_report(maintenance)
        self.llapi.edit_case(case)


    def available_contractors(self):
        while True:
            print('Available contractors to choose from: \n')
            for contractor in self.llapi.get_contractors_name():
                print(contractor)
            print()
            contractor = str(input("Enter contractor: ")).lower().capitalize()
            if contractor not in self.llapi.get_contractors_name():
                print("Contractor not found")
            else:
                return contractor