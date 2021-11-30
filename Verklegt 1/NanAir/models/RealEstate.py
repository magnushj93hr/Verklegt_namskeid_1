class RealEstate:
    def __init__(self, location, street_number, square_meters, room, type, Property_number):
        self.location = location
        self.street_number = street_number
        self.square_meters = square_meters
        self.room = room
        self.type = type
        self.Property_number = Property_number

    def __str__(self):
        return f"Location: {self.location}, street number: {self.street_number}, square: {self.square_meters}, room: {self.room}, type: {self.type}, Property_number: {self.Property}"