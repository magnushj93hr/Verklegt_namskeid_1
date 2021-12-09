import csv
from models.Location import Location


class LocationDL:
    def __init__(self):
        self.filepath = "Verklegt 1/NanAir/csv_files/Location.csv"
    
    def get_all_locations(self):
        """Returns a list of all location"""
        ret_list = []
        with open(self.filepath, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                loc = Location(row["country"], row["location"], row["airport"], row["phone"], row["opening hours"])
                ret_list.append(loc)
        return ret_list

    def create_location(self, loc):
        """Takes in information you need to create a location. The information will 
        be stored in a Location.csv file"""
        with open(self.filepath, 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ["country","location","airport","phone",'opening hours']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'country': loc.country, "location": loc.location, "airport": loc.airport, 'phone': loc.phone, 'opening hours': loc.opening_hours})