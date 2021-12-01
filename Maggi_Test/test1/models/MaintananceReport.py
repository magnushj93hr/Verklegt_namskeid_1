class MaintananceReport:
    def __init__(self, real_estate_id, description, repeated, employee_id, case_id, total_cost, contractor):
        self.real_estate_id = real_estate_id
        self.description = description
        self.repeated = repeated
        self.case_id = case_id
        self.total_cost = total_cost
        self.contractor = contractor
        

    def __str__(self):
        return f"country: {self.country}, aiport: {self.airport}, phone: {self.phone}, opening hours: {self.opening_hours}"