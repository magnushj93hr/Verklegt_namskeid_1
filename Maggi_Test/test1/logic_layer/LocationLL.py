from data_layer.DLAPI import DLAPI
from models.Location import Location


class LocationLL:
    def __init__(self, dlapi):
        self.dlapi = dlapi
    
    def all_locations(self):
        return self.dlapi.get_all_locations()

    def create_location(self, loc):
        self.dlapi.create_location(loc)

    def get_locations_name(self):
        location_names = []
        all_locations = self.all_locations()
        for location in all_locations:
            location_names.append(location.location)
        return location_names

if __name__ == "__main__":
    locLL = LocationLL(DLAPI())