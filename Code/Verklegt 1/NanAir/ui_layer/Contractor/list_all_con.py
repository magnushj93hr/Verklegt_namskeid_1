
class ListAllContractors:
    def __init__(self, llapi):
        self.llapi = llapi        
        self.variables = """
_________________________________________________________________________________________________________________________
|  Name                       Contact                  Phone        Opening Hours    Location            Review(1 to 5) |
|                                                                                                                       |"""

        self.footer = "|_______________________________________________________________________________________________________________________|"

    def list_all_contractors(self):
        """Returns list of all contractors"""
        all_con = self.llapi.all_contractors()
        self.print_contractors(all_con)
    
    def print_contractors(self, all_con):
        """Returns info about contractor"""
        while True:
            self.llapi.clear()
            print(self.variables)
            for con in all_con:
                print(f"|  {con.name:<27}{con.contact:<25}{con.phone:<13}{con.opening_hours:<17s}{con.location:<20s}{con.review:<15}|")
            print(self.footer)
            ret = input("Return to previous menu(y/n): ").lower()
            if ret == "y": break
