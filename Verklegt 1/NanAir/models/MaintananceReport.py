class MaintananceReport:
    def __init__(self, real_estate_id, description, employee_id, case_id, material_cost, contractor, contractor_cost, total_cost,):
        self.real_estate_id = real_estate_id
        self.description = description
        self.case_id = case_id
        self.meterial_cost = material_cost
        self.contractor = contractor
        self.employee_id = employee_id
        self.contractor_cost = contractor_cost
        self.total_cost = total_cost

    def __str__(self):
        return f"real estate id: {self.real_estate_id}, description: {self.description}, case id: {self.case_id}, material cost: {self.meterial_cost}, contractor: {self.contractor}, contractor cost: {self.contractor_cost}, total cost: {self.total_cost}"