

class SearchEmp:
    def __init__(self, llapi):
        self.llapi = llapi
    
    def search_employee(self):
        """Search for employee"""
        while True:
            print("Quit by entering (q)")
            search_id = input("Enter employee id: ")
            if search_id.lower() != "q":
                result = self.llapi.search_employee(search_id)
                if result == None:
                    print("No employee found")
                else:
                    self.print_searched_emp(result)
            break
    
    def print_searched_emp(self, result):
        """Prints employee info"""
        layout = f"""
      __|__                                                                                             __|__
*---o--(_)--o---*                                                                                 *---o--(_)--o---* 
___________________________________________________________________________________________________________________
|                                                                                                                 |
|       Home        >Employee<          Real estate         Cases           Contractor           Location         |
|_________________________________________________________________________________________________________________|
|                                                                                                                 |
|      Employee                                                                                                   |
|                                                                                                                 |
|                    Name: {result.name:87s}|
|                      ID: {result.id:87s}|
|            Home address: {result.address:87s}|
|        Home phonenumber: {result.homeline:87s}|
|                     GSM: {result.phone:87s}|
|                   Email: {result.email:87s}|
|                Location: {result.location:87s}|
|              Supervisor: {result.supervisor:87s}|
|_________________________________________________________________________________________________________________|
"""
        self.llapi.clear()
        print(layout)