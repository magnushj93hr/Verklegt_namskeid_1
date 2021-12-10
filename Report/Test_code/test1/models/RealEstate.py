SIZE_END = "m2"

class RealEstate:
    def __init__(self, address, size, rooms, id, amenities, location):
        self.address = address
        self.size = self.add_m2_to_size(size)
        self.rooms = rooms
        self.id = id
        self.amenities = amenities
        self.location = location

    def add_m2_to_size(self, size):
        if SIZE_END not in size: 
            final_size = size + SIZE_END
            return final_size
        else:
            return size

    def __str__(self):
        return f"address: {self.address}, size: {self.size}, rooms: {self.rooms}, id: {self.id}, amenities: {self.amenities}, location: {self.location}"