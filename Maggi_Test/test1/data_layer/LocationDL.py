import csv
from models.Location import Location


class LocationDL:
    def __init__(self):
        self.filepath = "Maggi_Test/test1/csv_files/Location.csv"
    
    def get_all_locations(self):
        ret_list = []
        with open(self.filepath, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                loc = Location(row["country"], row["airport"], row["phone"], row["opening hours"])
                ret_list.append(loc)
        return ret_list

    def create_location(self, loc):
        with open(self.filepath, 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ["country","airport","phone",'opening hours']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'country': loc.country, "airport": loc.airport, 'phone': loc.phone, 'opening hours': loc.opening_hours})