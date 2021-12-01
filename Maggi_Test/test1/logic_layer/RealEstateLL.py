from data_layer.DLAPI import DLAPI
from models.RealEstate import RealEstate


class RealEstateLL:
    def __init__(self, dlapi):
        self.dlapi = dlapi
    
    def all_realestate(self):
        return self.dlapi.get_all_realestate()

    def create_realestate(self, real):
        self.dlapi.create_realestate(real)
        
    def edit_realestate(self, realedit_id):
        self.dlapi.edit_realestate(realedit_id)

    
if __name__ == "__main__":
    realLL = RealEstateLL(DLAPI())