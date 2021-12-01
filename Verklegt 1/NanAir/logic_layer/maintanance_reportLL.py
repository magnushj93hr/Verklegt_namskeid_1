from data_layer.DLAPI import DLAPI


class CaseLL:
    def __init__(self, dlapi):
        self.dlapi = dlapi

    def see_status(self, status):
        self.dlapi.see_status(status)
        
    def search_for_keywords(self,search):
        self.dlapi.search_for_keywords(search)
        
    def create_warning(self,warning):
        self.dlapi.create_warning(warning)
        
    def pay_contractor(self,pay):
        self.dlapi.pay_contractor(pay)