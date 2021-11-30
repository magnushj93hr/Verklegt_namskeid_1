from data_layer.DLAPI import DLAPI


class WorkRequestLL:
    def __init__(self, dlapi):
        self.dlapi = dlapi
    
    def print_summary(self, summary):
        self.dlapi.print_summary(summary)
        

if __name__ == "__main__":
    empLL = WorkRequestLL(DLAPI())