from models.Employee import Employee

AUTO_ID = 'NaN-'

class CreateEmp:
    def __init__(self, llapi):
        self.llapi = llapi
        self.options = """
      __|__                                                                                             __|__
*---o--(_)--o---*                                                                                 *---o--(_)--o---* 
___________________________________________________________________________________________________________________
|                                                                                                                 |
|       Home         Employee           Real estate         Cases          >Contractor<          Location         |
|_________________________________________________________________________________________________________________|
|                                                                                                                 |
|   Create New Employee                                                                                           |
|_________________________________________________________________________________________________________________|
"""


    def create_employee(self):
        """Creates employee"""
        print(self.options)
        print("Welcome to the creation kit!")
        name, phone, id, address, homeline, location, supervisor = self.user_options()
        emp = Employee(name, id, address, homeline, location, phone, supervisor)
        save = self.display_emp(emp)
        if save:
            self.llapi.create_employee(emp)

    def user_options(self):
        """Returns employee information"""
        location = self.available_locations()
        id = self.get_emp_id()
        name = self.input_and_check("name", lambda value : self.llapi.is_name_correct(value))
        phone = self.input_and_check("phone", lambda value : self.llapi.is_phone_correct(value))
        homeline = self.input_and_check("homeline", lambda value : self.llapi.is_phone_correct(value))
        address = self.input_and_check("address", lambda value : self.llapi.is_address_correct(value))
        supervisor = self.is_supervisor()
        return name, phone, id, address, homeline, location, supervisor


# input parameters and checks
    def input_and_check(self, info_type, check_fun):
        """Takes in input from user and checks if input is valid, returns the input if it's valid"""
        while True:
            value = input(f"Enter employee {info_type}: ")
            if not check_fun(value):
                print(f"Invalid employee {info_type}")
            else:
                return value

    def available_locations(self):
        """Displays available locations and returns the location the user chooses"""
        while True:
            print('Available locations to choose from: \n')
            for location in self.llapi.get_locations_name():
                print(location)
            print()
            location = str(input("Enter location: ")).lower().capitalize()
            if location not in self.llapi.get_locations_name():
                print("Invalid location")
            else:
                return location

    def get_emp_id(self):
        """Returns employee id"""
        all_id = self.llapi.all_employees()
        id = AUTO_ID + str(len(all_id) + 1)
        return id
    
    def is_supervisor(self):
        """Making employee an supervisor or not, returns yes or no"""
        while True:
            opt = input("Make employee supervisor(yes/no): ")
            if opt != "yes" and opt != "no":
                print("Invalid option")
            else:
                return opt

# ------------------------------------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------------------------------------


    def display_emp(self, emp):
        """Prints new employee info"""
        header = """
      __|__                                                                                             __|__
*---o--(_)--o---*                                                                                 *---o--(_)--o---* 
___________________________________________________________________________________________________________________
|                                                                                                                 |
|       Home        Employee          Real estate         >Cases<           Contractor           Location         |
|_________________________________________________________________________________________________________________|
|                                                                                                                 |
|   Create New Employee                                                                                           |
|_________________________________________________________________________________________________________________|"""
        
        new_emp = f"""|                                                                                                                 |
|      Employee                                                                                                   |
|                                                                                                                 |
|                    Name: {emp.name:87s}|
|                      ID: {emp.id:87s}|
|            Home address: {emp.address:87s}|
|        Home phonenumber: {emp.homeline:87s}|
|                     GSM: {emp.phone:87s}|
|                   Email: {emp.email:87s}|
|                Location: {emp.location:87s}|
|              Supervisor: {emp.supervisor:87s}|
|_________________________________________________________________________________________________________________|
"""
        self.llapi.clear()
        print(header)
        print(new_emp)
        while True:
            save = input("Do you want to save employee(y/n): ")
            if save == "y":
                return True
            elif save == "n":
                return False
            else:
                print("Invalid option")