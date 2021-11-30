import csv


class RealEstateDL:
    def __init__(self):
        self.filepath = "csv_files/RealEstate.csv"

    def load_real_estate_from_file(self):
        """[This function opens the file RealEstate.csv, reads it and returns a list.]
        Returns:
            [list]: [list of the Real estate]
        """
        ret_list = []
        with open(self.filepath, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                real = RealEstate(row["location"], row["street_number"], row["square_meters"], row["room"], row["type"], row["Property_number"])
                ret_list.append(real)
                print(ret_list)
        return ret_listSS

    def store_real_to_file(self):
        pass

