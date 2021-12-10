from data_layer.DLAPI import DLAPI
from models.RealEstate import RealEstate


class RealEstateLL:
    def __init__(self, dlapi):
        self.dlapi = dlapi
    
    def all_realestate(self):
        """Returns list of all real estates"""

        return self.dlapi.get_all_realestate()

    def create_realestate(self, real):
        """Takes in information and creates a real estate"""

        self.dlapi.create_realestate(real)
        
    def edit_realestate(self, edit_id):
        """Takes in ID and edits realestate"""

        self.dlapi.edit_realestate(edit_id)
    
    def search_realestate(self, real_id):
        """Takes in real estate ID and returns real estate"""

        all_realestate = self.dlapi.get_all_realestate()
        for realestate in all_realestate:
            if realestate.id == real_id:
                return realestate
        return None
    
    def filter_realestate(self, filter):
        """Returns real estate by location"""
        
        filtered_realestate = []
        all_realestate = self.dlapi.get_all_realestate()
        for realestate in all_realestate:
            if realestate.location == filter:
                filtered_realestate.append(realestate)
        return filtered_realestate

    
if __name__ == "__main__":
    realLL = RealEstateLL(DLAPI())