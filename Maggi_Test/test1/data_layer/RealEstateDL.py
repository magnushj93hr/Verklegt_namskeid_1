import csv

from models.RealEstate import RealEstate

class RealEstateDL:
    def __init__(self):
        self.filepath = "csv_files/RealEstate.csv"
    
    def get_all_realestate(self):
        ret_list = []
        with open(self.filepath, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                real = RealEstate(row["address"], row["size"], row["rooms"], row["id"], row["amenities"], row["location"])
                ret_list.append(real)
        return ret_list

    def create_realestate(self, real):
        with open(self.filepath, 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ["address","size","rooms",'id','amenities','location']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'address': real.address, "size": real.size, "rooms": real.rooms, 'id': real.id, 'amenities': real.amenities, 'location': real.location})