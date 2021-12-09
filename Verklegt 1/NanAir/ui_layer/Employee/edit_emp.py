class EditEmployee:
    def __init__(self, llapi):
        self.llapi = llapi


    def print_emp_as_menu(self, emp):
        """Prints employee menu"""

        edit_options = f"""
      __|__                                                                                             __|__
*---o--(_)--o---*                                                                                 *---o--(_)--o---* 
___________________________________________________________________________________________________________________
|                                                                                                                 |
|       Home        >Employee<          Real estate         Cases           Contractor           Location         |
|_________________________________________________________________________________________________________________|
|                                                                                                                 |
|      Employee: {emp.id:97s}|
|                                                                                                                 |
|    1 - Name: {emp.name:99s}|
|    2 - Home address: {emp.address:91s}|
|    3 - Home phonenumber: {emp.homeline:87s}|
|    4 - GSM: {emp.phone:100s}|
|    5 - Location: {emp.location:95s}|
|    r - Return to previous menu                                                                                  |
|_________________________________________________________________________________________________________________|
"""
        print(edit_options)


    def edit_employee(self):
        """"""

        #check if id is len 4
        print("Quit by entering (q)")
        while True:
            edit_id = str(input("Enter employee id: "))
            if edit_id != "q":
                emp = self.llapi.search_employee(edit_id)
                self.promt_edit(emp)
            elif emp == None: 
                print("The employee id was not found")
            else: 
                return

    def promt_edit(self, emp):
        while True:
            self.print_emp_as_menu(emp)
            command = input("Enter edit option: ")
                
            if command == "1":
                emp.name = self.input_and_check("name", lambda value : self.llapi.is_name_correct(value))
                self.llapi.edit_employee(emp)
            elif command == "2":
                emp.address = self.input_and_check("address", lambda value : self.llapi.is_address_correct(value))
                self.llapi.edit_employee(emp)
            elif command == "3":
                emp.homeline = self.input_and_check("homeline", lambda value : self.llapi.is_phone_correct(value))
                self.llapi.edit_employee(emp)
            elif command == "4":
                emp.phone = self.input_and_check("phone", lambda value : self.llapi.is_phone_correct(value))
                self.llapi.edit_employee(emp)
            elif command == "5":
                emp.location = self.available_locations()
                self.llapi.edit_employee(emp)
            elif command == "r":
                return
            else:
                print("Invalid option")

    def input_and_check(self, info_type, check_fun):
        while True:
            value = input(f"Enter employee {info_type}: ")
            if not check_fun(value): print(f"Invalid employee {info_type}")
            else: return value