from models.Employee import Employee

class CreateEmp:
    def __init__(self, llapi, user):
        self.user = user
        self.llapi = llapi
        self.options = """
      __|__                                                                                             __|__
*---o--(_)--o---*                                                                                 *---o--(_)--o---* 
___________________________________________________________________________________________________________________
|                                                                                                                 |
|       Home(home)        >Employee(emp)<        Real estate(real)         Cases(cases)        Contractor(con)    |
|_________________________________________________________________________________________________________________|
|                                                                                                                 |
|   Create New Employee                                                                                           |
|_________________________________________________________________________________________________________________|
"""

    def draw_options(self):
        print(self.options)
        return self.create_employee()

    def create_employee(self):
        name = input("Enter employee name: ")
        emp_id = input("Enter employee ID: ")
        homeline = input("Enter employee homeline: ")
        address = input("Enter employee address: ")
        email = input("Enter employee email: ")
        phone = input("Enter employee phone: ")
        location = input("Enter employee location: ")
        area = input("Enter employee area: ")
        supervisor = input("Is Supervisor(yes/no): ")
        emp = Employee(name, emp_id, address, homeline, email, phone, location, area, supervisor)
        self.display_emp(emp)
        save = input("Do you want to save the information (yes/no)? ")
        if save == "yes":
            self.llapi.create_employee(emp)

    def display_emp(self, emp):
        header = """
      __|__                                                                                             __|__
*---o--(_)--o---*                                                                                 *---o--(_)--o---* 
___________________________________________________________________________________________________________________
|                                                                                                                 |
|       Home(home)        >Employee(emp)<        Real estate(real)         Cases(cases)        Contractor(con)    |
|_________________________________________________________________________________________________________________|
|                                                                                                                 |
|   Create New Employee                                                                                           |
|_________________________________________________________________________________________________________________|"""
        
        new_emp = f"""|                                                                                                                 |
|   Create New Employee                                                                                           |
|                                                                                                                 |
|                    Name: {emp.name:87s}|
|                      ID: {emp.emp_id:87s}|
|            Home address: {emp.address:87s}|
|        Home phonenumber: {emp.homeline:87s}|
|                     GSM: {emp.phone:87s}|
|                   Email: {emp.email:87s}|
|                Location: {emp.location:87s}|
|                    Area: {emp.area:87s}|
|   Is Supervisor(yes/no): {emp.supervisor:87s}|
|_________________________________________________________________________________________________________________|
"""

        print(header)
        print(new_emp)