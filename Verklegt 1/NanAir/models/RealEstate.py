class RealEstate:
<<<<<<< HEAD
    def __init__(self,address, realestate_id, amenities, conditions, type, rooms, location):
        self.address = address
        self.realestate_id = realestate_id
        self.amenities = amenities
        self.conditions = conditions
        self.type = type
        self.rooms = rooms
        self.location = location
        
=======
    def __init__(self, location, street_number, square_meters, room, type, Property_number):
        self.location = location
        self.street_number = street_number
        self.square_meters = square_meters
        self.room = room
        self.type = type
        self.Property_number = Property_number

    def __str__(self):
        return f"Location: {self.location}, street number: {self.street_number}, square: {self.square_meters}, room: {self.room}, type: {self.type}, Property_number: {self.Property}"
>>>>>>> b23aa8d87933193321eb1665db97b3b6f0285f3c
