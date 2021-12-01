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
|   - se             //Save and exit                           - x        //Exit without saving                   |
|_________________________________________________________________________________________________________________|
|                                                                                                                 |
|   Create New Employee                                                                                           |
|                                                                                                                 |
|                    Name:                                                                                        |
|                      ID:                                                                                        |
|            Home address:                                                                                        |
|        Home phonenumber:                                                                                        |
|                     GSM:                                                                                        |
|                   Email:                                                                                        |
|                 Country:                                                                                        |
|                Location:                                                                                        |
|   Is Supervisor(yes/no):                                                                                        |
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

        emp = Employee(name, emp_id, address, homeline, email, phone, location)
        self.llapi.create_employee(emp)

    def display_emp(self, emp):
        pass