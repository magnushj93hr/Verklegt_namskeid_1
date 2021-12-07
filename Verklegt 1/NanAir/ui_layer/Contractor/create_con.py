from models.Contractor import Contractor
    
class CreateReal:
    def __init__(self, llapi, user):
        self.user = user
        self.llapi = llapi
        self.options = """
      __|__                                                                                             __|__
*---o--(_)--o---*                                                                                 *---o--(_)--o---* 
___________________________________________________________________________________________________________________
|                                                                                                                 |
|       Home(home)        Employee(emp)        >Real estate(real)<         Cases(cases)        >Contractor(con)<  |
|_________________________________________________________________________________________________________________|
|                                                                                                                 |
|   Create New Contractor                                                                                         |
|_________________________________________________________________________________________________________________|
"""

    def draw_options(self):
        print(self.options)
        return self.create_contractor()  
    
    def user_options(self):
        while True:
            name = input("Enter contractor name: ")
            name_c = self.llapi.check_if_name_correct(name)
            if name_c == False:
                print("invalid contractor name")
            else: break
#----
        while True:
            phone = input("Enter contractor phone number: ")
            phone_c = self.llapi.check_if_phone_correct(phone)
            if phone_c == False:
                print("invalid contractor phone number")
            else: break
#----
        while True:
            contact = input("Enter contractor contact: ")
            contact_c = self.llapi.check_if_location_correct(contact)
            if contact_c == False:
                print("invalid contracotr contact")
            else: break
#----
        while True:
            location = input("Enter contractor location: ")
            location_c = self.llapi.check_if_location_correct(location)
            if location_c == False:
                print("invalid Contractor location")
            else: break
#----
        while True:
            open = input("Enter opening hours for contractor: ")
            open_c = self.llapi.check_if_location_correct(open)
            if open_c == False:
                print("invalid opening hours for Contractor ")
            else: break
#----
        return name, phone, contact, location, open

    def create_contractor(self):
        name, phone, contact, location, opening_hours = self.user_options()        
        contr = Contractor(name, contact, phone, opening_hours, location)
        self.display_contr(contr)
        save = input("Do you want to save the information (yes/no)? ")
        if save == "yes":
            self.llapi.create_contractor(contr)


    def display_emp(self, contr):
        header = """
      __|__                                                                                             __|__
*---o--(_)--o---*                                                                                 *---o--(_)--o---* 
___________________________________________________________________________________________________________________
|                                                                                                                 |
|       Home(home)        >Employee(emp)<        Real estate(real)         Cases(cases)        Contractor(con)    |
|_________________________________________________________________________________________________________________|
|                                                                                                                 |
|   Create New Employee                                                                                           |
|_________________________________________________________________________________________________________________|"""
        
        new_contr = f"""|                                                                                                                 |
|   Create New Employee                                                                                           |
|                                                                                                                 |
|                  Name: {contr.country:87s}|
|               Contact: {contr.airport:87s}|
|                 Phone: {contr.phone:87s}|
|         Opening hours: {contr.opening_hours:87s}|
|              Location: {contr.location:87s}|
|_________________________________________________________________________________________________________________|
"""

        print(header)
        print(new_contr)

                        