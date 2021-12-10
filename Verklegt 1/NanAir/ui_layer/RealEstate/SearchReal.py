from ui_layer.RealEstate.EditReal import EditReal
from ui_layer.RealEstate.CreateCase import CreateCase
from ui_layer.RealEstate.EditCase import EditCase

class SearchReal:
    
    def __init__(self, llapi, user):
        self.edit_real1 = EditReal(llapi, user)
        self.create_real1 = CreateCase(llapi, user)
        self.edit_case1 = EditCase(llapi, user)
        self.llapi = llapi
        self.user = user
        
    def search_output_printer(self, real):
        self.header = """
      __|__                                                                                             __|__
*---o--(_)--o---*                                                                                 *---o--(_)--o---* 
___________________________________________________________________________________________________________________
|                                                                                                                 |
|       Home(home)        Employee(emp)        >Real estate(real)<         Cases(cases)        Contractor(con)    |
|_________________________________________________________________________________________________________________|
|                                                                                                                 |
|   - 1               //Edit Real Estate information            - 2           //Create case                       |
|   - 3               //Edit case information                   - r           //return to previous menu           |
|_________________________________________________________________________________________________________________|"""
        self.edit_options = f"""|                                                                                                                 |
|      Real Estate: {real.id:94s}|
|                                                                                                                 |
|      Address: {real.address:98s}|
|      Size: {real.size:101s}|
|      Rooms: {real.rooms:100s}|
|      Amenities: {real.amenities:96s}|
|      Location: {real.location:97s}|
|      Return to previous menu                                                                                    |
|_________________________________________________________________________________________________________________|"""
        self.llapi.clear()
        print(f"{self.header}\n{self.edit_options}")


# ------------------------------------------------------------------------------------------------------------------
# Search for real estate
    def search_realestate(self):
        while True:
            print("Quit by entering (q)")
            self.search_id = input("Enter real estate id: ")
            if self.search_id != "q":
                result = self.llapi.search_realestate(self.search_id)
                if result == None:
                    print("Invalid ID")
                else:
                    return result
            else: return None
# ------------------------------------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------------------------------------
# Menu after search
    def prompt_input_search(self, result):
        while True:
            self.search_output_printer(result)
            command = input("Enter your input: ")
            if command == "1": 
                self.edit_real1.edit_real(result)
            elif command == "2":
                self.create_real1.create_case(result)
            elif command == "3": 
                self.edit_case1.edit_case(result)   
            elif command == "r": 
                self.llapi.clear()
                return
            else: print("Invalid option, try again!")
# ------------------------------------------------------------------------------------------------------------------
