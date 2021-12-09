
class ListAllEmployee:
    def __init__(self, llapi):
        self.llapi = llapi
        self.header = """
      __|__                                                                                             __|__
*---o--(_)--o---*                                                                                 *---o--(_)--o---* 
___________________________________________________________________________________________________________________
|                                                                                                                 |
|       Home(home)        >Employee(emp)<        Real estate(real)         Cases(cases)        Contractor(con)    |
|_________________________________________________________________________________________________________________|
|                                                                                                                 |"""
        
        self.variables = """
_________________________________________________________________________________________________________________________________________________________________________
|   Name                   ID          Homeline         GSM           Address                 Location             Email                                Supervisor      |
|                                                                                                                                                                       |"""

        self.footer = "|_______________________________________________________________________________________________________________________________________________________________________|"

    def list_all_employees(self):
        all_emps = self.llapi.all_employees()
        self.print_employees(all_emps)
        self.filter_by_location()
        
# Asks to filter by location
    def filter_by_location(self):
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

    def available_locations(self):
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
        print(self.variables)
        for emp in all_emps:
            print(f"|   {emp.name:<23}{emp.id:<12}{emp.homeline:<17s}{emp.phone:<14s}{emp.address:<24}{emp.location:<21}{emp.email:<37s}{emp.supervisor:<16}|")
        print(self.footer)
