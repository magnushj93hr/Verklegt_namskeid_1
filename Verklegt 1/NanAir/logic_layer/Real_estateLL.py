from data_layer.DLAPI import DLAPI


class RealEstateLL:
    def __init__(self, dlapi):
        self.dlapi = dlapi
    
    

if __name__ == "__main__":
    empLL = RealEstateLL(DLAPI())