from data_layer.DLAPI import DLAPI



class ContractorLL:
    def __init__(self, dlapi):
        self.dlapi = dlapi


if __name__ == "__main__":
    empLL = ContractorLL(DLAPI())