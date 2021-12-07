from models.MaintenanceReport import MaintananceReport

class CreateReport:
    def __init__(self, llapi, user):
        self.user = user
        self.llapi = llapi
        self.options = """
      __|__                                                                                             __|__
*---o--(_)--o---*                                                                                 *---o--(_)--o---* 
___________________________________________________________________________________________________________________
|                                                                                                                 |
|       Home(home)         Employee(emp)         >Real estate(real)<       Cases(cases)        Contractor(con)    |
|_________________________________________________________________________________________________________________|
|                                                                                                                 |
|   Create New Report                                                                                             |
|_________________________________________________________________________________________________________________|
"""

    def draw_options(self):
        print(self.options)
        return self.create_report()

    
    def create_maintenance_report(self):
        real_estate_id = input("Enter ID: ")
        description = input("Enter description:")
        repeated = input("Is it repeated: ")
        employee_id = input("Enter employee id : ")
        case_id = input("Enter case id: ")
        total_cost = input("Enter total cost: ")
        contractor = input("Enter contractor: ")
        
    
        main = MaintananceReport(real_estate_id, description, repeated, employee_id, case_id, total_cost, contractor)
        self.display_case(main)
        save = input("Do you want to save the information (yes/no)? ")
        if save == "yes":
            self.llapi.create_maintenance_report(main)

    def display_case(self, main):
        header = """
      __|__                                                                                             __|__
*---o--(_)--o---*                                                                                 *---o--(_)--o---* 
___________________________________________________________________________________________________________________
|                                                                                                                 |
|       Home(home)         Employee(emp)         Real estate(real)         Cases(cases)        Contractor(con)    |
|_________________________________________________________________________________________________________________|
|                                                                                                                 |
|   Create New Case                                                                                               |
|_________________________________________________________________________________________________________________|"""
        
        new_main = f"""|                                                                                                                 |
|   Create new report for case: {main.case_id:82s}|                                                               
|                                                                                                                 |
|          Real estate ID: {main.real_estate_id:87s}|                                                                          
|             Description: {main.description:87s}|
|                Repeated: {main.repeated:87s}|?????
|             Employee ID: {main.employee_id:87s}|
|              Total cost: {main.total_cost:87s}|
|               Contrator: {main.Contractor:87s}|
|_________________________________________________________________________________________________________________|
"""

        print(header)
        print(new_main)