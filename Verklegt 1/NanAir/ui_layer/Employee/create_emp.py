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
        print("Welcome to the creation kit!")
        print("Quit by entering (q): ")
        name, phone, id, address, homeline, location, supervisor = self.user_options()
        # if name != None and phone != None and id != None and address != None and homeline != None and location != None and supervisor != None:
        emp = Employee(name, id, address, homeline, location, phone, supervisor)
        self.llapi.create_employee(emp)

    def user_options(self):
        location = self.available_locations()
        check = self.llapi.check_location_append_to_list(location)
        id = self.make_emp_or_sup_id(check, location)
        name = self.input_and_check("name", lambda value : self.llapi.is_name_correct(value))
        phone = self.input_and_check("phone", lambda value : self.llapi.is_phone_correct(value))
        address = self.input_and_check("address", lambda value : self.llapi.is_address_correct(value))
        homeline = self.input_and_check("homeline", lambda value : self.llapi.is_phone_correct(value))
        return name, phone, id, address, homeline, location


# input parameters and checks
    def input_and_check(self, info_type, check_fun):
        while True:
            value = input(f"Enter employee {info_type}: ")
            if not check_fun(value):
                print(f"Invalid employee {info_type}")
            else:
                return value

    def available_locations(self):
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

    def make_emp_or_sup_id(self, check, location):
        while True:
            all_id = self.llapi.all_employees()
            emp_or_sup = input("Make employee or supervisor(e/s): ").lower()
            if emp_or_sup == "e":
                id = EMP_ID + str(len(all_id) + 1).zfill(4)
                return id
            elif emp_or_sup == "s":
                if check == "True":
                    id = SUP_ID + str(len(all_id) + 1).zfill(4)
                    return id
                else: print(f"Invalid ther is alredy a supervisor in {location}")


# ------------------------------------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------------------------------------







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