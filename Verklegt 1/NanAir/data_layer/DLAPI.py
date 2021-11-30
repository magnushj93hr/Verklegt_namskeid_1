from data_layer.EmployeeDL import EmployeeDL

class DLAPI:
    def __init__(self):
        self.empDL = EmployeeDL()

    def get_all_employees(self):
        return self.empDL.get_all_employees()
    
    def create_employee(self, emp):
        return self.empDL.create_employee(emp)