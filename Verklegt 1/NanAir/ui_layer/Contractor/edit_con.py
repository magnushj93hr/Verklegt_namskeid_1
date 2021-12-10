from ui_layer.Contractor.create_con import CreateCon

class EditCon:
    def __init__(self, llapi):
        self.llapi = llapi
        self.creat_con = CreateCon(llapi)
    

    def print_contr_as_menu(self, emp):
        """Prints contractor"""
        edit_options = f"""
      __|__                                                                                             __|__
*---o--(_)--o---*                                                                                 *---o--(_)--o---* 
___________________________________________________________________________________________________________________
|                                                                                                                 |
|       Home        Employee          Real estate         Cases           >Contractor<           Location         |
|_________________________________________________________________________________________________________________|
|                                                                                                                 |
|    1 - Name: {emp.name:99s}|
|    2 - Contact: {emp.contact:96s}|
|    3 - Location: {emp.location:95s}|
|    4 - Phone: {emp.phone:98s}|
|    5 - Openin hours: {emp.opening_hours:91s}|
|    r - Return to previous menu                                                                                  |
|_________________________________________________________________________________________________________________|
"""
        self.llapi.clear()
        print(edit_options)

    def promt_input(self):
        contractor_name = self.select_contr()
        if contractor_name == None:
            return
        contractor = self.llapi.search_contractor(contractor_name)
        self.edit_contr(contractor)

    def select_contr(self):
        contractors = self.llapi.get_contractors_name()
        while True:
            print('Available contractors to choose from: \n')
            for contractor in contractors:
                print(contractor)
            print()
            print("Enter (q) to quit")
            contractor = input("Enter contractor: ").lower().title()
            if contractor == "q":
                return
            elif contractor not in contractors:
                print("Contractor not found")
            else:
                return contractor
                

    def edit_contr(self, contr):
        """Asks user to enter edit option"""
        while True:
            self.print_contr_as_menu(contr)
            command = input("Enter edit option: ")
                
            if command == "1":
                contr.name = self.input_and_check("name", lambda value : self.llapi.is_name_correct(value))
                self.llapi.edit_contractor(contr)
            elif command == "2":
                contr.address = self.input_and_check("contact", lambda value : self.llapi.is_name_correct(value))
                self.llapi.edit_contractor(contr)
            elif command == "3":
                contr.location = self.creat_con.available_locations()
                self.llapi.edit_contractor(contr)
            elif command == "4":
                contr.phone = self.input_and_check("phone", lambda value : self.llapi.is_phone_correct(value))
                self.llapi.edit_contractor(contr)
            elif command == "5":
                contr.opening_hours = input("Enter opening hours( h-h or 24/7 if its open twenty four hours: ")
            elif command == "r":
                return
            else:
                print("Invalid option")

    def input_and_check(self, info_type, check_fun):
        """Takes in input from user and checks if input is valid, returns the input if it's valid"""
        while True:
            value = input(f"Enter {info_type}: ")
            if not check_fun(value): print(f"Invalid {info_type}")
            else: return value
    