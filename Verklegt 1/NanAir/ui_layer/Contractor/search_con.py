

class SearchCon:
    def __init__(self, llapi):
        self.llapi = llapi
    
    def search_con(self):
        """Displays available contractors and user inputs a contractor name"""
        while True:
            print('Available contractors to choose from: \n')
            for contractor in self.llapi.get_contractors_name():
                print(contractor)
            print()
            print("Quit by entering (q)")
            search_name = input("Enter contractor name: ")
            if search_name.lower().title() != "q":
                result = self.llapi.search_contractor(search_name)
                if result == None:
                    print("No contractor found")
                else:
                    self.print_searched_contractor(result)
            break
    
    def print_searched_contractor(self, contractor):
        """prints contractor infor"""
        layout = f"""
      __|__                                                                                             __|__
*---o--(_)--o---*                                                                                 *---o--(_)--o---* 
___________________________________________________________________________________________________________________
|                                                                                                                 |
|       Home        Employee          Real estate         Cases           >Contractor<           Location         |
|_________________________________________________________________________________________________________________|
|                                                                                                                 |
|      Contractor                                                                                                 |
|                                                                                                                 |
|                    Name: {contractor.name:87s}|
|                 Contact: {contractor.contact:87s}|
|                Location: {contractor.location:87s}|
|                   Phone: {contractor.phone:87s}|
|           Opening hours: {contractor.opening_hours:87s}|
|                  Review: {contractor.review:87s}|
|_________________________________________________________________________________________________________________|
"""
        print(layout)
