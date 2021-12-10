
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
        """Gets all real estates and calls print and sort functions"""
        self.llapi.clear()
        all_real = self.llapi.all_realestate()
        self.output_printer(all_real)
        self.sort_by_location()

    def output_printer(self, real):
        """Prints all real estate"""
        data = ""
        for real in real:
            data += f"\n|   {real.id:<8s}{real.address:<20s}{real.location:<20s}|"
        print(f"{self.variables}{data}\n{self.footer}")

    def sort_by_location(self):
        """Filters by location"""
        while True:
            filter_input = input("Do you want to filter by location(y/n)?: ")
            if filter_input == 'y':
                filter_location = self.location_in()
                result = self.llapi.filter_realestate(filter_location)
                if result != []:
                    self.output_printer(result)
                else: print("No real estate found.")
            else: break

    def location_in(self):
        """User inputs location he wants to filter by"""
        while True:
            self.llapi.clear()
            print('Available locations to choose from:')
            for location in self.llapi.get_locations_name():
                print(location)
            location = str(input("Enter location: ")).lower().capitalize()
            if location in self.llapi.get_locations_name(): return location
            else: print("Invalid location")