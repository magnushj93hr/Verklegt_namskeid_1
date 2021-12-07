class Contractor:
    def __init__(self, name, contact, phone, opening_hours, location, review = None):
        self.name = name
        self.contact = contact
        self.phone = phone
        self.opening_hours = opening_hours
        self.location = location
        self.review = review

    def __str__(self):
        return f"name: {self.name}, contact: {self.contact}, phone: {self.phone}, opening hours: {self.opening_hours}, location: {self.location}, review: {self.review}"