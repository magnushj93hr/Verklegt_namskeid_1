import ast

class EditReal:
    
    def __init__(self, llapi, user):
        self.llapi = llapi


    def input_real_and_check(self, info_type, check_fun):
        """Takes in real estate info type and checks if the value is valid"""
        while True:
            value = input(f"Enter the {info_type} of the real estate: ")
            if not check_fun(value): print(f"Invalid {info_type} for the real estate")
            else: return value

# ------------------------------------------------------------------------------------------------------------------
# -- Print Real estate information
    def print_real_as_menu(self, real):
        """print real estate info"""
        self.header = f"""
      __|__                                                                                             __|__
*---o--(_)--o---*                                                                                 *---o--(_)--o---* 
___________________________________________________________________________________________________________________
|                                                                                                                 |
|       Home        Employee         >Real estate<         Cases            Contractor           Location         |
|_________________________________________________________________________________________________________________|
|                                                                                                                 |
|                                  You are currently editing Real Estate: {real.id}                                    |
|                                   - r            //Return to previous menu                                      |
|_________________________________________________________________________________________________________________|"""
        self.edit_options = f"""|                                                                                                                 |
|      Real Estate: {real.id:94s}|
|                                                                                                                 |
|    1 - Address: {real.address:96s}|
|    2 - Size: {real.size:99s}|
|    3 - Rooms: {real.rooms:98s}|
|    4 - Amenities: {real.amenities:94s}|
|    5 - Location: {real.location:95s}|
|_________________________________________________________________________________________________________________|
"""
        self.llapi.clear()
        print(f"{self.header}\n{self.edit_options}")

# -- Start of edit
    def edit_real(self, real):
        """Search for real estate to edit"""
        real = self.llapi.search_realestate(real.id)
        if real == None:
            print("The real estate id was not found")
            print(self.edit_options) 
            return
        self.promt_edit_real(real)

    def promt_edit_real(self, real):
        """Asks user to input edit real estate option"""
        while True:
            self.print_real_as_menu(real)
            command = input("Enter edit option: ")
            
            if command == "1":
                real.address = self.input_real_and_check("address", lambda value : self.llapi.is_address_correct(value))
                self.llapi.edit_realestate(real)
            elif command == "2":
                real.size = self.input_real_and_check("size", lambda value : self.llapi.check_if_size_correct(value))
                self.llapi.edit_realestate(real)
            elif command == "3":
                real.rooms = self.input_real_and_check("rooms", lambda value : self.llapi.check_if_room_correct(value))
                self.llapi.edit_realestate(real)
            elif command == "4":
                self.amenities_ui(real)
                real.amenities = self.amenities_logic(real)
                self.llapi.edit_realestate(real)
            elif command == "5":
                real.location = self.available_locations()
                self.llapi.edit_realestate(real)
            elif command == "r":
                return
            else:
                print("Invalid option")
# -- end of edit real main
# -- edit amenities ui
    def amenities_ui(self, ame):
        self.edit_ame = f"""
        Amenities: {ame.amenities}
        1 - Remove
        2 - Add
        """
        print(self.edit_ame)

    def amenities_logic(self, ame):
        """amenities options, add or remove"""
        input_ame = input("Enter a option: ")
        if input_ame == "1":
            list_ame = self.amenities_remove(ame)
        elif input_ame == "2":
            list_ame = self.amenities_add(ame)
        return list_ame

    def amenities_remove(self, ame):
        """Remove amenities from amenities list"""
        while True:
            print(ame.amenities)
            rem_input = input("Enter a amenitie to remove: ")
            if rem_input in ame.amenities: 
                new_list = ast.literal_eval(ame.amenities)
                new_list.remove(rem_input)
                return new_list
            else: print(f"{rem_input} is not in the amenities")

    def amenities_add(self, ame):
        """Add amenities to amenities list"""
        print(ame.amenities)
        list_ame = input("Enter a amenities to add, seperated by(,): ").split(",")
        if ame.amenities == "":
            ame.amenities = []
        return ame.amenities.extend(list_ame)
# -- end of edit amenities

    def available_locations(self):
        """Displays available locations and returns the location the user chooses"""
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