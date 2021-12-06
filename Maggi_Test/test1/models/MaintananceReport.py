class MaintananceReport:
    def __init__(self, real_estate_id, description, repeated, employee_id, case_id, total_cost, contractor, case):
        self.real_estate_id = real_estate_id
        self.description = description
        self.repeated = repeated
        self.case_id = case_id
        self.total_cost = total_cost
        self.contractor = contractor
        self.employee_id = employee_id

        self.case = case

    def __str__(self):
        return f"real estate id: {self.real_estate_id}, description: {self.description}, repeated: {self.repeated}, case id: {self.case_id}, total cost: {self.total_cost}, contractor: {self.contractor}"