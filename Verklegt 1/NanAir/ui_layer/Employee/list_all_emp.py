
class ListAllEmployee:
    def __init__(self, llapi):
        self.llapi = llapi        
        self.variables = """
___________________________________________________________________________________________________________________________________________________________________________________________
|  Name                            Supervisor     ID        Homeline       GSM           Address                    Location                   Email                                      |
|                                                                                                                                                                                         |"""

        self.footer = "|_________________________________________________________________________________________________________________________________________________________________________________________|"

    def list_all_employees(self):
        """Returns list of all employees"""

        all_emps = self.llapi.all_employees()
        self.print_employees(all_emps)
        self.filter_by_location()
        
# Asks to filter by location
    def filter_by_location(self):
        """List filtered by location"""
        while True:
            filter_input = input("Do you want to filter by location(y/n)?: ")
            if filter_input == 'y':
                location = self.available_locations()
                result = self.llapi.filter_employee(location)
                self.print_employees(result)
            elif filter_input == "n":
                return
            else:
                print("Invalid option")

# Gives available locations
    def available_locations(self):
        """List of available locations"""
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
    
    def print_employees(self, all_emps):
        """Returns info about employee"""
        print(self.variables)
        for emp in all_emps:
            print(f"|  {emp.name:<32}{emp.supervisor:<15}{emp.id:<10}{emp.homeline:<15s}{emp.phone:<14s}{emp.address:<27}{emp.location:<27}{emp.email:<43s}|")
        print(self.footer)
