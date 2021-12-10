
class ListAllLocations:
    def __init__(self, llapi):
        self.llapi = llapi
        self.variables = """
________________________________________________________________________________________________________________________
|  Country                    Location                   Airport                    Phone           Opening Hours      |
|                                                                                                                      |"""

        self.footer = "|______________________________________________________________________________________________________________________|"

    def list_all_locations(self):
        """Returns list of all locations"""
        all_loc = self.llapi.all_locations()
        self.print_contractors(all_loc)
    
    def print_contractors(self, all_loc):
        """Returns info about contractor"""
        while True:
            self.llapi.clear()
            print(self.variables)
            for loc in all_loc:
                print(f"|  {loc.country:<27}{loc.location:<27}{loc.airport:<27}{loc.phone:<16s}{loc.opening_hours:<19s}|")
            print(self.footer)
            cont = input("Return to previous menu(y/n): ").lower()
            if cont == "y": break
            
            
        
