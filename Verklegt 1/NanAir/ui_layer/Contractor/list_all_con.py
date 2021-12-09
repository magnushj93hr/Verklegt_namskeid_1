
class ListAllContractors:
    def __init__(self, llapi):
        self.llapi = llapi        
        self.variables = """
_______________________________________________________________________________________________________
|  Name                      Contact       Phone     Opening Hours       Location      Review(1 to 5) |
|                                                                                                     |"""

        self.footer = "|_____________________________________________________________________________________________________|"

    def list_all_contractors(self):
        """Returns list of all contractors"""
        all_con = self.llapi.all_contractors()
        self.print_contractors(all_con)
    
    def print_contractors(self, all_con):
        """Returns info about contractor"""
        print(self.variables)
        for con in all_con:
            print(f"|  {con.name:<27}{con.contact:<13}{con.phone:<14}{con.opening_hours:<17s}{con.location:<20s}{con.review:<8}|")
        print(self.footer)
