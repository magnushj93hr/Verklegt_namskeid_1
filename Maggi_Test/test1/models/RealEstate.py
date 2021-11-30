class RealEstate:
    def __init__(self, address, size, rooms, id, amenities, location):
        self.address = address
        self.size = size
        self.rooms = rooms
        self.id = id
        self.amenities = amenities
        self.location = location

    def __str__(self):
        return f"address: {self.address}, size: {self.size}, rooms: {self.rooms}, id {self.id}, amenities {self.amenities}, location {self.location}"