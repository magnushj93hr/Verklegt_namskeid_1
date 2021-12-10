import csv
import shutil
from tempfile import NamedTemporaryFile
from models.RealEstate import RealEstate

class RealEstateDL:
    def __init__(self):
        self.filepath = "Verklegt 1/NanAir/csv_files/RealEstate.csv"
    
    def get_all_realestate(self):
        """Returns a list of all real estates"""
        ret_list = []
        with open(self.filepath, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                real = RealEstate(row["address"], row["size"], row["rooms"], row["id"], row["amenities"], row["location"])
                ret_list.append(real)
        return ret_list

    def create_realestate(self, real):
        """Takes in information you need to create a real estate. The information will 
        be stored in a RealEstate.csv file"""
        with open(self.filepath, 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ["address","size","rooms",'id','amenities','location']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'address': real.address, "size": real.size, "rooms": real.rooms, 'id': real.id, 'amenities': real.amenities, 'location': real.location})

    def edit_realestate(self, real):
        """Takes in case information and updates it"""
        temp_file = NamedTemporaryFile(mode = 'w', newline='', encoding='utf-8', delete=False)
        
        fieldnames = ["address","size","rooms",'id','amenities','location']
        with open(self.filepath, 'r', newline='', encoding='utf-8') as csvfile, temp_file:
            reader = csv.DictReader(csvfile, fieldnames=fieldnames)
            writer = csv.DictWriter(temp_file, fieldnames=fieldnames)

            for row in reader:
                if row['id'] == real.id:
                    print('updating row', row['id'])
                    writer.writerow({'address': real.address, "size": real.size, "rooms": real.rooms, 'id': real.id, 'amenities': real.amenities, 'location': real.location})
                    
                else:
                    row = {'address': row['address'], 'size': row['size'], 'rooms': row['rooms'], 'id': row['id'], 'amenities': row['amenities'], 'location': row['location']}
                    writer.writerow(row)

        shutil.move(temp_file.name, self.filepath)