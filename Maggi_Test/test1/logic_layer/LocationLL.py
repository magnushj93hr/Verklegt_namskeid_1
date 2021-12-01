from data_layer.DLAPI import DLAPI
from models.Location import Location


class LocationLL:
    def __init__(self, dlapi):
        self.dlapi = dlapi
    
    def all_location(self):
        return self.dlapi.get_all_location()

    def create_location(self, loc):
        self.dlapi.create_location(loc)
    
if __name__ == "__main__":
    locLL = LocationLL(DLAPI())