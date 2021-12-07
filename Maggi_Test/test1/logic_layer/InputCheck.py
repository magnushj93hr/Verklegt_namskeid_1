MAX_NAME = 40
MAX_ID = 4 
MAX_REL_ID = 6
MAX_PHONE = 7  #Þarf að vera lengra?
MAX_ADDRESS = 20 # -||-
MAX_LOCATION = 15 # -||-
MAX_ROOM = 10 


class InputCheck:
    def __init__(self, dlapi):
        pass
    
    
# ----------------------------------------------------------------
# INPUT CHECK
    def check_if_name_correct(self, name):
        if len(name) <= MAX_NAME:
            if not name.isdigit():
                return True
        return False
    def check_if_id_correct(self, id):
        if len(id) == MAX_ID:
            if id.isdigit():
                return True
        return False
    def check_if_phone_correct(self, phone):
        if len(phone) == MAX_PHONE:
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