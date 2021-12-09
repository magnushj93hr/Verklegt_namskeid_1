from data_layer.DLAPI import DLAPI

MAX_NAME = 30
MAX_REL_ID = 6
MAX_PHONE = 12 
MIN_PHONE = 7
MAX_ADDRESS = 25
MAX_LOCATION = 25
MAX_ROOM = 10 


class InputCheck:
    def __init__(self, dlapi):
        self.dlapi = dlapi
    

# ----------------------------------------------------------------
# INPUT EMPLOYEE
    def check_location_append_to_list(self, location):
        """Takes in location and returns true if supervisor exists at that location"""
        new_list = []
        all_employees = self.dlapi.get_all_employees()
        for employee in all_employees:
            if employee.location == location:
                new_list.append(employee)
        return self.check_if_sup_in_location(new_list)

    def check_if_sup_in_location(self, emp_list):
        """Takes in employee list at a specific location and checks if there is a supervisor"""
        for emp in emp_list:
            if emp.supervisor == "y":
                return True
        return False
# ----------------------------------------------------------------
# INPUT CHECK
    def check_if_name_correct(self, name):
        """Takes in name and checks if the name is valid"""
        if len(name) <= MAX_NAME:
            if not name.isdigit():
                return True
        return False
    def check_if_phone_correct(self, phone):
        """Takes in phone number and checks if the phonenumber is valid"""
        if len(phone) <= MAX_PHONE and len(phone) >= MIN_PHONE:
            if phone.isdigit():
                return True
        return False
    def check_if_address_correct(self, address):
        """Takes in address and checks if the address is valid"""
        if len(address) <= MAX_ADDRESS:
            return True
        return False 
# ------------------------------
# for real estate ///
    def check_if_rel_id_correct(self, id):
        """Takes in real estate id and checks if the id is valid"""
        if id.isdigit():
            return True
        return False
    def check_if_size_correct(self, size):
        """Takes in size and checks if the size is valid"""
        if size.isdigit():
            return True
        return False
    def check_if_room_correct(self, room):
        """Takes in number of rooms and checks if the number is valid"""
        if room.isdigit():
            if len(room) <= MAX_ROOM:
                return True
        return False
# ----------------------------------------------------------------