from models.Location import Location

class CreateLocation:
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
|   Create New Location                                                                                           |
|_________________________________________________________________________________________________________________|
"""

    def create_location(self):
        """Creates location"""
        print(self.options)
        print("Welcome to the creation kit!")
        country, location, airport, phone, opening_hours = self.user_options()        
        location= Location(country, location, airport, phone, opening_hours)
        save = self.display_loc(location)
        if save:
            self.llapi.create_location(location)

    def user_options(self):
        """Returns contractor information"""
        country = self.input_and_check("country", lambda value : self.llapi.is_address_correct(value))
        location = self.input_and_check("location", lambda value : self.llapi.is_address_correct(value))
        airport = self.input_and_check("airport", lambda value : self.llapi.is_address_correct(value))
        phone = self.input_and_check("phone", lambda value : self.llapi.is_phone_correct(value))
        opening_hours = self.input_and_check("opening hours", lambda value : self.llapi.is_address_correct(value))
        return country, location, airport, phone, opening_hours


# input parameters and checks
    def input_and_check(self, info_type, check_fun):
        """Takes in input from user and checks if input is valid, returns the input if it's valid"""
        while True:
            value = input(f"Enter {info_type}: ")
            if not check_fun(value):
                print(f"Invalid {info_type}!")
            else:
                return value


    def display_loc(self, loc):
        """Prints new location info"""
        layout = f"""
      __|__                                                                                             __|__
*---o--(_)--o---*                                                                                 *---o--(_)--o---* 
___________________________________________________________________________________________________________________
|                                                                                                                 |
|       Home(home)         Employee(emp)         Real estate(real)         Cases(cases)        >Contractor(con)<  |
|_________________________________________________________________________________________________________________|
|                                                                                                                 |
|   Create New Location                                                                                           |
|_________________________________________________________________________________________________________________|
|                                                                                                                 |
|      Contractor                                                                                                 |
|                                                                                                                 |
|                 Country: {loc.country:87s}|
|                Location: {loc.location:87s}|
|                 Airport: {loc.airport:87s}|
|                   Phone: {loc.phone:87s}|
|           Opening hours: {loc.opening_hours:87s}|
|_________________________________________________________________________________________________________________|
"""
        print(layout)

        while True:
            save = input("Do you want to save location(y/n): ")
            if save == "y":
                return True
            elif save == "n":
                return False
            else:
                print("Invalid option")