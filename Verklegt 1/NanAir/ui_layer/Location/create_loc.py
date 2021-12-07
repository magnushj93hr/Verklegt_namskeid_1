from models.Location import Location

class CreateLoc:
    def __init__(self, llapi, user):
        self.user = user
        self.llapi = llapi
        self.options = """
      __|__                                                                                             __|__
*---o--(_)--o---*                                                                                 *---o--(_)--o---* 
___________________________________________________________________________________________________________________
|                                                                                                                 |
|       Home(home)         Employee(emp)         Real estate(real)         Cases(cases)        Contractor(con)    |
|_________________________________________________________________________________________________________________|
|                                                                                                                 |
|   Create New Location                                                                                           |
|_________________________________________________________________________________________________________________|
"""

    def draw_options(self):
        print(self.options)
        return self.create_location()

    def create_location(self):
        country = input("Enter Country name: ")
        airport = input("Enter aiport:")
        phone = input("Enter locations phone number: ")
        opening_hours = input("Enter locations opening hours: ")
        loc = Location(country, airport, phone, opening_hours)
        self.display_loc(loc)
        save = input("Do you want to save the information (yes/no)? ")
        if save == "yes":
            self.llapi.create_location(loc)

    def display_loc(self, loc):
        header = """
      __|__                                                                                             __|__
*---o--(_)--o---*                                                                                 *---o--(_)--o---* 
___________________________________________________________________________________________________________________
|                                                                                                                 |
|       Home(home)         Employee(emp)         Real estate(real)         Cases(cases)        Contractor(con)    |
|_________________________________________________________________________________________________________________|
|                                                                                                                 |
|   Create New Location                                                                                           |
|_________________________________________________________________________________________________________________|"""
        
        new_loc = f"""|                                                                                                                 |
|   Create New Location                                                                                           |
|                                                                                                                 |
|                 Country: {loc.country:87s}|
|                 Airport: {loc.airport:87s}|
|                   Phone: {loc.phone:87s}|
|           Opening hours: {loc.opening_hours:87s}|
|_________________________________________________________________________________________________________________|
"""

        print(header)
        print(new_loc)