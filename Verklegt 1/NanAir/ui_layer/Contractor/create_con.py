from models.Contractor import Contractor


class CreateCon:
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
|   Create New Contractor                                                                                         |
|_________________________________________________________________________________________________________________|
"""


    def create_contractor(self):
        """Creates contractor"""
        print(self.options)
        print("Welcome to the creation kit!")
        name, phone, contact, location, opening_hours = self.user_options()        
        contr = Contractor(name, contact, phone, opening_hours, location)
        save = self.display_con(contr)
        if save:
            self.llapi.create_contractor(contr)

    def user_options(self):
        """Returns contractor information"""
        name = self.input_and_check("name", lambda value : self.llapi.is_name_correct(value))
        phone = self.input_and_check("phone number", lambda value : self.llapi.is_phone_correct(value))
        contact = self.input_and_check("contact", lambda value : self.llapi.is_address_correct(value))
        location = self.available_locations()
        open = self.input_and_check("opening hours", lambda value : self.llapi.is_address_correct(value))
        return name, phone, contact, location, open


# input parameters and checks
    def input_and_check(self, info_type, check_fun):
        """Takes in input from user and checks if input is valid, returns the input if it's valid"""
        while True:
            value = input(f"Enter {info_type} for contractor: ")
            if not check_fun(value):
                print(f"Invalid {info_type} for contractor!")
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


    def display_con(self, con):
        """Prints new contractor info"""
        header = """
      __|__                                                                                             __|__
*---o--(_)--o---*                                                                                 *---o--(_)--o---* 
___________________________________________________________________________________________________________________
|                                                                                                                 |
|       Home(home)         Employee(emp)         Real estate(real)         Cases(cases)        >Contractor(con)<  |
|_________________________________________________________________________________________________________________|
|                                                                                                                 |
|   Create New Contractor                                                                                         |
|_________________________________________________________________________________________________________________|"""
        
        new_con = f"""|                                                                                                                 |
|      Contractor                                                                                                 |
|                                                                                                                 |
|                    Name: {con.name:87s}|
|                 Contact: {con.contact:87s}|
|            Phone number: {con.phone:87s}|
|                Location: {con.location:87s}|
|           Opening hours: {con.opening_hours:87s}|
|_________________________________________________________________________________________________________________|
"""

        print(header)
        print(new_con)
        while True:
            save = input("Do you want to save contractor(y/n): ")
            if save == "y":
                return True
            elif save == "n":
                return False
            else:
                print("Invalid option")