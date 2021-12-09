
class ListReal:

    def __init__(self, llapi, user):
        self.llapi = llapi
        self.user = user
        self.variables = """
_____________________________________________________
|   ID      Address            Location             |
|                                                   |"""
        self.footer = "|___________________________________________________|"

    def real_printer(self):
        print(self.variables)
        all_real = self.llapi.all_realestate()
        for real in all_real:
            print(f"|   {real.id:<8s}{real.address:<20s}{real.location:<20s}|")
        print(self.footer)