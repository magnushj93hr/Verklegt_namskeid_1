from models.Location import Location


OPEN_HOURS = "24/7"

class CreateLocation:

    def __init__(self, llapi, user):
        self.llapi = llapi
        self.user = user

    def input_and_check(self, info_type, check_fun):
        """Takes in user input and checks if it's valid"""
        while True:
            value = input(f"Enter the {info_type} of the new location: ")
            if not check_fun(value): print(f"Invalid {info_type} for new location")
            else: return value

    def user_options(self):
        """Returns employee information"""
        location = self.input_and_check("name", lambda value : self.llapi.check_if_location_correct(value))
        country = self.input_and_check("country", lambda value : self.llapi.is_name_correct(value))
        airport = self.input_and_check("airport", lambda value : self.llapi.is_name_correct(value))
        phone = self.input_and_check("phone", lambda value : self.llapi.is_phone_correct(value))
        opening_hours = OPEN_HOURS
        return location, country, airport, phone, opening_hours

    def create_location(self):
        """Create location"""
        location, country, airport, phone, opening_hours = self.user_options()
        loc = Location(country, location, airport, phone, opening_hours)
        save = self.display_loc(loc)
        if save == True:
            self.llapi.create_location(loc)

    def display_loc(self, loc):
        """prints location info"""
        header = """
      __|__                                                                                             __|__
*---o--(_)--o---*                                                                                 *---o--(_)--o---* 
___________________________________________________________________________________________________________________
|                                                                                                                 |
|        Home        Employee          Real estate         Cases           Contractor          >Location <        |
|_________________________________________________________________________________________________________________|
|                                                                                                                 |
|   Create New Location                                                                                           |
|_________________________________________________________________________________________________________________|"""
        
        new_emp = f"""|                                                                                                                 |
|      Location                                                                                                   |
|                                                                                                                 |
|                Location: {loc.location:87s}|
|                 Country: {loc.country:87s}|
|                 Airport: {loc.airport:87s}|
|                   Phone: {loc.phone:87s}|
|           Opening hours: {loc.opening_hours:87s}|
|_________________________________________________________________________________________________________________|
"""
        self.llapi.clear()
        print(f"{header}\n{new_emp}")

        while True:
            save = input("Do you want to save the new location(y/n): ")
            if save == "y": return True
            elif save == "n": return False
            else: print("Invalid option")