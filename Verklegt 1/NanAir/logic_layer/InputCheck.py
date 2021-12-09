from data_layer.DLAPI import DLAPI

MAX_NAME = 30
MAX_REL_ID = 6
MAX_PHONE = 12  #Þarf að vera lengra?
MIN_PHONE = 7
MAX_ADDRESS = 25 # -||-
MAX_LOCATION = 25 # -||-
MAX_ROOM = 10 


class InputCheck:
    def __init__(self, dlapi):
        self.dlapi = dlapi
    

# ----------------------------------------------------------------
# INPUT EMPOYEE
    def check_location_append_to_list(self, location):
        new_list = []
        all_employees = self.dlapi.get_all_employees()
        for employee in all_employees:
            if employee.location == location:
                new_list.append(employee)
        return self.check_if_sup_in_location(new_list)

    def check_if_sup_in_location(self, emp_list):
        for emp in emp_list:
            if emp.supervisor == "y":
                return True
        return False
# ----------------------------------------------------------------
# INPUT CHECK
    def check_if_name_correct(self, name):
        if len(name) <= MAX_NAME:
            if not name.isdigit():
                return True
        return False
    def check_if_phone_correct(self, phone):
        if len(phone) <= MAX_PHONE and len(phone) >= MIN_PHONE:
            if phone.isdigit():
                return True
        return False
    def check_if_address_correct(self, address):
        if len(address) <= MAX_ADDRESS:
            return True
        return False 
# ------------------------------
# for real estate ///
    def check_if_rel_id_correct(self, id):
        if id.isdigit():
            return True
        return False
    def check_if_size_correct(self, size):
        if size.isdigit():
            return True
        return False
    def check_if_room_correct(self, room):
        if room.isdigit():
            if len(room) <= MAX_ROOM:
                return True
        return False
# ----------------------------------------------------------------