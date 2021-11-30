import csv
from models.RealEstate import RealEstate

class RealEstateDL:
    def __init__(self):
        self.filepath = "csv_files/RealEstate.csv"
    
    def get_all_RealEstates(self):
        ret_list = []
        with open(self.filepath, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                real = RealEstate(row["Address"],row["ID"], row["Amenities"], row["Condition"], row["Type"],row["Rooms"], row["Location"])
                ret_list.append(real)
        return ret_list

    def create_RealEstate(self, real):
        with open(self.filepath, 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ["Address","ID","Amenities","condition","Type","Rooms","Location"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'Address': real.address, "ID": real.realestate_id, "Amenities": real.amenities, "Condition": real.condition, 'Type': real.Type, 'Rooms': real.rooms, 'Location': real.location})

    def load_RealEstate_from_file(self, ID):
        pass

    def store_RealEstate_to_file(self, RealEstates):
        pass
